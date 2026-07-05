#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import math
import re
import sys
from contextlib import redirect_stdout, redirect_stderr
from datetime import datetime
from pathlib import Path

import pandas as pd
import pyomo.environ as pyo

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
if str(PROJECT_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT / "src"))

from src.data_loader import load_inputs
from src.preprocessing import preprocess
from src.solve_model import solve_model
from src.utils import ensure_dir, load_json, resolve_project_path
from src_lbbd.lbbd_master import build_lbbd_master, apply_hard_no_slack
from src_lbbd.lbbd_export import export_all, print_summary
from src_lbbd.lbbd_subproblem import extract_interface, solve_type_assignment_lp, add_type_assignment_cut


class TeeStream:
    def __init__(self, *streams):
        self.streams = [s for s in streams if s is not None]
    def write(self, msg):
        for s in self.streams:
            s.write(msg)
        self.flush()
        return len(msg)
    def flush(self):
        for s in self.streams:
            s.flush()


def parse_args():
    p = argparse.ArgumentParser(description="Logic-Based Benders Decomposition for the EV charging infrastructure model.")
    p.add_argument("--dataset", choices=["small", "full"], default="small")
    p.add_argument("--scenario", choices=["no_redirection", "with_redirection"], default="with_redirection")
    p.add_argument("--project-root", default=str(PROJECT_ROOT))
    p.add_argument("--threads", type=int, default=None)
    p.add_argument("--master-gap", type=float, default=0.001)
    p.add_argument("--subproblem-gap", type=float, default=0.001)
    p.add_argument("--lbbd-gap", type=float, default=0.001)
    p.add_argument("--max-iterations", type=int, default=25)
    p.add_argument("--time-limit", type=int, default=None)
    p.add_argument("--disable-pv", action="store_true")
    p.add_argument("--disable-bess", action="store_true")
    p.add_argument("--hard-no-slack", action="store_true")
    p.add_argument("--write-lp", action="store_true")
    p.add_argument("--cut-strategy", choices=["standard", "corepoint", "mw", "pareto"], default="standard")
    p.add_argument("--max-cuts-per-iteration", type=int, default=None)
    p.add_argument("--min-cut-violation", type=float, default=1e-5)
    p.add_argument("--core-weight", type=float, default=0.35)
    p.add_argument("--core-floor-kwh", type=float, default=0.0)
    p.add_argument("--pareto-tolerance", type=float, default=1e-7)
    return p.parse_args()

def load_configs(root: Path, dataset: str):
    raw_paths = load_json(root / "config" / "paths.json")
    cfg = load_json(root / "config" / "model_config.json")
    solver_cfg = load_json(root / "config" / "solver_gurobi.json")
    paths = dict(raw_paths["datasets"][dataset])
    paths["dataset"] = dataset
    paths["pvgis_excel"] = raw_paths["pvgis_excel"]
    paths["spot_price_csv"] = raw_paths["spot_price_csv"]
    paths["runs_root"] = raw_paths["runs_root"]
    for key in ["demand_shapefile", "distance_csv", "parking_shapefile", "pvgis_excel", "spot_price_csv", "runs_root"]:
        paths[key] = str(resolve_project_path(root, paths[key]))
    return paths, cfg, solver_cfg


def make_run_dir(paths, dataset, scenario, disable_pv, disable_bess, cut_strategy="standard"):
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    tech = ("noPV" if disable_pv else "withPV") + "_" + ("noBESS" if disable_bess else "withBESS")
    strategy = str(cut_strategy or "standard").lower().replace("/", "-").replace("\\", "-").replace(" ", "_")
    label = "LBBD_Standard" if strategy == "standard" else f"LBBD_advCuts_{strategy}"
    d = Path(paths["runs_root"]) / f"{stamp}_{dataset}_{scenario}_{label}_{tech}"
    for sub in ["logs", "results", "model", "nodefiles", "iterations", "subproblems"]:
        ensure_dir(d / sub)
    return d

def finite_gap(ub: float, lb: float) -> float:
    if not (math.isfinite(ub) and math.isfinite(lb)):
        return float("inf")
    return max(0.0, ub - lb) / max(1.0, abs(lb))



def update_core_interface(core: dict | None, interface: dict, weight: float, floor: float = 0.0) -> dict:
    # Convex averaging preserves R/W/G balance when the stored interfaces are balanced.
    if core is None:
        return {fam: dict(vals) for fam, vals in interface.items() if fam in {"R", "W", "G"}}
    w = min(1.0, max(0.0, float(weight)))
    out = {}
    for fam in ["R", "W", "G"]:
        keys = set(core.get(fam, {})) | set(interface.get(fam, {}))
        vals = {}
        for k in keys:
            v = (1.0 - w) * float(core.get(fam, {}).get(k, 0.0)) + w * float(interface.get(fam, {}).get(k, 0.0))
            vals[k] = max(float(floor), v) if floor > 0 and v > 0 else max(0.0, v)
        out[fam] = vals
    return out


