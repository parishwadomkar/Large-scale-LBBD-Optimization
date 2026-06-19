from __future__ import annotations

import math
import time
from pathlib import Path
from typing import Any

import pandas as pd
import pyomo.environ as pyo

from .lbbd_master import (
    add_dual_cut,
    build_master_model,
    evaluate_base_objective,
    extract_interface,
)
from .lbbd_subproblem_redirection import (
    solve_redirection_dual_lp,
    solve_redirection_primal_mip,
)
from .lbbd_export_results import export_lbbd_results, sv


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
    if ub == float("inf") or lb == -float("inf") or math.isnan(ub) or math.isnan(lb):
        return float("inf")
    return max(0.0, ub - lb) / max(1.0, abs(lb))


def _subproblem_solver_cfg(solver_cfg: dict, subproblem_gap: float | None = None) -> dict:
    cfg = dict(solver_cfg)
    cfg["time_limit_seconds"] = max(30, min(int(cfg.get("time_limit_seconds", 6600)), 300))
    if subproblem_gap is not None:
        cfg["mip_gap"] = float(subproblem_gap)
    cfg["threads"] = max(1, min(int(cfg.get("threads", 1) or 1), 2))
    return cfg


def _update_core_point(
    core: dict[str, dict] | None,
    interface: dict[str, dict],
    weight: float,
    floor_kwh: float,
) -> dict[str, dict]:
    """Moving-average reference point for Magnanti-Wong/core-point cut selection.

    The core is not used as a feasible solution; it is only a reference RHS used to
    pick a stronger dual solution from the optimal dual face. A small floor avoids
    selecting cuts that ignore cells/types that have been zero so far.
    """
    w = min(1.0, max(0.0, float(weight)))
    floor = max(0.0, float(floor_kwh))
    if core is None:
        return {
            "R": {k: max(floor, float(v)) for k, v in interface["R"].items()},
            "S": {k: max(floor, float(v)) for k, v in interface["S"].items()},
        }
    new_R = {}
    new_S = {}
    for k, v in interface["R"].items():
        new_R[k] = (1.0 - w) * float(core["R"].get(k, floor)) + w * max(floor, float(v))
    for k, v in interface["S"].items():
        new_S[k] = (1.0 - w) * float(core["S"].get(k, floor)) + w * max(floor, float(v))
    return {"R": new_R, "S": new_S}


def _select_cut_candidates(
    candidates: list[dict[str, Any]],
    max_cuts_per_iteration: int | None,
    min_cut_violation: float,
) -> list[dict[str, Any]]:
    pool = [c for c in candidates if float(c["violation"]) > float(min_cut_violation)]
    pool.sort(key=lambda c: float(c["violation"]), reverse=True)
    if max_cuts_per_iteration is not None and int(max_cuts_per_iteration) > 0:
        return pool[: int(max_cuts_per_iteration)]
    return pool


