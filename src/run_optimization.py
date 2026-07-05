#!/usr/bin/env python
# coding: utf-8
from __future__ import annotations

import argparse
import importlib
import os
import sys
from datetime import datetime
from pathlib import Path

for _stream_name in ("stdout", "stderr"):
    _stream = getattr(sys, _stream_name, None)
    if hasattr(_stream, "reconfigure"):
        try:
            _stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

from utils import ensure_dir, load_json, resolve_project_path
from data_loader import check_input_paths, load_inputs
from preprocessing import preprocess
from model_builder import apply_scenario, apply_hard_no_slack, build_model
from solve_model import solve_model
from export_results import export_all, print_summary

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the type-aware EV CPO optimization from VS Code/terminal."
    )
    parser.add_argument(
        "--scenario",
        choices=["with_redirection", "no_redirection"],
        default="with_redirection",
        help="Optimization scenario."
    )
    parser.add_argument(
        "--dataset",
        choices=["small", "full"],
        default=None,
        help="Input dataset to use from config/paths.json."
    )
    parser.add_argument(
        "--hard-no-slack",
        action="store_true",
        help="Fix all slack variables to zero. Use for feasibility/final no-slack runs."
    )
    parser.add_argument(
        "--smoke",
        action="store_true",
        help="Check environment and input files only."
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=None,
        help="Override Gurobi Threads."
    )
    parser.add_argument(
        "--time-limit",
        type=int,
        default=None,
        help="Override Gurobi TimeLimit seconds."
    )
    parser.add_argument(
        "--mip-gap",
        type=float,
        default=None,
        help="Override Gurobi MIPGap."
    )
    parser.add_argument(
        "--project-root",
        default=str(PROJECT_ROOT),
        help="Project root folder."
    )
    parser.add_argument(
        "--write-lp",
        action="store_true",
        help="Write model.lp to the run folder before solving."
    )
    parser.add_argument(
        "--disable-pv",
        action="store_true",
        help="Disable PV investment and PV operation."
    )
    parser.add_argument(
        "--disable-bess",
        action="store_true",
        help="Disable BESS investment and BESS operation."
    )
    parser.add_argument(
        "--speed-car-kmh",
        type=float,
        default=None,
        help="Sensitivity override for model_config.json speed_car_kmh."
    )
    parser.add_argument(
        "--value-time-sek-per-h",
        type=float,
        default=None,
        help="Sensitivity override for model_config.json value_time_sek_per_h."
    )
    parser.add_argument(
        "--max-redirection-distance-km",
        type=float,
        default=None,
        help="Sensitivity override for model_config.json max_redirection_distance_km."
    )
    parser.add_argument(
        "--sensitivity-name",
        default=None,
        help="Optional short label appended to the run folder name for sensitivity runs."
    )
    return parser.parse_args()


def load_configs(project_root: Path, dataset_arg: str | None) -> tuple[dict, dict, dict, str]:
    raw_paths = load_json(project_root / "config" / "paths.json")
    model_cfg = load_json(project_root / "config" / "model_config.json")
    solver_cfg = load_json(project_root / "config" / "solver_gurobi.json")

    dataset = dataset_arg or raw_paths.get("default_dataset", "small")
    available = list(raw_paths.get("datasets", {}).keys())

    if "datasets" not in raw_paths or dataset not in raw_paths["datasets"]:
        raise KeyError(
            f"Dataset '{dataset}' not found in config/paths.json. "
            f"Available datasets: {available}"
        )

    paths = dict(raw_paths["datasets"][dataset])
    paths["dataset"] = dataset
    paths["pvgis_excel"] = raw_paths["pvgis_excel"]
    paths["spot_price_csv"] = raw_paths["spot_price_csv"]
    paths["runs_root"] = raw_paths["runs_root"]

    for key in [
        "demand_shapefile",
        "distance_csv",
        "parking_shapefile",
        "pvgis_excel",
        "spot_price_csv",
        "runs_root",
    ]:
        paths[key] = str(resolve_project_path(project_root, paths[key]))

    return paths, model_cfg, solver_cfg, dataset



def _format_sensitivity_value(value: float) -> str:
    text = (f"{float(value):g}").replace("-", "m").replace(".", "p")
    return text