def _candidate_violation(candidate) -> float:
    if hasattr(candidate, "violation"):
        return float(getattr(candidate, "violation", 0.0) or 0.0)
    if isinstance(candidate, dict):
        return float(candidate.get("violation", 0.0) or 0.0)
    return 0.0


def select_cut_candidates(candidates: list, max_cuts: int | None, min_violation: float) -> list:
    kept = [c for c in candidates if _candidate_violation(c) > float(min_violation)]
    kept.sort(key=_candidate_violation, reverse=True)
    if max_cuts is not None and int(max_cuts) > 0:
        return kept[: int(max_cuts)]
    return kept


def parse_gurobi_final_bound(log_path: Path):
    text = log_path.read_text(encoding="utf-8", errors="replace") if log_path.exists() else ""
    pat = re.compile(r"Best objective\s+([-+0-9.eE]+),\s+best bound\s+([-+0-9.eE]+),\s+gap\s+([-+0-9.eE%]+)")
    matches = pat.findall(text)
    if not matches:
        return None, None, None
    obj, bound, gap = matches[-1]
    gap_val = None
    try:
        gap_val = float(gap.rstrip("%")) / (100.0 if gap.endswith("%") else 1.0)
    except Exception:
        pass
    return float(obj), float(bound), gap_val


def snapshot_vars(model):
    snap = {}
    for comp in model.component_objects(pyo.Var, active=True):
        vals = {}
        for idx in comp:
            vals[idx] = pyo.value(comp[idx], exception=False)
        snap[comp.name] = vals
    return snap


def restore_vars(model, snap):
    for name, vals in snap.items():
        comp = model.find_component(name)
        if comp is None:
            continue
        for idx, val in vals.items():
            if val is not None:
                comp[idx].set_value(val, skip_validation=True)


def solve_master(model, solver_cfg, run_dir: Path, iteration: int):
    log_path = run_dir / "logs" / f"gurobi_master_iter_{iteration:03d}.log"
    solver_cfg_iter = dict(solver_cfg)
    old_log = run_dir / "logs" / "gurobi_run.log"
    if old_log.exists():
        old_log.unlink()
    res = solve_model(model, solver_cfg_iter, run_dir)
    if old_log.exists():
        log_path.write_text(old_log.read_text(encoding="utf-8", errors="replace"), encoding="utf-8", errors="replace")
    inc, bound, mip_gap = parse_gurobi_final_bound(log_path)
    if inc is None:
        inc = float(pyo.value(model.obj))
    if bound is None:
        bound = inc
    return res, inc, bound, mip_gap


