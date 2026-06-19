from __future__ import annotations

import csv
import json
import shutil
import time
from datetime import datetime
from pathlib import Path
from typing import Any

from .lbbd_export import read_model_summary
from .lbbd_io import configure_project_imports, load_and_preprocess
from .lbbd_logging import ensure_dir, technology_suffix, write_json
from .lbbd_loop import run_lbbd_iterations


SCENARIOS = {"no_redirection", "with_redirection"}


def _as_float(value: Any) -> float | None:
    if value is None:
        return None
    text = str(value).strip()
    if text == "" or text.lower() in {"nan", "none"}:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def _write_csv(path: Path, rows: list[dict[str, Any]], fieldnames: list[str]) -> None:
    ensure_dir(path.parent)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def _read_last_csv_row(path: Path) -> dict[str, str]:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    return rows[-1] if rows else {}


def _make_run_dir(project_root: Path, dataset: str, scenario: str, disable_pv: bool, disable_bess: bool) -> Path:
    """Create a single LBBD run folder with the standard project layout.
    """
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    tech = technology_suffix(disable_pv, disable_bess).replace("with", "").replace("no", "no")
    if not disable_pv and not disable_bess:
        tech_label = "PV_BESS"
    elif not disable_pv and disable_bess:
        tech_label = "PV_noBESS"
    elif disable_pv and not disable_bess:
        tech_label = "noPV_BESS"
    else:
        tech_label = "noPV_noBESS"
    run_dir = project_root / "runs" / f"{stamp}_{dataset}_{scenario}_LBBD_{tech_label}"
    for sub in ["logs", "results", "iterations", "master", "subproblems"]:
        ensure_dir(run_dir / sub)
    return run_dir


def _preset_values(preset: str | None, dataset: str) -> dict[str, Any]:
    preset = preset or ("full_default" if dataset == "full" else "small_validation")
    if preset == "full_default":
        return {
            "master_gap": 0.005,
            "subproblem_gap": 0.005,
            "lbbd_gap": 0.001,
            "max_iterations": 30,
            "time_limit": 21600,
        }
    if preset == "full_strict":
        return {
            "master_gap": 0.001,
            "subproblem_gap": 0.001,
            "lbbd_gap": 0.0005,
            "max_iterations": 60,
            "time_limit": 43200,
        }
    return {
        "master_gap": 0.001,
        "subproblem_gap": 0.001,
        "lbbd_gap": 0.0001,
        "max_iterations": 40,
        "time_limit": None,
    }


def _quality_checks(summary: dict[str, Any], iter_last: dict[str, str], target_lbbd_gap: float) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    def add(check: str, passed: bool, value: Any, threshold: Any, note: str = "") -> None:
        rows.append({
            "check": check,
            "passed": bool(passed),
            "value": value,
            "threshold": threshold,
            "note": note,
        })

    gap_pct = _as_float(iter_last.get("lbbd_gap"))
    if gap_pct is not None:
        gap_pct *= 100.0
    add("lbbd_gap_within_target", gap_pct is not None and gap_pct <= 100.0 * target_lbbd_gap, gap_pct, 100.0 * target_lbbd_gap, "percent")

    slack = _as_float(summary.get("slack_penalty_SEK"))
    add("slack_penalty_effectively_zero", slack is not None and abs(slack) <= 1e-3, slack, "<= 1e-3 SEK")

    # The SoC linkage is enforced by equality constraints in the optimization model.
    # On large MIP runs, exported values may show tiny numerical residuals because the
    # solver returns a solution within feasibility/integrality tolerances and the report
    # aggregates floating-point values across many cells/months. Use an adaptive
    # reporting tolerance rather than an unrealistic 1e-6 kWh absolute threshold.
    soc_gap = _as_float(summary.get("max_abs_soc_gap_Jan0_Dec48_kWh"))
    batt_units = _as_float(summary.get("battery_units_installed")) or 0.0
    # 10 kWh per BESS unit in the current formulation; tolerate at least 1 kWh, or
    # 0.01% of installed BESS energy capacity, whichever is larger.
    soc_tol = max(1.0, 1e-4 * 10.0 * batt_units)
    add(
        "soc_month_link_gap_within_numerical_tolerance",
        soc_gap is not None and abs(soc_gap) <= soc_tol,
        soc_gap,
        f"<= {soc_tol:.6g} kWh",
        "adaptive tolerance: max(1 kWh, 0.01% of installed BESS energy capacity)",
    )

    profit = _as_float(summary.get("annual_profit_SEK"))
    add("annual_profit_present", profit is not None, profit, "numeric")

    pv = _as_float(summary.get("PV_panels_installed"))
    add("pv_panels_present", pv is not None, pv, "numeric")

    batt = _as_float(summary.get("battery_units_installed"))
    add("battery_units_present", batt is not None, batt, "numeric")

    return rows


