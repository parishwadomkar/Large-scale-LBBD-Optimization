from __future__ import annotations

import json
import sys
from contextlib import contextmanager, redirect_stderr, redirect_stdout
from datetime import datetime
from pathlib import Path
from typing import Any, TextIO


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


class TeeStream:
    """Write text to multiple streams, normally console + run-log file."""

    def __init__(self, *streams: TextIO):
        self.streams = streams

    def write(self, data: str) -> int:
        for stream in self.streams:
            stream.write(data)
        return len(data)

    def flush(self) -> None:
        for stream in self.streams:
            stream.flush()

    def isatty(self) -> bool:
        return bool(self.streams and hasattr(self.streams[0], "isatty") and self.streams[0].isatty())


@contextmanager
def tee_console_to_file(log_path: Path):
    """Mirror stdout and stderr to a UTF-8 text file while preserving console output."""
    ensure_dir(log_path.parent)
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    with log_path.open("w", encoding="utf-8", buffering=1) as log_file:
        tee_out = TeeStream(old_stdout, log_file)
        tee_err = TeeStream(old_stderr, log_file)
        with redirect_stdout(tee_out), redirect_stderr(tee_err):
            yield log_file
