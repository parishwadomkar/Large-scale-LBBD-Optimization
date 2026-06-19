from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd
import pyomo.environ as pyo

from .lbbd_export_stage1 import (
    _redir_incoming_by_slot_type,
    _redir_outgoing_by_slot_type,
    export_model_summary,
    export_redirections,
    export_origin_type_allocation,
    write_combined_xlsx,
)


def sv(obj, default: float = 0.0) -> float:
    try:
        val = pyo.value(obj, exception=False)
        return default if val is None else float(val)
    except Exception:
        return default


def compute_stage4_metrics(model, data: dict, cfg: dict, redir_rows: list[dict[str, Any]]) -> dict[str, Any]:
    incoming = _redir_incoming_by_slot_type(redir_rows)
    ndays = data["N_MONTH"]
    days = data["DAYS"]
    pub_types = data["PUB_TYPES"]

    local_revenue = 0.0
    local_grid_cost = 0.0
    slack_pen = 0.0
    local_grid_kwh = 0.0
    grid_batt_kwh = 0.0
    pv_direct_kwh = 0.0
    pv_batt_kwh = 0.0
    batt_dis_kwh = 0.0
    for i in model.I:
        for mon in model.M:
            for t in model.H:
                g = sv(model.grid_dir[i, mon, t])
                gb = sv(model.grid_batt[i, mon, t])
                pv = sv(model.pv_dir[i, mon, t])
                pvb = sv(model.pv_batt[i, mon, t])
                bd = sv(model.batt_discharge[i, mon, t])
                local_grid_cost += ndays[mon] * sv(model.tou[mon, t]) * (g + gb)
                local_grid_kwh += ndays[mon] * g
                grid_batt_kwh += ndays[mon] * gb
                pv_direct_kwh += ndays[mon] * pv
                pv_batt_kwh += ndays[mon] * pvb
                batt_dis_kwh += ndays[mon] * bd
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
    capex_pv = days * sum(sv(model.PVF_PV) * sv(model.PV[i]) for i in model.I)
    capex_batt = days * sum(sv(model.PVF_Batt) * sv(model.Batt[i]) for i in model.I)
    revenue_total = local_revenue + redir_revenue
    grid_cost_total = local_grid_cost + redir_grid_cost
    profit = revenue_total - grid_cost_total - redir_price_cost - redir_distance_cost - slack_pen - capex_chargers - capex_pv - capex_batt

    last_h = max(data["INTERVALS"])
    if len(list(model.I)):
        soc_gap = max(abs(sv(model.soc[i, "December", last_h]) - sv(model.soc[i, "January", 0])) for i in model.I)
    else:
        soc_gap = 0.0

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
        "capex_PV_BESS_SEK": capex_pv + capex_batt,
        "grid_direct_kWh": local_grid_kwh + redir_energy,
        "grid_to_battery_kWh": grid_batt_kwh,
        "grid_total_kWh": local_grid_kwh + grid_batt_kwh + redir_energy,
        "pv_direct_kWh": pv_direct_kwh,
        "pv_to_battery_kWh": pv_batt_kwh,
        "pv_used_total_kWh": pv_direct_kwh + pv_batt_kwh,
        "battery_discharge_kWh": batt_dis_kwh,
        "energy_redirected_kWh": redir_energy,
        "PV_panels_installed": sum(sv(model.PV[i]) for i in model.I),
        "battery_units_installed": sum(sv(model.Batt[i]) for i in model.I),
        "max_abs_soc_gap_Jan0_Dec48_kWh": soc_gap,
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


def export_infrastructure_stage4(model, data: dict, results_dir: Path) -> pd.DataFrame:
    rows = []
    for i in model.I:
        row = {"HexID": int(i)}
        for c in model.C_pub:
            row[f"{c}_chargers"] = sv(model.x[i, c])
            row[f"{c}_footprint"] = data["charger_footprint"][str(c)] * sv(model.x[i, c])
            row[f"{c}_capacity_kWh_slot"] = data["charger_capacity_pub"][str(c)] * sv(model.x[i, c])
        row["PV_panels"] = sv(model.PV[i])
        row["Battery_units"] = sv(model.Batt[i])
        row["Total_charger_footprint"] = sum(data["charger_footprint"][str(c)] * sv(model.x[i, c]) for c in model.C_pub)
        row["Total_public_capacity_kWh_slot"] = sum(data["charger_capacity_pub"][str(c)] * sv(model.x[i, c]) for c in model.C_pub)
        rows.append(row)
    df = pd.DataFrame(rows).sort_values("HexID")
    df.to_csv(results_dir / "infrastructure_by_hex.csv", index=False)
    return df