def run_lbbd_iterations(
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
    cut_strategy: str = "standard",
    max_cuts_per_iteration: int | None = None,
    min_cut_violation: float | None = None,
    mip_reconstruction_frequency: int = 1,
    core_weight: float = 0.35,
    core_floor_kwh: float = 1e-4,
    pareto_tolerance: float = 1e-7,
) -> dict[str, Any]:
    """PV+BESS master with redirection LP/MIP recourse.

    Acceleration options:
    - cut_strategy='corepoint' uses a Magnanti-Wong-style auxiliary dual LP.
    - max_cuts_per_iteration limits cut addition to the most violated slots.
    - mip_reconstruction_frequency skips expensive MIP recourse reconstruction in
      non-reporting iterations; this keeps the UB valid and the LB conservative.
    """
    if scenario == "no_redirection":
        max_iterations = 1
    cut_strategy = (cut_strategy or "standard").lower().strip()
    if cut_strategy in {"mw", "pareto", "magnanti_wong"}:
        cut_strategy = "corepoint"
    if cut_strategy not in {"standard", "corepoint"}:
        raise ValueError(f"Unsupported cut_strategy={cut_strategy!r}. Use 'standard' or 'corepoint'.")
    min_cut_violation = cut_tolerance if min_cut_violation is None else float(min_cut_violation)
    mip_reconstruction_frequency = max(1, int(mip_reconstruction_frequency or 1))

    print("Building PV+BESS LBBD master model...")
    if cut_strategy == "corepoint":
        print("Acceleration       : core-point/Pareto dual cut selection enabled")
    if max_cuts_per_iteration:
        print(f"Cut throttling     : at most {max_cuts_per_iteration} most violated cuts per iteration")
    if mip_reconstruction_frequency > 1:
        print(f"MIP reconstruction : every {mip_reconstruction_frequency} iterations, plus the first iteration and near-convergence iterations")

    model = build_master_model(data, cfg, scenario=scenario)

    best_lb = -float("inf")
    best_iter = None
    history: list[dict[str, Any]] = []
    sp_records: list[dict[str, Any]] = []
    cut_records: list[dict[str, Any]] = []
    last_interface: dict[str, dict] | None = None
    best_mip_rows: list[dict[str, Any]] = []
    converged = False
    start = time.time()
    sp_cfg = _subproblem_solver_cfg(solver_cfg, subproblem_gap=subproblem_gap)
    core_point: dict[str, dict] | None = None

    for iteration in range(1, max_iterations + 1):
        print(f"\n========== LBBD ITERATION {iteration} ==========")
        status, term, master_elapsed = _solve_master(model, solver_cfg, run_dir, iteration, tee=tee)
        master_obj = sv(model.obj)
        base_obj = evaluate_base_objective(model)
        interface = extract_interface(model)
        last_interface = interface

        lp_value_sum = 0.0
        mip_value_sum = float("nan")
        cuts_added = 0
        max_violation = 0.0
        n_subproblems = 0
        n_positive_type_arcs = 0
        n_mip_positive_rows = 0
        iter_mip_rows: list[dict[str, Any]] = []
        cut_candidates: list[dict[str, Any]] = []

        # A valid UB is the current master objective.  MIP reconstruction is needed only
        # to update the feasible LB.  It is safe to skip it in selected iterations.
        prelim_gap = _relative_gap(master_obj, best_lb)
        do_mip_reconstruction = (
            scenario == "with_redirection" and (
                iteration == 1
                or iteration == max_iterations
                or iteration % mip_reconstruction_frequency == 0
                or prelim_gap <= max(10.0 * float(lbbd_gap), 0.002)
            )
        )

        if scenario == "with_redirection":
            for mon, t in _all_slots(data):
                use_core = cut_strategy == "corepoint" and core_point is not None
                dual_res = solve_redirection_dual_lp(
                    data=data,
                    cfg=cfg,
                    solver_cfg=sp_cfg,
                    mon=mon,
                    t=t,
                    R_values=interface["R"],
                    S_values=interface["S"],
                    log_dir=None,
                    pareto_core_R_values=core_point["R"] if use_core else None,
                    pareto_core_S_values=core_point["S"] if use_core else None,
                    pareto_tolerance=pareto_tolerance,
                )
                n_subproblems += 1
                n_positive_type_arcs += dual_res.n_positive_type_arcs
                lp_value_sum += dual_res.objective
                theta_val = interface["theta"][(mon, t)]
                violation = theta_val - dual_res.objective
                max_violation = max(max_violation, violation)
                if violation > min_cut_violation:
                    cut_candidates.append({
                        "iteration": iteration,
                        "Month": mon,
                        "TimeIndex": int(t),
                        "alpha": dual_res.alpha,
                        "beta": dual_res.beta,
                        "rhs_at_current_SEK": dual_res.objective,
                        "theta_at_current_SEK": theta_val,
                        "violation": violation,
                        "positive_type_arcs": dual_res.n_positive_type_arcs,
                        "dual_status": dual_res.status,
                        "dual_termination": dual_res.termination,
                    })

                if do_mip_reconstruction:
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
                    if math.isnan(mip_value_sum):
                        mip_value_sum = 0.0
                    mip_value_sum += mip_res.objective
                    n_mip_positive_rows += len(mip_res.flows)
                    iter_mip_rows.extend(mip_res.flows)
                    sp_records.append({
                        "iteration": iteration,
                        "Month": mon,
                        "TimeIndex": int(t),
                        "subproblem_type": "redirection_mip_reconstruction_with_lp_dual_bound",
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
                    sp_records.append({
                        "iteration": iteration,
                        "Month": mon,
                        "TimeIndex": int(t),
                        "subproblem_type": "lp_dual_bound_only_mip_reconstruction_skipped",
                        "lp_relaxation_objective_SEK": dual_res.objective,
                        "mip_objective_SEK": "",
                        "theta_master_SEK": theta_val,
                        "lp_violation_SEK": violation,
                        "lp_mip_recourse_gap_SEK": "",
                        "positive_type_arcs": dual_res.n_positive_type_arcs,
                        "mip_positive_rows": "",
                        "dual_status": dual_res.status,
                        "dual_termination": dual_res.termination,
                        "mip_status": "skipped",
                        "mip_termination": "skipped",
                    })

            selected = _select_cut_candidates(cut_candidates, max_cuts_per_iteration, min_cut_violation)
            for cand in selected:
                nz = add_dual_cut(model, cand["Month"], cand["TimeIndex"], cand["alpha"], cand["beta"])
                cuts_added += 1
                cut_records.append({
                    "iteration": iteration,
                    "Month": cand["Month"],
                    "TimeIndex": cand["TimeIndex"],
                    "cut_type": "corepoint_lp_dual_upper_cut" if cut_strategy == "corepoint" else "exact_lp_dual_upper_cut",
                    "rhs_at_current_SEK": cand["rhs_at_current_SEK"],
                    "theta_at_current_SEK": cand["theta_at_current_SEK"],
                    "violation_SEK": cand["violation"],
                    "nonzeros": nz,
                    "positive_type_arcs": cand["positive_type_arcs"],
                    "dual_termination": cand["dual_termination"],
                    "exactness": "valid_upper_cut_for_continuous_redirection_LP_restricted_model",
                    "selection_rule": f"{cut_strategy}; top={max_cuts_per_iteration or 'all'}; min_violation={min_cut_violation}",
                })

            if cut_strategy == "corepoint":
                core_point = _update_core_point(core_point, interface, core_weight, core_floor_kwh)
        else:
            lp_value_sum = 0.0
            mip_value_sum = 0.0

        if not math.isnan(mip_value_sum):
            lb_candidate = base_obj + mip_value_sum
            if lb_candidate > best_lb:
                best_lb = lb_candidate
                best_iter = iteration
                best_mip_rows = list(iter_mip_rows)
        else:
            lb_candidate = float("nan")

        ub = master_obj
        gap = _relative_gap(ub, best_lb)
        row = {
            "iteration": iteration,
            "dataset": data.get("dataset", "unknown"),
            "scenario": scenario,
            "status": "converged" if gap <= lbbd_gap else "running",
            "master_status": status,
            "master_termination": term,
            "master_objective_UB_SEK": ub,
            "base_master_objective_SEK": base_obj,
            "lp_recourse_value_SEK": lp_value_sum,
            "mip_recourse_value_SEK": mip_value_sum if not math.isnan(mip_value_sum) else "",
            "LB_candidate_SEK": lb_candidate if not math.isnan(lb_candidate) else "",
            "best_LB_SEK": best_lb,
            "best_LB_iteration": best_iter,
            "lbbd_gap": gap,
            "cuts_added": cuts_added,
            "cut_candidates": len(cut_candidates),
            "total_cuts": len(cut_records),
            "max_theta_violation_SEK": max_violation,
            "cut_strategy": cut_strategy,
            "max_cuts_per_iteration": max_cuts_per_iteration or "all",
            "mip_reconstruction_performed": do_mip_reconstruction or scenario == "no_redirection",
            "mip_reconstruction_frequency": mip_reconstruction_frequency,
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
        mip_txt = f"{mip_value_sum:,.3f}" if not math.isnan(mip_value_sum) else "skipped"
        print(
            f"Iteration {iteration}: UB={ub:,.3f}, MIP-LB={best_lb:,.3f}, "
            f"gap={100.0 * gap:.6f}%, LP_rec={lp_value_sum:,.3f}, MIP_rec={mip_txt}, "
            f"PV={row['PV_panels_installed']:,.0f}, Batt={row['battery_units_installed']:,.0f}, "
            f"cuts_added={cuts_added}/{len(cut_candidates)}, max_violation={max_violation:,.6f}, strategy={cut_strategy}"
        )

        if scenario == "no_redirection" or (gap <= lbbd_gap):
            converged = True
            history[-1]["status"] = "converged"
            break

    history_df = pd.DataFrame(history)
    sp_df = pd.DataFrame(sp_records)
    cuts_df = pd.DataFrame(cut_records)
    export_lbbd_results(model, data, cfg, run_dir, best_mip_rows, history_df, sp_df, cuts_df)

    upper_bound = history[-1]["master_objective_UB_SEK"] if history else float("nan")
    bound_gap = history[-1]["lbbd_gap"] if history else float("nan")
    print("\n========== LBBD SOLUTION SUMMARY ==========")
    print(f"Status                : {'converged' if converged else 'stopped'}")
    print(f"Iterations            : {len(history)}")
    print(f"Best MIP-LB SEK       : {best_lb:,.3f}")
    print(f"LP upper bound SEK   : {upper_bound:,.3f}")
    print(f"LBBD gap            : {100.0 * bound_gap:.6f}%")
    print(f"Cuts generated        : {len(cut_records)}")
    print(f"Cut strategy          : {cut_strategy}")
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
        "upper_bound": upper_bound,
        "bound_gap": bound_gap,
        "interface": last_interface,
    }
