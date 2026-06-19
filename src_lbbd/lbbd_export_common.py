from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
import pyomo.environ as pyo

def sv(obj, default: float = 0.0) -> float:
    try:
        val = pyo.value(obj, exception=False)
        return default if val is None else float(val)
    except Exception:
        return default

def _redir_incoming_by_slot_type(redir_rows: list[dict[str, Any]]) -> dict[tuple[int, str, int, str], float]:
    incoming: dict[tuple[int, str, int, str], float] = {}
    for r in redir_rows:
        key = (int(r["to_HexID"]), str(r["Month"]), int(r["TimeIndex"]), str(r["DestinationType"]))
        incoming[key] = incoming.get(key, 0.0) + float(r["Energy_kWh_day"])
    return incoming

def _redir_outgoing_by_slot_type(redir_rows: list[dict[str, Any]]) -> dict[tuple[int, str, int, str], float]:
    outgoing: dict[tuple[int, str, int, str], float] = {}
    for r in redir_rows:
        key = (int(r["from_HexID"]), str(r["Month"]), int(r["TimeIndex"]), str(r["OriginType"]))
        outgoing[key] = outgoing.get(key, 0.0) + float(r["Energy_kWh_day"])
    return outgoing

def export_model_summary(metrics: dict[str, Any], results_dir: Path) -> pd.DataFrame:
    df = pd.DataFrame([{"Metric": k, "Value": v} for k, v in metrics.items()])
    df.to_csv(results_dir / "model_summary.csv", index=False)
    return df

def export_redirections(redir_rows: list[dict[str, Any]], data: dict, results_dir: Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    by_type = pd.DataFrame(redir_rows)
    if by_type.empty:
        by_type.to_csv(results_dir / "redirections_by_type.csv", index=False)
        by_type.to_csv(results_dir / "redirections.csv", index=False)
        return by_type, by_type
    by_type["DeltaPrice_SEK_per_kWh"] = by_type.apply(lambda r: data["delta_price"][(str(r["OriginType"]), str(r["DestinationType"]))], axis=1)
    by_type["PriceComp_SEK_annual"] = by_type["DeltaPrice_SEK_per_kWh"] * by_type["Energy_kWh_annual"]
    by_type.to_csv(results_dir / "redirections_by_type.csv", index=False)
    agg = (
        by_type.groupby(["from_HexID", "to_HexID", "Month", "TimeIndex"], as_index=False)
        .agg(Energy_kWh_day=("Energy_kWh_day", "sum"), Energy_kWh_annual=("Energy_kWh_annual", "sum"), AnnualNetValue_SEK=("AnnualNetValue_SEK", "sum"))
    )
    agg["Distance_km"] = agg.apply(lambda r: data["dist_dict"].get((int(r["from_HexID"]), int(r["to_HexID"])), None), axis=1)
    if {"Yarc", "Trips_day", "Tail_kWh_day"}.issubset(by_type.columns):
        trip_agg = (
            by_type.groupby(["from_HexID", "to_HexID", "Month", "TimeIndex"], as_index=False)
            .agg(Yarc=("Yarc", "max"), Trips=("Trips_day", "sum"), Tail_kWh=("Tail_kWh_day", "sum"))
        )
        agg = agg.merge(trip_agg, on=["from_HexID", "to_HexID", "Month", "TimeIndex"], how="left")
        agg["Yarc"] = agg["Yarc"].fillna((agg["Energy_kWh_day"] > 1e-8).astype(float))
        agg["Trips"] = agg["Trips"].fillna(0.0)
        agg["Tail_kWh"] = agg["Tail_kWh"].fillna(0.0)
    else:
        agg["Yarc"] = (agg["Energy_kWh_day"] > 1e-8).astype(float)
        agg["Trips"] = agg["Energy_kWh_day"] / float(data.get("x_kWh", 20.0)) if "x_kWh" in data else agg["Energy_kWh_day"] / 20.0
        agg["Tail_kWh"] = 0.0
    agg.to_csv(results_dir / "redirections.csv", index=False)
    return agg, by_type

def export_origin_type_allocation(model, data: dict, results_dir: Path) -> pd.DataFrame:
    rows = []
    for i in model.I:
        for mon in model.M:
            for t in model.H:
                for c in model.C_pub:
                    q = sv(model.q[i, mon, t, c])
                    rows.append({
                        "HexID": int(i),
                        "Month": mon,
                        "TimeIndex": int(t),
                        "OriginType": str(c),
                        "q_origin_baseline_kWh_day": q,
                        "q_origin_baseline_kWh_annual": data["N_MONTH"][mon] * q,
                        "R_redirectable_kWh_day": sv(model.R[i, mon, t, c]),
                    })
    df = pd.DataFrame(rows)
    df.to_csv(results_dir / "origin_type_allocation_or_benchmark_tariff.csv", index=False)
    df.to_csv(results_dir / "origin_type_allocation_q.csv", index=False)
    return df

def write_combined_xlsx(results_dir: Path, frames: dict[str, pd.DataFrame]) -> Path | None:
    """Write a convenience Excel workbook without failing on large full-scale outputs.

    Excel worksheets are limited to 1,048,576 rows. The full dataset can exceed
    this limit for detailed redirection/type-flow tables, while the CSV exports
    remain the authoritative complete outputs. For the combined workbook we split
    oversized frames across numbered sheets so the export remains useful and no
    spurious warning is raised.
    """
    out = results_dir / "combined_results.xlsx"
    max_excel_rows = 1_048_576
    max_data_rows = max_excel_rows - 1  # reserve one row for the header
    try:
        with pd.ExcelWriter(out) as writer:
            used_sheet_names: set[str] = set()
            for name, df in frames.items():
                base = str(name)[:25] or "sheet"
                if len(df) <= max_data_rows:
                    sheet = base[:31]
                    counter = 1
                    while sheet in used_sheet_names:
                        suffix = f"_{counter}"
                        sheet = f"{base[:31-len(suffix)]}{suffix}"
                        counter += 1
                    used_sheet_names.add(sheet)
                    df.to_excel(writer, sheet_name=sheet, index=False)
                    continue

                n_parts = (len(df) + max_data_rows - 1) // max_data_rows
                for part in range(n_parts):
                    start = part * max_data_rows
                    end = min((part + 1) * max_data_rows, len(df))
                    suffix = f"_{part + 1}"
                    sheet = f"{base[:31-len(suffix)]}{suffix}"
                    counter = 1
                    while sheet in used_sheet_names:
                        alt_suffix = f"_{part + 1}_{counter}"
                        sheet = f"{base[:31-len(alt_suffix)]}{alt_suffix}"
                        counter += 1
                    used_sheet_names.add(sheet)
                    df.iloc[start:end].to_excel(writer, sheet_name=sheet, index=False)
        return out
    except Exception as exc:
        print(f"WARNING: Could not write combined XLSX ({exc}). CSV files were still written.")
        return None