def run_lbbd_loop(model, data, cfg, solver_cfg, run_dir: Path, args, stage_label: str = "lbbd"):
    best_lb = -float("inf")
    best_rows = []
    best_snapshot = None
    global_ub = float("inf")
    history, sp_rows, cut_rows = [], [], []
    cut_tol = float(getattr(args, "min_cut_violation", 1e-5))
    cut_strategy = str(getattr(args, "cut_strategy", "standard")).lower()
    if cut_strategy in {"mw", "pareto"}:
        cut_strategy = "corepoint"
    core_interface = None
    converged = False
    for it in range(1, int(args.max_iterations) + 1):
        print(f"\n========== LBBD ITERATION {it} ==========")
        res, master_incumbent, master_bound, master_mip_gap = solve_master(model, solver_cfg, run_dir, it)
        global_ub = min(global_ub, master_bound)
        term = str(res.solver.termination_condition).lower()
        if not ("optimal" in term or "time" in term):
            raise RuntimeError(f"Master failed: {res.solver.status} {res.solver.termination_condition}")
        interface = extract_interface(model, data)
        master_obj = float(pyo.value(model.obj))
        theta_total = sum(interface["theta"].values())
        true_type_cost = 0.0
        cuts_added = 0
        max_viol = 0.0
        cut_candidates = []
        iter_flows = []
        bad_slots = 0
        for mon in data["MONTHS"]:
            for t in data["INTERVALS"]:
                outg = sum(interface["G"].get((int(i), int(j), mon, int(t)), 0.0) for (i, j, m2, t2) in data["allowed_st"] if m2 == mon and int(t2) == int(t))
                if outg <= 1e-8:
                    sp_rows.append({"iteration": it, "Month": mon, "TimeIndex": int(t), "objective_SEK": 0.0, "theta_SEK": interface["theta"].get((mon, int(t)), 0.0), "violation_SEK": 0.0, "positive_rows": 0, "n_arcs": 0, "n_vars": 0, "status": "ok", "termination": "empty_zero_redirection"})
                    continue
                sp = solve_type_assignment_lp(
                    data, solver_cfg, mon, int(t), interface,
                    run_dir=run_dir, iteration=it, tol=1e-8,
                    cut_strategy=cut_strategy, core_interface=core_interface,
                    pareto_tolerance=float(getattr(args, "pareto_tolerance", 1e-7)),
                )
                sp_rows.append({"iteration": it, "Month": mon, "TimeIndex": int(t), "objective_SEK": sp.objective, "theta_SEK": sp.theta, "violation_SEK": sp.violation, "dual_rhs_current_SEK": sp.dual_rhs_current, "dual_selection": sp.dual_selection, "positive_rows": len(sp.flows), "n_arcs": sp.n_arcs, "n_vars": sp.n_vars, "status": sp.status, "termination": sp.termination})
                if not math.isfinite(sp.objective):
                    bad_slots += 1
                    continue
                true_type_cost += sp.objective
                iter_flows.extend(sp.flows)
                if sp.violation > cut_tol:
                    max_viol = max(max_viol, sp.violation)
                    cut_candidates.append(sp)
        selected_cuts = select_cut_candidates(cut_candidates, getattr(args, "max_cuts_per_iteration", None), cut_tol)
        for sp in selected_cuts:
            nz = add_type_assignment_cut(model, sp)
            cuts_added += 1
            cut_rows.append({
                "iteration": it,
                "Month": sp.mon,
                "TimeIndex": int(sp.t),
                "cut_type": "type_assignment_LP_dual_optimality",
                "selection_rule": cut_strategy,
                "dual_selection": sp.dual_selection,
                "rhs_at_current_SEK": sp.dual_rhs_current,
                "true_objective_SEK": sp.objective,
                "theta_at_current_SEK": sp.theta,
                "violation_SEK": sp.violation,
                "nonzeros": nz,
                "n_arcs": sp.n_arcs,
                "n_vars": sp.n_vars,
                "termination": sp.termination,
            })
        certified = master_obj + theta_total - true_type_cost if bad_slots == 0 else -float("inf")
        if certified > best_lb:
            best_lb = certified
            best_rows = list(iter_flows)
            best_snapshot = snapshot_vars(model)
        gap = finite_gap(global_ub, best_lb)
        row = {
            "iteration": it, "method": "LBBD",
            "master_incumbent_SEK": master_incumbent,
            "master_best_bound_UB_SEK": master_bound,
            "global_best_UB_SEK": global_ub,
            "master_reported_mip_gap": master_mip_gap,
            "theta_master_SEK": theta_total,
            "true_type_assignment_cost_SEK": true_type_cost,
            "certified_LB_candidate_SEK": certified,
            "best_LB_SEK": best_lb,
            "LBBD_gap": gap,
            "cuts_added": cuts_added,
            "cut_candidates": len(cut_candidates),
            "bad_slots": bad_slots,
            "max_theta_violation_SEK": max_viol,
            "positive_type_rows": len(iter_flows)
        }
        history.append(row)
        print(f"Iteration {it}: incumbent={master_incumbent:,.3f}, boundUB={master_bound:,.3f}, globalUB={global_ub:,.3f}, certified={certified:,.3f}, bestLB={best_lb:,.3f}, LBBDgap={100*gap:.6f}%, type_cost={true_type_cost:,.3f}, theta={theta_total:,.3f}, cuts={cuts_added}, candidates={len(cut_candidates)}, bad_slots={bad_slots}, strategy={cut_strategy}")
        if cut_strategy == "corepoint":
            core_interface = update_core_interface(core_interface, interface, float(getattr(args, "core_weight", 0.35)), float(getattr(args, "core_floor_kwh", 0.0)))
        if bad_slots == 0 and gap <= float(args.lbbd_gap):
            converged = True
            break
    hist = pd.DataFrame(history)
    sp = pd.DataFrame(sp_rows)
    cuts = pd.DataFrame(cut_rows)
    hist.to_csv(run_dir / "iterations" / "lbbd_iteration_history.csv", index=False)
    sp.to_csv(run_dir / "iterations" / "type_assignment_subproblem_summary.csv", index=False)
    cuts.to_csv(run_dir / "iterations" / "type_assignment_cuts.csv", index=False)
    if best_snapshot is not None:
        restore_vars(model, best_snapshot)
    return {"converged": converged, "history": hist, "sp": sp, "cuts": cuts, "best_rows": best_rows, "best_lb": best_lb, "best_snapshot_restored": best_snapshot is not None}