def apply_sensitivity_overrides(model_cfg: dict, args: argparse.Namespace) -> dict:
    """Apply command-line sensitivity overrides to the loaded model config.

    The base config file is not modified on disk. The returned dictionary is a
    record of the parameters changed for this run and is written to the terminal
    transcript and run metadata.
    """
    overrides = {}
    if args.speed_car_kmh is not None:
        model_cfg["speed_car_kmh"] = float(args.speed_car_kmh)
        overrides["speed_car_kmh"] = float(args.speed_car_kmh)
    if args.value_time_sek_per_h is not None:
        model_cfg["value_time_sek_per_h"] = float(args.value_time_sek_per_h)
        overrides["value_time_sek_per_h"] = float(args.value_time_sek_per_h)
    if args.max_redirection_distance_km is not None:
        model_cfg["max_redirection_distance_km"] = float(args.max_redirection_distance_km)
        overrides["max_redirection_distance_km"] = float(args.max_redirection_distance_km)
    return overrides


def make_sensitivity_suffix(args: argparse.Namespace, overrides: dict) -> str:
    if args.sensitivity_name:
        label = str(args.sensitivity_name).strip().replace(" ", "_")
        return "_" + label if label else ""
    if not overrides:
        return ""
    parts = []
    if "speed_car_kmh" in overrides:
        parts.append("speed" + _format_sensitivity_value(overrides["speed_car_kmh"]) + "kmh")
    if "value_time_sek_per_h" in overrides:
        parts.append("vot" + _format_sensitivity_value(overrides["value_time_sek_per_h"]) + "sekph")
    if "max_redirection_distance_km" in overrides:
        parts.append("dist" + _format_sensitivity_value(overrides["max_redirection_distance_km"]) + "km")
    return "_" + "_".join(parts)

def run_smoke(project_root: Path, paths: dict) -> int:
    print("========== ENVIRONMENT ==========")
    print(f"Project root : {project_root}")
    print(f"Dataset      : {paths.get('dataset')}")
    print(f"Python exe   : {sys.executable}")
    print(f"Python ver   : {sys.version}")
    print(f"Conda env    : {os.environ.get('CONDA_DEFAULT_ENV', '')}")

    print("\n========== PACKAGE IMPORTS ==========")
    packages = [
        "pandas",
        "geopandas",
        "numpy",
        "pyomo.environ",
        "networkx",
        "matplotlib",
        "shapely",
        "gurobipy",
        "openpyxl",
    ]

    ok = True
    for pkg in packages:
        try:
            mod = importlib.import_module(pkg)
            if pkg == "gurobipy":
                import gurobipy as gp
                version = gp.gurobi.version()
            else:
                version = getattr(mod, "__version__", "OK")
            print(f"{pkg:<18}: {version}")
        except Exception as exc:
            ok = False
            print(f"{pkg:<18}: FAIL - {exc}")

    try:
        import pyomo.environ as pyo
        available = pyo.SolverFactory("gurobi").available()
        print(f"{'SolverFactory':<18}: gurobi available = {available}")
        ok = ok and bool(available)
    except Exception as exc:
        ok = False
        print(f"{'SolverFactory':<18}: FAIL - {exc}")

    print("\n========== INPUT DATA PATHS ==========")
    for p, exists in check_input_paths(paths):
        print(f"{p:<115} {'OK' if exists else 'MISSING'}")
        ok = ok and exists

    print("\nSMOKE TEST:", "PASS" if ok else "FAIL")
    return 0 if ok else 1


def make_run_dir(
    paths: dict,
    scenario: str,
    dataset: str,
    hard_no_slack: bool,
    disable_pv: bool,
    disable_bess: bool,
    sensitivity_suffix: str = "",
) -> Path:
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    slack_suffix = "hardnoslack" if hard_no_slack else "slackpenalty"

    if disable_pv and disable_bess:
        tech_suffix = "noPV_noBESS"
    elif disable_pv and not disable_bess:
        tech_suffix = "noPV_withBESS"
    elif not disable_pv and disable_bess:
        tech_suffix = "withPV_noBESS"
    else:
        tech_suffix = "withPV_withBESS"

    run_dir = (
        Path(paths["runs_root"])
        / f"{stamp}_{dataset}_{scenario}_{tech_suffix}{sensitivity_suffix}_{slack_suffix}"
    )

    for sub in ["logs", "results", "model", "nodefiles"]:
        ensure_dir(run_dir / sub)

    return run_dir


def _fix_if_exists(component, *index):
    try:
        component[index].fix(0)
    except Exception:
        return


