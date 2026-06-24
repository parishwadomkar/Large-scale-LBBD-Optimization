from __future__ import annotations

import csv
from pathlib import Path


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
