from __future__ import annotations

import csv
import shutil
from pathlib import Path
from typing import Any


def read_model_summary(results_dir: Path) -> dict[str, str]:
    path = results_dir / "model_summary.csv"
    if not path.exists():
        return {}
    out: dict[str, str] = {}
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            metric = row.get("Metric")
            value = row.get("Value")
            if metric is not None and value is not None:
                out[str(metric)] = str(value)
    return out


def write_iteration_history(path: Path, row: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "workflow_phase",
        "iteration",
        "dataset",
        "scenario",
        "status",
        "return_code",
        "monolithic_run_dir",
        "annual_profit_SEK",
        "revenue_all_chargers_SEK",
        "grid_cost_SEK",
        "redirection_total_cost_SEK",
        "slack_penalty_SEK",
        "capex_chargers_SEK",
        "capex_PV_BESS_SEK",
        "energy_redirected_kWh",
        "lb_SEK",
        "ub_SEK",
        "lbbd_gap",
        "elapsed_seconds",
    ]
    write_header = not path.exists()
    with path.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        if write_header:
            writer.writeheader()
        writer.writerow(row)


def copy_key_outputs(monolithic_run_dir: Path, lbbd_results_dir: Path) -> None:
    lbbd_results_dir.mkdir(parents=True, exist_ok=True)
    source_results = monolithic_run_dir / "results"
    if not source_results.exists():
        return
    key_files = [
        "model_summary.csv",
        "infrastructure_by_hex.csv",
        "energy_by_charger_type.csv",
        "redirections.csv",
        "redirections_by_type.csv",
        "origin_type_allocation_q.csv",
        "hourly_energy.csv",
        "slack.csv",
        "combined_results.xlsx",
    ]
    for name in key_files:
        src = source_results / name
        if src.exists():
            shutil.copy2(src, lbbd_results_dir / f"monolithic_{name}")