def apply_technology_switches(model, disable_pv: bool, disable_bess: bool) -> None:
    if disable_pv:
        print("Technology switch: PV disabled.")
        if hasattr(model, "PV"):
            for i in model.I:
                model.PV[i].fix(0)

        if hasattr(model, "pv_dir"):
            for i in model.I:
                for mon in model.M:
                    for t in model.H:
                        model.pv_dir[i, mon, t].fix(0)

        if hasattr(model, "pv_batt"):
            for i in model.I:
                for mon in model.M:
                    for t in model.H:
                        model.pv_batt[i, mon, t].fix(0)

    if disable_bess:
        print("Technology switch: BESS disabled.")
        if hasattr(model, "Batt"):
            for i in model.I:
                model.Batt[i].fix(0)

        soc_time_set = model.Hsoc if hasattr(model, "Hsoc") else model.H

        if hasattr(model, "soc"):
            for i in model.I:
                for mon in model.M:
                    for t in soc_time_set:
                        model.soc[i, mon, t].fix(0)

        if hasattr(model, "grid_batt"):
            for i in model.I:
                for mon in model.M:
                    for t in model.H:
                        model.grid_batt[i, mon, t].fix(0)

        if hasattr(model, "pv_batt"):
            for i in model.I:
                for mon in model.M:
                    for t in model.H:
                        model.pv_batt[i, mon, t].fix(0)

        if hasattr(model, "batt_discharge"):
            for i in model.I:
                for mon in model.M:
                    for t in model.H:
                        model.batt_discharge[i, mon, t].fix(0)

        if hasattr(model, "delta"):
            for i in model.I:
                for mon in model.M:
                    for t in model.H:
                        model.delta[i, mon, t].fix(0)




class TeeStream:
    """Write terminal output to multiple streams at once."""

    def __init__(self, *streams):
        self.streams = [s for s in streams if s is not None]

    def write(self, message: str) -> int:
        for stream in self.streams:
            try:
                stream.write(message)
            except UnicodeEncodeError:
                stream.write(message.encode("utf-8", errors="replace").decode("utf-8"))
        self.flush()
        return len(message)

    def flush(self) -> None:
        for stream in self.streams:
            try:
                stream.flush()
            except Exception:
                pass


def write_run_folder_readme(
    run_dir: Path,
    dataset: str,
    scenario: str,
    disable_pv: bool,
    disable_bess: bool,
    sensitivity_overrides: dict | None = None,
) -> None:
    readme = run_dir / "README_RUN_FOLDER.txt"
    tech = (
        "no PV, no BESS" if disable_pv and disable_bess else
        "PV enabled, BESS disabled" if (not disable_pv and disable_bess) else
        "PV disabled, BESS enabled" if (disable_pv and not disable_bess) else
        "PV enabled, BESS enabled"
    )
    sensitivity_overrides = sensitivity_overrides or {}
    sensitivity_text = "None" if not sensitivity_overrides else ", ".join(
        f"{k}={v}" for k, v in sensitivity_overrides.items()
    )
    readme.write_text(
        "Monolithic optimization run folder\n"
        "==================================\n\n"
        "This folder is produced by src/run_optimization.py. It contains the outputs from the full monolithic Pyomo/Gurobi formulation.\n\n"
        "Core files:\n"
        "- README_RUN.txt: complete terminal transcript from this run.\n"
        "- results/model_summary.csv: detailed economic, energy, and infrastructure metrics.\n"
        "- results/infrastructure_by_hex.csv: charger/PV/BESS deployment by cell.\n"
        "- results/redirections.csv and redirections_by_type.csv: optimized redirected flows.\n"
        "- results/hourly_energy.csv: slot-level energy dispatch.\n"
        "- logs/gurobi_run.log: Gurobi solver log.\n"
        "- logs/pyomo_solve.log: Pyomo solve log.\n\n"
        f"Scenario: {scenario}\n"
        f"Dataset: {dataset}\n"
        f"Technology: {tech}\n"
        f"Sensitivity overrides: {sensitivity_text}\n",
        encoding="utf-8",
    )


