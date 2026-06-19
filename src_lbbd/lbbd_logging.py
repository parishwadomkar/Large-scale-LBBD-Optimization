from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def technology_suffix(disable_pv: bool, disable_bess: bool) -> str:
    if disable_pv and disable_bess:
        return "noPV_noBESS"
    if disable_pv and not disable_bess:
        return "noPV_withBESS"
    if not disable_pv and disable_bess:
        return "withPV_noBESS"
    return "withPV_withBESS"


def create_lbbd_run_dir(project_root: Path, dataset: str, scenario: str, disable_pv: bool, disable_bess: bool) -> Path:
    stamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    tech = technology_suffix(disable_pv, disable_bess)
    run_dir = project_root / "runs" / f"{stamp}_{dataset}_{scenario}_LBBD_{tech}"
    for sub in ["logs", "results", "iterations", "master", "subproblems"]:
        ensure_dir(run_dir / sub)
    return run_dir


def write_json(path: Path, payload: dict[str, Any]) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