def export_energy_by_charger_type_stage4(model, data: dict, redir_rows: list[dict[str, Any]], results_dir: Path) -> pd.DataFrame:
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


def export_hourly_energy_stage4(model, data: dict, redir_rows: list[dict[str, Any]], results_dir: Path) -> pd.DataFrame:
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
                    "Grid_batt_kWh_day": sv(model.grid_batt[i, mon, t]),
                    "PV_direct_kWh_day": sv(model.pv_dir[i, mon, t]),
                    "PV_batt_kWh_day": sv(model.pv_batt[i, mon, t]),
                    "Batt_discharge_kWh_day": sv(model.batt_discharge[i, mon, t]),
                    "SOC_start_kWh": sv(model.soc[i, mon, t - 1]),
                    "SOC_end_kWh": sv(model.soc[i, mon, t]),
                }
                for c in model.C_pub:
                    row[f"E_{c}_home_kWh_day"] = sv(model.e_home[i, mon, t, c])
                    row[f"E_{c}_public_kWh_day"] = sv(model.q[i, mon, t, c]) - sv(model.R[i, mon, t, c]) + incoming.get((int(i), mon, int(t), str(c)), 0.0)
                rows.append(row)
    df = pd.DataFrame(rows)
    df.to_csv(results_dir / "hourly_energy.csv", index=False)
    return df


def export_slack_stage4(model, data: dict, results_dir: Path) -> pd.DataFrame:
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


def export_master_solution_stage4(model, results_dir: Path) -> pd.DataFrame:
    rows = []
    for i in model.I:
        for c in model.C_pub:
            rows.append({"variable": "x", "HexID": int(i), "Month": "", "TimeIndex": "", "Type": str(c), "Value": sv(model.x[i, c])})
        rows.append({"variable": "PV", "HexID": int(i), "Month": "", "TimeIndex": "", "Type": "PV", "Value": sv(model.PV[i])})
        rows.append({"variable": "Batt", "HexID": int(i), "Month": "", "TimeIndex": "", "Type": "Batt", "Value": sv(model.Batt[i])})
    df = pd.DataFrame(rows)
    df.to_csv(results_dir / "lbbd_master_solution.csv", index=False)
    return df


def export_stage4_all(model, data: dict, cfg: dict, run_dir: Path, redir_rows: list[dict[str, Any]], history_df: pd.DataFrame, sp_df: pd.DataFrame, cuts_df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    results_dir = run_dir / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    metrics = compute_stage4_metrics(model, data, cfg, redir_rows)
    frames = {
        "model_summary": export_model_summary(metrics, results_dir),
        "infrastructure_by_hex": export_infrastructure_stage4(model, data, results_dir),
        "energy_by_type": export_energy_by_charger_type_stage4(model, data, redir_rows, results_dir),
        "origin_type_q": export_origin_type_allocation(model, data, results_dir),
        "hourly_energy": export_hourly_energy_stage4(model, data, redir_rows, results_dir),
        "slack": export_slack_stage4(model, data, results_dir),
        "lbbd_master_solution": export_master_solution_stage4(model, results_dir),
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
    sp_df.to_csv(run_dir / "subproblems" / "lbbd_subproblem_summary.csv", index=False)
    cuts_df.to_csv(results_dir / "lbbd_cuts.csv", index=False)
    cuts_df.to_csv(run_dir / "iterations" / "lbbd_cuts.csv", index=False)
    notes = pd.DataFrame([
        {"Metric": "stage", "Value": "4_PV_BESS_master_with_MIP_trip_bundle_redirection_subproblem"},
        {"Metric": "bound_note", "Value": "UB is continuous-redirection LP relaxation with PV+BESS master; LB is feasible MIP trip-bundle reconstruction."},
        {"Metric": "BESS_note", "Value": "BESS sizing, charge/discharge exclusivity, and 12-month linked SoC are retained in the master. Redirected demand is conservatively costed as grid-supplied in the redirection subproblem."},
    ])
    notes.to_csv(results_dir / "model_summary_stage4_notes.csv", index=False)
    frames["stage4_notes"] = notes
    xlsx = write_combined_xlsx(results_dir, frames)
    if xlsx:
        print(f"Combined XLSX written to: {xlsx}")
    return frames