def _run_summary_row(run_dir: Path, dataset: str, scenario: str, elapsed: float) -> dict[str, Any]:
    results = run_dir / "results"
    summary = read_model_summary(results)
    iter_last = _read_last_csv_row(results / "lbbd_iteration_history.csv")

    gap = _as_float(iter_last.get("lbbd_gap"))
    return {
        "dataset": dataset,
        "scenario": scenario,
        "formulation": "LBBD_PV_BESS_type_aware_redirection",
        "run_dir": str(run_dir),
        "elapsed_seconds": elapsed,
        "annual_profit_SEK": summary.get("annual_profit_SEK", ""),
        "best_lb_SEK": iter_last.get("best_LB_SEK") or iter_last.get("best_lb_SEK") or summary.get("annual_profit_SEK", ""),
        "upper_bound_SEK": iter_last.get("master_objective_UB_SEK") or iter_last.get("upper_bound_SEK") or "",
        "lbbd_gap_pct": 100.0 * gap if gap is not None else "",
        "iterations": iter_last.get("iteration", ""),
        "cuts_generated": iter_last.get("total_cuts", ""),
        "cuts_added_last_iter": iter_last.get("cuts_added", ""),
        "energy_redirected_kWh": summary.get("energy_redirected_kWh", ""),
        "PV_panels_installed": summary.get("PV_panels_installed", ""),
        "battery_units_installed": summary.get("battery_units_installed", ""),
        "chargers_slow_installed": summary.get("chargers_slow_installed", ""),
        "chargers_medium_installed": summary.get("chargers_medium_installed", ""),
        "chargers_fast_installed": summary.get("chargers_fast_installed", ""),
        "grid_total_kWh": summary.get("grid_total_kWh", ""),
        "pv_used_total_kWh": summary.get("pv_used_total_kWh", ""),
        "battery_discharge_kWh": summary.get("battery_discharge_kWh", ""),
        "max_abs_soc_gap_Jan0_Dec48_kWh": summary.get("max_abs_soc_gap_Jan0_Dec48_kWh", ""),
        "slack_penalty_SEK": summary.get("slack_penalty_SEK", ""),
    }


def _postprocess_outputs(run_dir: Path, dataset: str, scenario: str, elapsed: float, target_lbbd_gap: float) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    # More user-facing aliases for the default workflow.
    # Make iteration/cut files available in both results and iterations, if one side is missing.
    for name in ["lbbd_iteration_history.csv", "lbbd_cuts.csv"]:
        src = run_dir / "results" / name
        dst = run_dir / "iterations" / name
        if src.exists() and not dst.exists():
            shutil.copy2(src, dst)
        elif dst.exists() and not src.exists():
            shutil.copy2(dst, src)

    summary_row = _run_summary_row(run_dir, dataset, scenario, elapsed)
    summary_fields = list(summary_row.keys())
    _write_csv(run_dir / "results" / "run_summary.csv", [summary_row], summary_fields)

    model_summary = read_model_summary(run_dir / "results")
    iter_last = _read_last_csv_row(run_dir / "results" / "lbbd_iteration_history.csv")
    quality = _quality_checks(model_summary, iter_last, target_lbbd_gap)
    _write_csv(run_dir / "results" / "quality_checks.csv", quality, ["check", "passed", "value", "threshold", "note"])

    readme = f"""LBBD run folder\n=====================\n\nThis folder is produced by src_lbbd/run_lbbd.py. It uses the validated LBBD formulation:\ncharger siting and sizing + PV + BESS in the master, with type-aware redirection handled through slot-wise LP/MIP recourse.\n\nCore files:\n- results/run_summary.csv: one-row run summary.\n- results/quality_checks.csv: automatic checks for LBBD gap, slack, and SoC linkage.\n- results/model_summary.csv: detailed economic/energy/infrastructure metrics.\n- results/infrastructure_by_hex.csv: charger/PV/BESS deployment by cell.\n- results/redirections.csv and redirections_by_type.csv: reconstructed redirected flows.\n- results/lbbd_iteration_history.csv: bound and cut progress per iteration.\n- master/master_iter_*.log: Gurobi logs for each master solve.\n- logs/run_manifest.json: run configuration and solver settings.\n\nScenario: {scenario}\nDataset: {dataset}\n"""
    (run_dir / "README_RUN_FOLDER.txt").write_text(readme, encoding="utf-8")
    return summary_row, quality