def main():
    args = parse_args()
    root = Path(args.project_root).resolve()
    paths, cfg, solver_cfg = load_configs(root, args.dataset)
    if args.threads is not None:
        solver_cfg["threads"] = int(args.threads)
    if args.time_limit is not None:
        solver_cfg["time_limit_seconds"] = int(args.time_limit)
    solver_cfg["mip_gap"] = float(args.master_gap)
    run_dir = make_run_dir(paths, args.dataset, args.scenario, args.disable_pv, args.disable_bess, args.cut_strategy)
    transcript = run_dir / "README_RUN.txt"
    with transcript.open("w", encoding="utf-8", errors="replace") as log_file, redirect_stdout(TeeStream(sys.__stdout__, log_file)), redirect_stderr(TeeStream(sys.__stderr__, log_file)):
        print("========== LBBD TERMINAL LOG ==========")
        print(f"Project root : {root}")
        print(f"Dataset      : {args.dataset}")
        print(f"Scenario     : {args.scenario}")
        print(f"Cut strategy : {args.cut_strategy}")
        print(f"Run folder   : {run_dir}")
        print("=======================================")
        raw = load_inputs(paths)
        data = preprocess(raw, cfg)
        data["dataset"] = args.dataset
        data["disable_pv"] = bool(args.disable_pv)
        data["disable_bess"] = bool(args.disable_bess)
        print(f"Hex cells    : {len(data['hex_ids'])}")
        print(f"Arc-slots    : {len(data['allowed_st']):,}")
        print("Building LBBD master...")
        model = build_lbbd_master(data, cfg, scenario=args.scenario)
        if args.hard_no_slack:
            print("Hard no-slack mode: fixing slack to zero.")
            apply_hard_no_slack(model)
        if args.write_lp:
            lp = run_dir / "model" / "lbbd_master.lp"
            model.write(str(lp), io_options={"symbolic_solver_labels": True})
            print(f"LP written to: {lp}")
        manifest = {
            "dataset": args.dataset,
            "scenario": args.scenario,
            "method": "LBBD",
            "master_gap": args.master_gap,
            "subproblem_gap": args.subproblem_gap,
            "lbbd_gap": args.lbbd_gap,
            "max_iterations": args.max_iterations,
            "cut_strategy": args.cut_strategy,
            "max_cuts_per_iteration": args.max_cuts_per_iteration,
            "min_cut_violation": args.min_cut_violation,
            "core_weight": args.core_weight,
            "core_floor_kwh": args.core_floor_kwh,
            "pareto_tolerance": args.pareto_tolerance,
            "note": "Final LBBD implementation. Redirection type-pair assignment is solved by slot-wise LP recourse and represented through Benders optimality cuts."
        }
        (run_dir / "logs" / "lbbd_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        if args.scenario == "with_redirection":
            out = run_lbbd_loop(model, data, cfg, solver_cfg, run_dir, args, stage_label="lbbd")
            print_summary(model, data, cfg)
            export_all(model, data, cfg, run_dir, type_rows=out["best_rows"], history=out["history"], sp_summary=out["sp"], cut_records=out["cuts"], certified_lb=out["best_lb"])
            print(f"LBBD status: {'converged' if out['converged'] else 'stopped'}; best certified incumbent restored={out['best_snapshot_restored']}; best LB={out['best_lb']:,.3f} SEK")
        else:
            print("Solving no-redirection master with Gurobi...")
            res = solve_model(model, solver_cfg, run_dir)
            print(res.solver)
            term = str(res.solver.termination_condition).lower()
            if "infeasible" in term:
                print("Model infeasible. Inspect solver log and slack/hard-no-slack settings.")
                return 2
            print_summary(model, data, cfg)
            export_all(model, data, cfg, run_dir)
            obj_val = pyo.value(model.obj)
            rows = [{"iteration": 1, "method": "LBBD_no_redirection_validation", "master_obj_SEK": obj_val, "best_LB_SEK": obj_val, "global_best_UB_SEK": obj_val, "LBBD_gap": 0.0, "cuts_added": 0, "bad_slots": 0, "note": "No-redirection validation: redirection variables fixed to zero"}]
            pd.DataFrame(rows).to_csv(run_dir / "iterations" / "lbbd_iteration_history.csv", index=False)
        print(f"Run finished successfully. Run directory: {run_dir}")
        print(f"Terminal transcript written to: {transcript}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
