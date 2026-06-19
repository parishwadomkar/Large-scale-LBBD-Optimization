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


def compute_stage1_metrics(model, data: dict, cfg: dict, redir_rows: list[dict[str, Any]]) -> dict[str, Any]:
    incoming = _redir_incoming_by_slot_type(redir_rows)
    outgoing = _redir_outgoing_by_slot_type(redir_rows)
    ndays = data["N_MONTH"]
    days = data["DAYS"]
    pub_types = data["PUB_TYPES"]

    local_revenue = 0.0
    local_grid_cost = 0.0
    slack_pen = 0.0
    total_grid = 0.0
    for i in model.I:
        for mon in model.M:
            for t in model.H:
                local_grid = sv(model.grid_dir[i, mon, t])
                local_grid_cost += ndays[mon] * sv(model.tou[mon, t]) * local_grid
                total_grid += ndays[mon] * local_grid
                for c in model.C_pub:
                    local_energy = sv(model.e_home[i, mon, t, c]) + sv(model.q[i, mon, t, c]) - sv(model.R[i, mon, t, c])
                    local_revenue += ndays[mon] * sv(model.Price[c]) * local_energy
                for b in model.B:
                    slack_pen += float(cfg["penalty_per_kwh_slack"]) * ndays[mon] * sv(model.slack[i, mon, t, b])

    redir_revenue = 0.0
    redir_grid_cost = 0.0
    redir_price_cost = 0.0
    redir_distance_cost = 0.0
    redir_energy = 0.0
    for r in redir_rows:
        mon = str(r["Month"])
        t = int(r["TimeIndex"])
        co = str(r["OriginType"])
        cd = str(r["DestinationType"])
        i = int(r["from_HexID"])
        j = int(r["to_HexID"])
        z = float(r["Energy_kWh_day"])
        redir_energy += ndays[mon] * z
        redir_revenue += ndays[mon] * data["charger_price"][cd] * z
        redir_grid_cost += ndays[mon] * data["tou"][mon][t] * z
        redir_price_cost += ndays[mon] * data["delta_price"][(co, cd)] * z
        redir_distance_cost += ndays[mon] * (data["T_dict"].get((i, j), 0.0) / float(cfg["x_kwh_per_trip"])) * z

    capex_chargers = days * sum(sv(model.PVF_cost[c]) * sv(model.x[i, c]) for i in model.I for c in model.C_pub)
    revenue_total = local_revenue + redir_revenue
    grid_cost_total = local_grid_cost + redir_grid_cost
    profit = revenue_total - grid_cost_total - redir_price_cost - redir_distance_cost - slack_pen - capex_chargers

    rows = {
        "dataset": data.get("dataset", "unknown"),
        "annual_profit_SEK": profit,
        "revenue_all_chargers_SEK": revenue_total,
        "grid_cost_SEK": grid_cost_total,
        "redirection_distance_cost_SEK": redir_distance_cost,
        "redirection_price_compensation_SEK": redir_price_cost,
        "redirection_total_cost_SEK": redir_distance_cost + redir_price_cost,
        "slack_penalty_SEK": slack_pen,
        "capex_chargers_SEK": capex_chargers,
        "capex_PV_BESS_SEK": 0.0,
        "grid_direct_kWh": total_grid + redir_energy,
        "grid_to_battery_kWh": 0.0,
        "grid_total_kWh": total_grid + redir_energy,
        "pv_direct_kWh": 0.0,
        "pv_to_battery_kWh": 0.0,
        "pv_used_total_kWh": 0.0,
        "battery_discharge_kWh": 0.0,
        "energy_redirected_kWh": redir_energy,
        "PV_panels_installed": 0.0,
        "battery_units_installed": 0.0,
        "max_abs_soc_gap_Jan0_Dec48_kWh": 0.0,
    }
    for c in pub_types:
        installed = sum(sv(model.x[i, c]) for i in model.I)
        local_energy = sum(
            ndays[mon] * (sv(model.e_home[i, mon, t, c]) + sv(model.q[i, mon, t, c]) - sv(model.R[i, mon, t, c]))
            for i in model.I for mon in model.M for t in model.H
        )
        incoming_energy = sum(ndays[mon] * incoming.get((int(i), mon, int(t), c), 0.0) for i in model.I for mon in model.M for t in model.H)
        energy_c = local_energy + incoming_energy
        annual_cap_c = installed * data["charger_capacity_pub"][c] * len(data["INTERVALS"]) * days
        rows[f"chargers_{c}_installed"] = installed
        rows[f"energy_{c}_kWh"] = energy_c
        rows[f"capacity_upper_bound_{c}_kWh"] = annual_cap_c
        rows[f"capacity_ratio_{c}"] = energy_c / annual_cap_c if annual_cap_c > 0 else 0.0
    return rows


