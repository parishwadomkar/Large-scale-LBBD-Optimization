from __future__ import annotations

import time
from pathlib import Path
from typing import Any

import pandas as pd
import pyomo.environ as pyo

from .lbbd_master_stage4 import (
    add_stage4_dual_cut,
    build_stage4_master,
    evaluate_stage4_base_objective,
    extract_stage4_interface,
)
from .lbbd_subproblem_redirection import (
    solve_redirection_dual_lp,
    solve_redirection_primal_mip,
)
from .lbbd_export_stage4 import export_stage4_all, sv


def _make_solver(solver_cfg: dict, run_dir: Path, iteration: int, tee: bool = True):
    solver = pyo.SolverFactory("gurobi")
    opts = solver.options
    if solver_cfg.get("threads") is not None:
        opts["Threads"] = int(solver_cfg["threads"])
    if solver_cfg.get("mip_gap") is not None:
        opts["MIPGap"] = float(solver_cfg["mip_gap"])
    if solver_cfg.get("time_limit_seconds") is not None:
        opts["TimeLimit"] = int(solver_cfg["time_limit_seconds"])
    if solver_cfg.get("presolve") is not None:
        opts["Presolve"] = int(solver_cfg["presolve"])
    if solver_cfg.get("numeric_focus") is not None:
        opts["NumericFocus"] = int(solver_cfg["numeric_focus"])
    if solver_cfg.get("heuristics") is not None:
        opts["Heuristics"] = float(solver_cfg["heuristics"])
    if solver_cfg.get("cuts") is not None:
        opts["Cuts"] = int(solver_cfg["cuts"])
    if solver_cfg.get("mip_focus") is not None:
        opts["MIPFocus"] = int(solver_cfg["mip_focus"])
    opts["LogFile"] = str((run_dir / "master" / f"master_iter_{iteration:03d}.log")).replace("\\", "/")
    return solver


def _solve_master(model, solver_cfg: dict, run_dir: Path, iteration: int, tee: bool = True) -> tuple[str, str, float]:
    solver = _make_solver(solver_cfg, run_dir, iteration, tee=tee)
    t0 = time.time()
    res = solver.solve(model, tee=tee)
    elapsed = time.time() - t0
    status = str(res.solver.status).lower()
    term = str(res.solver.termination_condition).lower()
    if not ("optimal" in term or "maxtimelimit" in term or "time" in term):
        raise RuntimeError(f"Master solve failed at iteration {iteration}. status={status}, termination={term}")
    return status, term, elapsed


def _all_slots(data: dict) -> list[tuple[str, int]]:
    return [(mon, int(t)) for mon in data["MONTHS"] for t in data["INTERVALS"]]


def _relative_gap(ub: float, lb: float) -> float:
    if ub == float("inf") or lb == -float("inf"):
        return float("inf")
    return max(0.0, ub - lb) / max(1.0, abs(lb))


def _subproblem_solver_cfg(solver_cfg: dict, subproblem_gap: float | None = None) -> dict:
    cfg = dict(solver_cfg)
    cfg["time_limit_seconds"] = max(30, min(int(cfg.get("time_limit_seconds", 6600)), 300))
    if subproblem_gap is not None:
        cfg["mip_gap"] = float(subproblem_gap)
    cfg["threads"] = max(1, min(int(cfg.get("threads", 1) or 1), 2))
    return cfg


