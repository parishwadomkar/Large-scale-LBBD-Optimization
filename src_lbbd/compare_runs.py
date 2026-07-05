#!/usr/bin/env python
from __future__ import annotations

import argparse
from pathlib import Path
import pandas as pd

KEYS = [
    "annual_profit_SEK", "revenue_all_chargers_SEK", "grid_cost_SEK",
    "redirection_distance_cost_SEK", "redirection_price_compensation_SEK",
    "redirection_total_cost_SEK", "slack_penalty_SEK", "capex_chargers_SEK",
    "capex_PV_BESS_SEK", "grid_direct_kWh", "grid_to_battery_kWh",
    "grid_total_kWh", "pv_direct_kWh", "pv_to_battery_kWh", "pv_used_total_kWh",
    "battery_discharge_kWh", "energy_redirected_kWh", "PV_panels_installed",
    "battery_units_installed", "chargers_slow_installed", "chargers_medium_installed",
    "chargers_fast_installed", "energy_slow_kWh", "energy_medium_kWh", "energy_fast_kWh",
]


def read_summary(run: Path) -> dict:
    p = run / "results" / "model_summary.csv"
    if not p.exists():
        raise FileNotFoundError(p)
    df = pd.read_csv(p)
    out = {}
    for _, r in df.iterrows():
        key = str(r["Metric"])
        val = r["Value"]
        try:
            out[key] = float(val)
        except Exception:
            out[key] = val
    return out


def redir_total(run: Path, name: str) -> float:
    p = run / "results" / name
    if not p.exists():
        return 0.0
    df = pd.read_csv(p)
    return float(df.get("Energy_kWh_annual", pd.Series(dtype=float)).sum())


def main() -> int:
    ap = argparse.ArgumentParser(description="Compare an LBBD run folder against a monolithic run folder.")
    ap.add_argument("--lbbd-run", required=True)
    ap.add_argument("--monolithic-run", required=True)
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    aw = Path(args.lbbd_run).resolve()
    mono = Path(args.monolithic_run).resolve()
    a, m = read_summary(aw), read_summary(mono)
    rows = []
    for k in KEYS:
        av, mv = a.get(k), m.get(k)
        if isinstance(av, float) and isinstance(mv, float):
            diff = av - mv
            rel = diff / max(1.0, abs(mv))
        else:
            diff, rel = None, None
        rows.append({"Metric": k, "LBBD": av, "Monolithic": mv, "Difference": diff, "RelativeDifference": rel})
    rows.extend([
        {"Metric": "LBBD_redirections_vs_type_energy_diff_kWh", "LBBD": redir_total(aw, "redirections.csv") - redir_total(aw, "redirections_by_type.csv"), "Monolithic": None, "Difference": None, "RelativeDifference": None},
        {"Metric": "Mono_redirections_vs_type_energy_diff_kWh", "LBBD": None, "Monolithic": redir_total(mono, "redirections.csv") - redir_total(mono, "redirections_by_type.csv"), "Difference": None, "RelativeDifference": None},
    ])
    df = pd.DataFrame(rows)
    out = Path(args.out).resolve() if args.out else aw / "results" / "lbbd_vs_monolithic_comparison.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print(df.to_string(index=False))
    print(f"Comparison written to: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