def export_model_summary(metrics: dict[str, Any], results_dir: Path) -> pd.DataFrame:
    df = pd.DataFrame([{"Metric": k, "Value": v} for k, v in metrics.items()])
    df.to_csv(results_dir / "model_summary.csv", index=False)
    return df


def export_infrastructure(model, data: dict, results_dir: Path) -> pd.DataFrame:
    rows = []
    for i in model.I:
        row = {"HexID": int(i)}
        for c in model.C_pub:
            row[f"{c}_chargers"] = sv(model.x[i, c])
            row[f"{c}_footprint"] = data["charger_footprint"][str(c)] * sv(model.x[i, c])
            row[f"{c}_capacity_kWh_slot"] = data["charger_capacity_pub"][str(c)] * sv(model.x[i, c])
        row["PV_panels"] = 0.0
        row["Battery_units"] = 0.0
        row["Total_charger_footprint"] = sum(data["charger_footprint"][str(c)] * sv(model.x[i, c]) for c in model.C_pub)
        row["Total_public_capacity_kWh_slot"] = sum(data["charger_capacity_pub"][str(c)] * sv(model.x[i, c]) for c in model.C_pub)
        rows.append(row)
    df = pd.DataFrame(rows).sort_values("HexID")
    df.to_csv(results_dir / "infrastructure_by_hex.csv", index=False)
    return df


def export_energy_by_charger_type(model, data: dict, redir_rows: list[dict[str, Any]], results_dir: Path) -> pd.DataFrame:
    incoming = _redir_incoming_by_slot_type(redir_rows)
    rows = []
    days = data["DAYS"]
    ndays = data["N_MONTH"]
    for c in model.C_pub:
        installed = sum(sv(model.x[i, c]) for i in model.I)
        annual_capacity = installed * data["charger_capacity_pub"][str(c)] * len(data["INTERVALS"]) * days
        home_energy = sum(ndays[mon] * sv(model.e_home[i, mon, t, c]) for i in model.I for mon in model.M for t in model.H)
        public_local = sum(ndays[mon] * (sv(model.q[i, mon, t, c]) - sv(model.R[i, mon, t, c])) for i in model.I for mon in model.M for t in model.H)
        public_incoming = sum(ndays[mon] * incoming.get((int(i), mon, int(t), str(c)), 0.0) for i in model.I for mon in model.M for t in model.H)
        vals = {"home": home_energy, "public": public_local + public_incoming}
        for b, energy in vals.items():
            rows.append({
                "ChargerType": str(c),
                "DemandClass": b,
                "AnnualEnergy_kWh": energy,
                "InstalledChargers": installed,
                "AnnualCapacity_kWh": annual_capacity,
                "CapacityRatio_all_classes": None,
            })
        total = home_energy + public_local + public_incoming
        rows.append({
            "ChargerType": str(c),
            "DemandClass": "ALL",
            "AnnualEnergy_kWh": total,
            "InstalledChargers": installed,
            "AnnualCapacity_kWh": annual_capacity,
            "CapacityRatio_all_classes": total / annual_capacity if annual_capacity > 0 else 0.0,
        })
    df = pd.DataFrame(rows)
    df.to_csv(results_dir / "energy_by_charger_type.csv", index=False)
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