def run_stage4_lbbd(
    data: dict,
    cfg: dict,
    solver_cfg: dict,
    run_dir: Path,
    scenario: str,
    max_iterations: int = 30,
    lbbd_gap: float = 1e-4,
    cut_tolerance: float = 1e-5,
    subproblem_gap: float | None = None,
    tee: bool = True,
) -> dict[str, Any]:
    """PV+BESS master with continuous LP Benders cuts and
    MIP trip-bundle redirection reconstruction.

    PV and BESS are placed in the master. BESS is not split by slot because SoC is temporally
    coupled across the 12 linked representative month-days. Redirection remains decomposed by
    month-time slots.
    """
    if scenario == "no_redirection":
        max_iterations = 1
    print("Building PV+BESS master model...")
    model = build_stage4_master(data, cfg, scenario=scenario)

    best_lb = -float("inf")
    best_iter = None
    history: list[dict[str, Any]] = []
    sp_records: list[dict[str, Any]] = []
    cut_records: list[dict[str, Any]] = []
    final_interface: dict[str, dict] | None = None
    best_mip_rows: list[dict[str, Any]] = []
    converged = False
    start = time.time()
    sp_cfg = _subproblem_solver_cfg(solver_cfg, subproblem_gap=subproblem_gap)

    for iteration in range(1, max_iterations + 1):
        print(f"\n========== LBBD ITERATION {iteration} ==========")
        status, term, master_elapsed = _solve_master(model, solver_cfg, run_dir, iteration, tee=tee)
        master_obj = sv(model.obj)
        base_obj = evaluate_stage4_base_objective(model)
        interface = extract_stage4_interface(model)
        final_interface = interface

        lp_value_sum = 0.0
        mip_value_sum = 0.0
        cuts_added = 0
        max_violation = 0.0
        n_subproblems = 0
        n_positive_type_arcs = 0
        n_mip_positive_rows = 0
        iter_mip_rows: list[dict[str, Any]] = []

        if scenario == "with_redirection":
            for mon, t in _all_slots(data):
                dual_res = solve_redirection_dual_lp(
                    data=data,
                    cfg=cfg,
                    solver_cfg=sp_cfg,
                    mon=mon,
                    t=t,
                    R_values=interface["R"],
                    S_values=interface["S"],
                    log_dir=None,
                )
                n_subproblems += 1
                n_positive_type_arcs += dual_res.n_positive_type_arcs
                lp_value_sum += dual_res.objective
                theta_val = interface["theta"][(mon, t)]
                violation = theta_val - dual_res.objective
                max_violation = max(max_violation, violation)
                if violation > cut_tolerance:
                    nz = add_stage4_dual_cut(model, mon, t, dual_res.alpha, dual_res.beta)
                    cuts_added += 1
                    cut_records.append({
                        "iteration": iteration,
                        "Month": mon,
                        "TimeIndex": t,
                        "cut_type": "exact_lp_dual_upper_cut",
                        "rhs_at_current_SEK": dual_res.objective,
                        "theta_at_current_SEK": theta_val,
                        "violation_SEK": violation,
                        "nonzeros": nz,
                        "exactness": "exact_for_continuous_redirection_LP_restricted_model",
                    })

                mip_res = solve_redirection_primal_mip(
                    data=data,
                    cfg=cfg,
                    solver_cfg=sp_cfg,
                    mon=mon,
                    t=t,
                    R_values=interface["R"],
                    S_values=interface["S"],
                    log_dir=None,
                )
                mip_value_sum += mip_res.objective
                n_mip_positive_rows += len(mip_res.flows)
                iter_mip_rows.extend(mip_res.flows)
                sp_records.append({
                    "iteration": iteration,
                    "Month": mon,
                    "TimeIndex": t,
                    "subproblem_type": "pv_bess_master_mip_trip_bundle_redirection_with_lp_dual_bound",
                    "lp_relaxation_objective_SEK": dual_res.objective,
                    "mip_objective_SEK": mip_res.objective,
                    "theta_master_SEK": theta_val,
                    "lp_violation_SEK": violation,
                    "lp_mip_recourse_gap_SEK": max(0.0, dual_res.objective - mip_res.objective),
                    "positive_type_arcs": dual_res.n_positive_type_arcs,
                    "mip_positive_rows": len(mip_res.flows),
                    "dual_status": dual_res.status,
                    "dual_termination": dual_res.termination,
                    "mip_status": mip_res.status,
                    "mip_termination": mip_res.termination,
                })
        else:
            lp_value_sum = 0.0
            mip_value_sum = 0.0

        lb_candidate = base_obj + mip_value_sum
        if lb_candidate > best_lb:
            best_lb = lb_candidate
            best_iter = iteration
            best_mip_rows = list(iter_mip_rows)

        ub = master_obj
        gap = _relative_gap(ub, best_lb)
        row = {
            "stage": 4,
            "iteration": iteration,
            "dataset": data.get("dataset", "unknown"),
            "scenario": scenario,
            "status": "converged" if gap <= lbbd_gap else "running",
            "master_status": status,
            "master_termination": term,
            "master_objective_UB_SEK": ub,
            "base_master_objective_SEK": base_obj,
            "lp_recourse_value_SEK": lp_value_sum,
            "mip_recourse_value_SEK": mip_value_sum,
            "LB_candidate_SEK": lb_candidate,
            "best_LB_SEK": best_lb,
            "best_LB_iteration": best_iter,
            "lbbd_gap": gap,
            "cuts_added": cuts_added,
            "total_cuts": len(cut_records),
            "max_theta_violation_SEK": max_violation,
            "n_subproblems": n_subproblems,
            "n_positive_type_arcs": n_positive_type_arcs,
            "n_mip_positive_rows": n_mip_positive_rows,
            "PV_panels_installed": sum(sv(model.PV[i]) for i in model.I),
            "battery_units_installed": sum(sv(model.Batt[i]) for i in model.I),
            "pv_direct_kWh": sum(data["N_MONTH"][mon] * sv(model.pv_dir[i, mon, t]) for i in model.I for mon in model.M for t in model.H),
            "pv_to_battery_kWh": sum(data["N_MONTH"][mon] * sv(model.pv_batt[i, mon, t]) for i in model.I for mon in model.M for t in model.H),
            "grid_to_battery_kWh": sum(data["N_MONTH"][mon] * sv(model.grid_batt[i, mon, t]) for i in model.I for mon in model.M for t in model.H),
            "battery_discharge_kWh": sum(data["N_MONTH"][mon] * sv(model.batt_discharge[i, mon, t]) for i in model.I for mon in model.M for t in model.H),
            "master_elapsed_seconds": master_elapsed,
            "elapsed_seconds": time.time() - start,
        }
        history.append(row)
        print(
            f"Iteration {iteration}: UB={ub:,.3f}, MIP-LB={best_lb:,.3f}, "
            f"gap={100.0 * gap:.6f}%, LP_rec={lp_value_sum:,.3f}, MIP_rec={mip_value_sum:,.3f}, "
            f"PV={row['PV_panels_installed']:,.0f}, Batt={row['battery_units_installed']:,.0f}, cuts_added={cuts_added}, max_violation={max_violation:,.6f}"
        )

        if scenario == "no_redirection" or (gap <= lbbd_gap):
            converged = True
            history[-1]["status"] = "converged"
            break

    history_df = pd.DataFrame(history)
    sp_df = pd.DataFrame(sp_records)
    cuts_df = pd.DataFrame(cut_records)
    export_stage4_all(model, data, cfg, run_dir, best_mip_rows, history_df, sp_df, cuts_df)

    final_ub = history[-1]["master_objective_UB_SEK"] if history else float("nan")
    final_gap = history[-1]["lbbd_gap"] if history else float("nan")
    print("\n========== LBBD SUMMARY ==========")
    print(f"Status                : {'converged' if converged else 'stopped'}")
    print(f"Iterations            : {len(history)}")
    print(f"Best MIP-LB SEK       : {best_lb:,.3f}")
    print(f"Final LP-UB SEK       : {final_ub:,.3f}")
    print(f"Final LBBD gap        : {100.0 * final_gap:.6f}%")
    print(f"Cuts generated        : {len(cut_records)}")
    print(f"MIP redirection rows  : {len(best_mip_rows)}")
    print(f"PV panels installed   : {sum(sv(model.PV[i]) for i in model.I):,.0f}")
    print(f"BESS units installed  : {sum(sv(model.Batt[i]) for i in model.I):,.0f}")
    print(f"Run folder            : {run_dir}")
    print("==========================================")
    return {
        "converged": converged,
        "history": history_df,
        "subproblems": sp_df,
        "cuts": cuts_df,
        "best_lb": best_lb,
        "final_ub": final_ub,
        "final_gap": final_gap,
        "interface": final_interface,
    }