def _run_optimization_impl(
    args: argparse.Namespace,
    project_root: Path,
    paths: dict,
    model_cfg: dict,
    solver_cfg: dict,
    dataset: str,
    run_dir: Path,
) -> int:
    print(f"Project root  : {project_root}")
    print(f"Dataset       : {dataset}")
    print(f"Scenario      : {args.scenario}")
    print(f"Disable PV    : {args.disable_pv}")
    print(f"Disable BESS  : {args.disable_bess}")
    print(f"Hard no-slack : {args.hard_no_slack}")
    sensitivity_overrides = getattr(args, "_sensitivity_overrides", {}) or {}
    if sensitivity_overrides:
        print("Sensitivity overrides:")
        for key, value in sensitivity_overrides.items():
            print(f"  {key}: {value}")
    else:
        print("Sensitivity overrides: none")
    print(f"Run directory : {run_dir}")

    print("Loading inputs...")
    raw = load_inputs(paths)

    print("Preprocessing inputs...")
    data = preprocess(raw, model_cfg)
    data["dataset"] = dataset
    data["disable_pv"] = args.disable_pv
    data["disable_bess"] = args.disable_bess

    print(f"Hex cells: {len(data['hex_ids'])}")
    print(f"Active redirection arc-slots: {len(data['allowed_st']):,}")

    print("Building type-aware Pyomo model...")
    model = build_model(data, model_cfg)

    apply_technology_switches(
        model=model,
        disable_pv=args.disable_pv,
        disable_bess=args.disable_bess,
    )

    apply_scenario(model, args.scenario)

    if args.hard_no_slack:
        apply_hard_no_slack(model)

    if args.write_lp:
        lp_path = run_dir / "model" / "model.lp"
        model.write(str(lp_path), io_options={"symbolic_solver_labels": True})
        print(f"LP model written to: {lp_path}")

    print("Solving with Gurobi...")
    results = solve_model(model, solver_cfg, run_dir)
    print(results.solver)

    term = str(results.solver.termination_condition).lower()
    if "infeasible" in term:
        print(
            "\nModel is infeasible under the current options. "
            "If --hard-no-slack was used, rerun without it and inspect slack diagnostics."
        )
        print(f"Run directory: {run_dir}")
        return 2

    print_summary(model, data, model_cfg)

    print("Writing CSV/XLSX outputs...")
    export_all(model, data, model_cfg, run_dir)

    print(f"Run finished successfully. Run directory: {run_dir}")
    return 0


def main() -> int:
    args = parse_args()
    project_root = Path(args.project_root).resolve()
    paths, model_cfg, solver_cfg, dataset = load_configs(project_root, args.dataset)
    sensitivity_overrides = apply_sensitivity_overrides(model_cfg, args)
    args._sensitivity_overrides = sensitivity_overrides
    sensitivity_suffix = make_sensitivity_suffix(args, sensitivity_overrides)

    if args.threads is not None:
        solver_cfg["threads"] = int(args.threads)
    if args.time_limit is not None:
        solver_cfg["time_limit_seconds"] = int(args.time_limit)
    if args.mip_gap is not None:
        solver_cfg["mip_gap"] = float(args.mip_gap)

    if args.smoke:
        return run_smoke(project_root, paths)

    run_dir = make_run_dir(
        paths=paths,
        scenario=args.scenario,
        dataset=dataset,
        hard_no_slack=args.hard_no_slack,
        disable_pv=args.disable_pv,
        disable_bess=args.disable_bess,
        sensitivity_suffix=sensitivity_suffix,
    )
    write_run_folder_readme(
        run_dir,
        dataset,
        args.scenario,
        args.disable_pv,
        args.disable_bess,
        sensitivity_overrides=sensitivity_overrides,
    )

    terminal_log = run_dir / "README_RUN.txt"
    with terminal_log.open("w", encoding="utf-8", errors="replace") as log_file:
        tee_out = TeeStream(sys.__stdout__, log_file)
        tee_err = TeeStream(sys.__stderr__, log_file)
        from contextlib import redirect_stdout, redirect_stderr
        import traceback

        with redirect_stdout(tee_out), redirect_stderr(tee_err):
            print("========== MONOLITHIC TERMINAL LOG ==========")
            print(f"Run transcript : {terminal_log}")
            print("=============================================\n")
            try:
                rc = _run_optimization_impl(
                    args=args,
                    project_root=project_root,
                    paths=paths,
                    model_cfg=model_cfg,
                    solver_cfg=solver_cfg,
                    dataset=dataset,
                    run_dir=run_dir,
                )
                print(f"\nTerminal transcript written to: {terminal_log}")
                return rc
            except Exception:
                print("\nERROR: Monolithic run failed. Full traceback follows.\n")
                traceback.print_exc()
                print(f"\nTerminal transcript written to: {terminal_log}")
                return 1


if __name__ == "__main__":
    raise SystemExit(main())