def export_hourly_energy(model, data: dict, redir_rows: list[dict[str, Any]], results_dir: Path) -> pd.DataFrame:
    incoming = _redir_incoming_by_slot_type(redir_rows)
    outgoing = _redir_outgoing_by_slot_type(redir_rows)
    rows = []
    for i in model.I:
        for mon in model.M:
            for t in model.H:
                row = {
                    "HexID": int(i),
                    "Month": mon,
                    "TimeIndex": int(t),
                    "Demand_home_kWh_day": sv(model.Demand[i, mon, t, "home"]),
                    "Demand_public_base_kWh_day": sv(model.Demand[i, mon, t, "public"]),
                    "Redirect_out_kWh_day": sum(outgoing.get((int(i), mon, int(t), str(c)), 0.0) for c in model.C_pub),
                    "Redirect_in_kWh_day": sum(incoming.get((int(i), mon, int(t), str(c)), 0.0) for c in model.C_pub),
                    "Grid_direct_kWh_day": sv(model.grid_dir[i, mon, t]) + sum(incoming.get((int(i), mon, int(t), str(c)), 0.0) for c in model.C_pub),
                    "Grid_batt_kWh_day": 0.0,
                    "PV_direct_kWh_day": 0.0,
                    "PV_batt_kWh_day": 0.0,
                    "Batt_discharge_kWh_day": 0.0,
                    "SOC_start_kWh": 0.0,
                    "SOC_end_kWh": 0.0,
                }
                for c in model.C_pub:
                    row[f"E_{c}_home_kWh_day"] = sv(model.e_home[i, mon, t, c])
                    row[f"E_{c}_public_kWh_day"] = sv(model.q[i, mon, t, c]) - sv(model.R[i, mon, t, c]) + incoming.get((int(i), mon, int(t), str(c)), 0.0)
                rows.append(row)
    df = pd.DataFrame(rows)
    df.to_csv(results_dir / "hourly_energy.csv", index=False)
    return df


def export_slack(model, data: dict, results_dir: Path) -> pd.DataFrame:
    rows = []
    for i in model.I:
        for mon in model.M:
            for t in model.H:
                for b in model.B:
                    sl = sv(model.slack[i, mon, t, b])
                    if sl > 1e-8:
                        rows.append({"HexID": int(i), "Month": mon, "TimeIndex": int(t), "DemandClass": str(b), "Slack_kWh_day": sl, "Slack_kWh_annual": data["N_MONTH"][mon] * sl})
    df = pd.DataFrame(rows)
    df.to_csv(results_dir / "slack.csv", index=False)
    return df


def export_master_solution(model, results_dir: Path) -> pd.DataFrame:
    rows = []
    for i in model.I:
        for c in model.C_pub:
            rows.append({"variable": "x", "HexID": int(i), "Month": "", "TimeIndex": "", "Type": str(c), "Value": sv(model.x[i, c])})
    df = pd.DataFrame(rows)
    df.to_csv(results_dir / "lbbd_master_solution.csv", index=False)
    return df


def write_combined_xlsx(results_dir: Path, frames: dict[str, pd.DataFrame]) -> Path | None:
    out = results_dir / "combined_results.xlsx"
    try:
        with pd.ExcelWriter(out) as writer:
            for name, df in frames.items():
                df.to_excel(writer, sheet_name=name[:31], index=False)
        return out
    except Exception as exc:
        print(f"WARNING: Could not write combined XLSX ({exc}). CSV files were still written.")
        return None


def export_stage1_all(model, data: dict, cfg: dict, run_dir: Path, redir_rows: list[dict[str, Any]], history_df: pd.DataFrame, sp_df: pd.DataFrame, cuts_df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    results_dir = run_dir / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    metrics = compute_stage1_metrics(model, data, cfg, redir_rows)
    frames = {
        "model_summary": export_model_summary(metrics, results_dir),
        "infrastructure_by_hex": export_infrastructure(model, data, results_dir),
        "energy_by_type": export_energy_by_charger_type(model, data, redir_rows, results_dir),
        "origin_type_q": export_origin_type_allocation(model, data, results_dir),
        "hourly_energy": export_hourly_energy(model, data, redir_rows, results_dir),
        "slack": export_slack(model, data, results_dir),
        "lbbd_master_solution": export_master_solution(model, results_dir),
        "lbbd_iteration_history": history_df,
        "lbbd_subproblem_summary": sp_df,
        "lbbd_cuts": cuts_df,
    }
    redir_agg, redir_type = export_redirections(redir_rows, data, results_dir)
    frames["redirections"] = redir_agg
    frames["redirections_by_type"] = redir_type
    history_df.to_csv(results_dir / "lbbd_iteration_history.csv", index=False)
    history_df.to_csv(run_dir / "iterations" / "lbbd_iteration_history.csv", index=False)
    sp_df.to_csv(results_dir / "lbbd_subproblem_summary.csv", index=False)
    cuts_df.to_csv(results_dir / "lbbd_cuts.csv", index=False)
    model_summary = pd.DataFrame([{"Metric": "stage", "Value": "1_continuous_redirection_lp"}])
    model_summary.to_csv(results_dir / "model_summary_stage1_notes.csv", index=False)
    xlsx = write_combined_xlsx(results_dir, frames)
    if xlsx:
        print(f"Combined XLSX written to: {xlsx}")
    return frames
