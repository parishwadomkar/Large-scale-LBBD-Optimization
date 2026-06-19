from __future__ import annotations

from pathlib import Path
from pyomo.environ import SolverFactory


def solve_model(model, solver_cfg: dict, run_dir: Path):
    log_dir = run_dir / "logs"
    node_dir = run_dir / "nodefiles"
    log_dir.mkdir(parents=True, exist_ok=True)
    node_dir.mkdir(parents=True, exist_ok=True)

    opt = SolverFactory(solver_cfg.get("solver", "gurobi"))
    opt.options["Threads"] = int(solver_cfg["threads"])
    opt.options["Presolve"] = int(solver_cfg["presolve"])
    opt.options["NumericFocus"] = int(solver_cfg["numeric_focus"])
    opt.options["Heuristics"] = float(solver_cfg["heuristics"])
    opt.options["MIPGap"] = float(solver_cfg["mip_gap"])
    opt.options["NodefileStart"] = float(solver_cfg["nodefile_start_gb"])
    opt.options["Cuts"] = int(solver_cfg["cuts"])
    opt.options["TimeLimit"] = int(solver_cfg["time_limit_seconds"])
    opt.options["LogFile"] = str((log_dir / "gurobi_run.log").resolve()).replace("\\", "/")
    opt.options["MIPFocus"] = int(solver_cfg["mip_focus"])
    opt.options["NodefileDir"] = str(node_dir.resolve())

    return opt.solve(
        model,
        tee=bool(solver_cfg.get("tee", True)),
        logfile=str(log_dir / "pyomo_solve.log"),
    )