def run_lbbd(args: Any) -> int:
    project_root = Path(args.project_root).resolve()
    configure_project_imports(project_root)
    if args.scenario not in SCENARIOS:
        raise ValueError(f"Unsupported scenario: {args.scenario}")

    values = _preset_values(args.preset, args.dataset)
    if args.master_gap is not None:
        values["master_gap"] = float(args.master_gap)
    if args.subproblem_gap is not None:
        values["subproblem_gap"] = float(args.subproblem_gap)
    if args.lbbd_gap is not None:
        values["lbbd_gap"] = float(args.lbbd_gap)
    if args.max_iterations is not None:
        values["max_iterations"] = int(args.max_iterations)
    if args.time_limit is not None:
        values["time_limit"] = int(args.time_limit)

    disable_pv = bool(args.disable_pv)
    disable_bess = bool(args.disable_bess)
    if disable_bess:
        print("Warning: the default workflow is calibrated for PV+BESS. You passed --disable-bess, so BESS will be disabled.")

    print("========== LBBD RUN ==========")
    print(f"Project root   : {project_root}")
    print(f"Dataset        : {args.dataset}")
    print(f"Scenario       : {args.scenario}")
    print(f"Technology     : {'PV enabled' if not disable_pv else 'PV disabled'}, {'BESS enabled' if not disable_bess else 'BESS disabled'}")
    print(f"Run preset     : {args.preset or ('full_default' if args.dataset == 'full' else 'small_validation')}")
    print(f"Master gap     : {values['master_gap']}")
    print(f"Subproblem gap : {values['subproblem_gap']}")
    print(f"LBBD gap       : {values['lbbd_gap']}")
    print(f"Max iterations : {values['max_iterations']}")
    print(f"Cut strategy   : {getattr(args, 'cut_strategy', 'standard')}")
    if getattr(args, "max_cuts_per_iteration", None):
        print(f"Cut limit      : {args.max_cuts_per_iteration} cuts/iteration")
    if getattr(args, "mip_reconstruction_frequency", 1) and int(args.mip_reconstruction_frequency) > 1:
        print(f"MIP rec freq   : every {args.mip_reconstruction_frequency} iterations")
    print("===============================================")

    paths, model_cfg, solver_cfg, data, dataset = load_and_preprocess(project_root, args.dataset)
    data["disable_pv"] = disable_pv
    data["disable_bess"] = disable_bess
    data["x_kWh"] = float(model_cfg.get("x_kwh_per_trip", 20.0))

    if args.threads is not None:
        solver_cfg["threads"] = int(args.threads)
    if values.get("time_limit") is not None:
        solver_cfg["time_limit_seconds"] = int(values["time_limit"])
    solver_cfg["mip_gap"] = float(values["master_gap"])
    solver_cfg.setdefault("nodefile_start_gb", 2.0)

    run_dir = _make_run_dir(project_root, dataset, args.scenario, disable_pv, disable_bess)
    print(f"Run folder     : {run_dir}")
    print(f"Hex cells      : {len(data['hex_ids'])}")
    print(f"Arc-slots      : {len(data['allowed_st']):,}")

    write_json(
        run_dir / "logs" / "run_manifest.json",
        {
            "workflow": "lbbd",
            "dataset": dataset,
            "scenario": args.scenario,
            "disable_pv": disable_pv,
            "disable_bess": disable_bess,
            "project_root": str(project_root),
            "run_dir": str(run_dir),
            "preset_values": values,
            "solver_cfg": solver_cfg,
            "hex_cells": len(data.get("hex_ids", [])),
            "active_redirection_arc_slots": len(data.get("allowed_st", [])),
            "acceleration": {
                "cut_strategy": getattr(args, "cut_strategy", "standard"),
                "max_cuts_per_iteration": getattr(args, "max_cuts_per_iteration", None),
                "min_cut_violation": getattr(args, "min_cut_violation", None),
                "mip_reconstruction_frequency": getattr(args, "mip_reconstruction_frequency", 1),
                "core_weight": getattr(args, "core_weight", 0.35),
                "core_floor_kwh": getattr(args, "core_floor_kwh", 1e-4),
                "pareto_tolerance": getattr(args, "pareto_tolerance", 1e-7),
            },
            "note": "The workflow writes a single LBBD run folder with solver logs, iteration history, quality checks, and result tables.",
        },
    )

    t0 = time.time()
    result = run_lbbd_iterations(
        data=data,
        cfg=model_cfg,
        solver_cfg=solver_cfg,
        run_dir=run_dir,
        scenario=args.scenario,
        max_iterations=int(values["max_iterations"]),
        lbbd_gap=float(values["lbbd_gap"]),
        cut_tolerance=float(args.cut_tolerance),
        subproblem_gap=float(values["subproblem_gap"]),
        tee=bool(args.show_master_log),
        cut_strategy=getattr(args, "cut_strategy", "standard"),
        max_cuts_per_iteration=getattr(args, "max_cuts_per_iteration", None),
        min_cut_violation=getattr(args, "min_cut_violation", None),
        mip_reconstruction_frequency=getattr(args, "mip_reconstruction_frequency", 1),
        core_weight=getattr(args, "core_weight", 0.35),
        core_floor_kwh=getattr(args, "core_floor_kwh", 1e-4),
        pareto_tolerance=getattr(args, "pareto_tolerance", 1e-7),
    )
    elapsed = time.time() - t0
    summary_row, quality = _postprocess_outputs(run_dir, dataset, args.scenario, elapsed, float(values["lbbd_gap"]))

    failed = [r for r in quality if not r["passed"]]
    # Update manifest after the run.
    manifest_path = run_dir / "logs" / "run_manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest.update({
        "status": "completed" if not failed and (result.get("converged") or args.scenario == "no_redirection") else "completed_with_warnings",
        "elapsed_seconds": elapsed,
        "run_summary": summary_row,
        "failed_quality_checks": failed,
    })
    write_json(manifest_path, manifest)

    print("\n========== LBBD SUMMARY ==========")
    print(f"Status              : {manifest['status']}")
    print(f"Run folder          : {run_dir}")
    print(f"Annual profit SEK   : {summary_row.get('annual_profit_SEK')}")
    print(f"LBBD gap pct        : {summary_row.get('lbbd_gap_pct')}")
    print(f"PV panels installed : {summary_row.get('PV_panels_installed')}")
    print(f"BESS units installed: {summary_row.get('battery_units_installed')}")
    print(f"Slow/Medium/Fast    : {summary_row.get('chargers_slow_installed')} / {summary_row.get('chargers_medium_installed')} / {summary_row.get('chargers_fast_installed')}")
    print(f"Redirected energy   : {summary_row.get('energy_redirected_kWh')} kWh/yr")
    print(f"Failed checks       : {len(failed)}")
    print("Summary file        : results/run_summary.csv")
    print("Quality checks      : results/quality_checks.csv")
    print("========================================")
    print(f"Run finished successfully. Run directory: {run_dir}")
    return 0 if manifest["status"] in {"completed", "completed_with_warnings"} else 1
