from __future__ import annotations

from collections import defaultdict
import math
import networkx as nx
import numpy as np
import pandas as pd

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]
M_ABBR = {
    "January": "Jan", "February": "Feb", "March": "Mar", "April": "Apr",
    "May": "May", "June": "Jun", "July": "Jul", "August": "Aug",
    "September": "Sep", "October": "Oct", "November": "Nov", "December": "Dec",
}
MONTH_NUM_TO_NAME = {i + 1: m for i, m in enumerate(MONTHS)}
N_MONTH = {
    "January": 31, "February": 28, "March": 31, "April": 30,
    "May": 31, "June": 30, "July": 31, "August": 31,
    "September": 30, "October": 31, "November": 30, "December": 31,
}
INTERVALS = list(range(1, 49))
HSOC = list(range(0, 49))
DAYS = sum(N_MONTH.values())
PUB_TYPES = ["slow", "medium", "fast"]
DEMAND_CLASSES = ["home", "public"]


def retail_price_from_ore(p_ore: float, cfg: dict) -> float:
    p_sek = float(p_ore) / 100.0
    return (
        p_sek
        + cfg["electricity_tax_sek_per_kwh"]
        + cfg["grid_fee_sek_per_kwh"]
        + cfg["retail_markup_sek_per_kwh"]
    ) * (1.0 + cfg["vat"])


def build_tou(spot_df: pd.DataFrame, cfg: dict) -> dict:
    return {
        m: {t: retail_price_from_ore(spot_df.at[(t - 1) // 2, M_ABBR[m]], cfg) for t in INTERVALS}
        for m in MONTHS
    }


def pvf_daily(r: float, n: int) -> float:
    return (r * (1 + r) ** n) / ((1 + r) ** n - 1) / 365.0


def build_daily_costs(cfg: dict) -> dict:
    out = {}
    r = float(cfg["discount_rate"])
    for asset, spec in cfg["asset_specs"].items():
        capex = float(spec["capex_sek"])
        life = int(spec["life_years"])
        om = float(spec.get("fixed_om_fraction", 0.0))
        out[asset] = round(capex * pvf_daily(r, life) + capex * om / 365.0, 4)
    return out


def build_pvgis_monthly_hourly_cf(pvgis_df: pd.DataFrame, cfg: dict):
    power_col = cfg["pvgis_power_col"]
    required_cols = {"year", "month", "date", "hour", power_col}
    missing = required_cols - set(pvgis_df.columns)
    if missing:
        raise ValueError(f"PVGIS file is missing required columns: {missing}")

    df = pvgis_df.copy()
    df["month"] = df["month"].astype(int)
    df["hour"] = df["hour"].astype(int)
    df[power_col] = pd.to_numeric(df[power_col], errors="coerce").fillna(0.0)
    if df["hour"].min() < 0 or df["hour"].max() > 23:
        raise ValueError("PVGIS hour column must be in the range 0,...,23.")

    panel_rated_w = float(cfg["panel_kw"]) * 1000.0
    monthly_hourly_power_w = (
        df.groupby(["month", "hour"], as_index=False)[power_col]
        .mean()
        .rename(columns={power_col: "avg_power_w"})
    )
    full_idx = pd.MultiIndex.from_product([range(1, 13), range(0, 24)], names=["month", "hour"])
    monthly_hourly_power_w = (
        monthly_hourly_power_w.set_index(["month", "hour"])
        .reindex(full_idx, fill_value=0.0)
        .reset_index()
    )
    monthly_hourly_power_w["cf"] = (monthly_hourly_power_w["avg_power_w"] / panel_rated_w).clip(0.0, 1.0)
    cf_lookup = {
        (MONTH_NUM_TO_NAME[int(r.month)], int(r.hour)): float(r.cf)
        for r in monthly_hourly_power_w.itertuples(index=False)
    }
    pv_cf = {mon: {t: cf_lookup[(mon, (t - 1) // 2)] for t in INTERVALS} for mon in MONTHS}

    pv_diag = (
        df.groupby("month")
        .agg(total_kwh_per_panel=(power_col, lambda x: x.sum() / 1000.0), n_days=("date", "nunique"))
        .reset_index()
    )
    pv_diag["month_name"] = pv_diag["month"].map(MONTH_NUM_TO_NAME)
    pv_diag["avg_kwh_per_panel_day"] = pv_diag["total_kwh_per_panel"] / pv_diag["n_days"]
    return pv_cf, pv_diag


def get_distance_dict(dist_df: pd.DataFrame) -> dict:
    df = dist_df.copy()
    df["distance_km"] = df["distance"] / 1000.0
    return {(int(r.from_HexID), int(r.to_HexID)): round(float(r.distance_km), 4) for _, r in df.iterrows()}


def preprocess(raw: dict, cfg: dict) -> dict:
    gdf = raw["gdf"].copy()
    parking_gdf = raw["parking_gdf"].copy()
    dist_df = raw["dist_df"].copy()
    spot_df = raw["spot_df"].copy()
    pvgis_df = raw["pvgis_df"].copy()

    gdf["HexID"] = gdf["HexID"].astype(int)
    gdf["charType"] = gdf["charType"].astype(str).str.lower().str.strip()
    hex_ids = sorted(gdf["HexID"].unique())
    time_indices = sorted(gdf["TimeIndex"].astype(int).unique())

    parking_gdf["HexID"] = parking_gdf["HexID"].astype(int)
    parking_gdf["ParkingCap"] = parking_gdf["ParkingCap"]/2.0 + int(cfg["parking_capacity_add"])
    parking_gdf["homeChar"] = parking_gdf["homeChar"] + int(cfg["home_charger_add"])

    cl = parking_gdf.set_index("HexID")["ParkingCap"].to_dict()
    home_avail = parking_gdf.set_index("HexID")["homeChar"].to_dict()
    for i in hex_ids:
        cl.setdefault(int(i), 0)
        home_avail.setdefault(int(i), 0)

    charger_capacity = cfg["charger_capacity_kwh_per_slot"]
    charger_capacity_pub = {c: float(charger_capacity[c]) for c in PUB_TYPES}
    charger_price = {c: float(cfg["charger_price_sek_per_kwh"][c]) for c in PUB_TYPES}
    charger_footprint = {c: float(cfg["charger_footprint"][c]) for c in PUB_TYPES}
    eligible = {"home": PUB_TYPES[:], "public": PUB_TYPES[:]}
    delta_price = {(co, cd): max(0.0, charger_price[cd] - charger_price[co]) for co in PUB_TYPES for cd in PUB_TYPES}

    daily_cost = build_daily_costs(cfg)
    tou = build_tou(spot_df, cfg)
    pv_cf, pv_diag = build_pvgis_monthly_hourly_cf(pvgis_df, cfg)
    dist_dict = get_distance_dict(dist_df)
    hex_id_set = set(int(i) for i in hex_ids)

    # Keep only distance arcs whose origin and destination both exist
    # in the selected demand/parking dataset.
    allowed = {
        (int(i), int(j))
        for (i, j), d in dist_dict.items()
        if (
            int(i) in hex_id_set
            and int(j) in hex_id_set
            and int(i) != int(j)
            and float(d) <= float(cfg["max_redirection_distance_km"])
        )
    }
    beta = float(cfg["value_time_sek_per_h"]) * (1.0 / float(cfg["speed_car_kmh"]) + 2.0 / float(cfg["speed_walk_kmh"]))
    t_dict = {(i, j): beta * dist_dict[(i, j)] for (i, j) in allowed}

    grp = (
        gdf[["HexID", "TimeIndex", "Demand", "charType"]]
        .groupby(["HexID", "TimeIndex", "charType"])["Demand"]
        .sum()
        .reset_index()
    )
    d_home = {(i, t): 0.0 for i in hex_ids for t in time_indices}
    d_work = {(i, t): 0.0 for i in hex_ids for t in time_indices}
    d_pub = {(i, t): 0.0 for i in hex_ids for t in time_indices}
    for _, r in grp.iterrows():
        i, t, et = int(r.HexID), int(r.TimeIndex), float(r.Demand)
        if r.charType == "home":
            d_home[(i, t)] += et
        elif r.charType == "work":
            d_work[(i, t)] += et
        else:
            d_pub[(i, t)] += et

    home_kwh_per_slot = float(charger_capacity["home"])
    for i in hex_ids:
        cap_i = float(home_avail[i]) * home_kwh_per_slot
        for t in time_indices:
            d_home[(i, t)] = max(d_home[(i, t)] - cap_i, 0.0)

    demand_event = {}
    for i in hex_ids:
        for t in time_indices:
            demand_event[(i, t, "home")] = d_home[(i, t)]
            demand_event[(i, t, "public")] = d_work[(i, t)] + d_pub[(i, t)]

    demand_event_annual = {
        (i, m, t, e): demand_event[(i, t, e)]
        for i in hex_ids for m in MONTHS for t in INTERVALS for e in DEMAND_CLASSES
    }

    def arc_active(i: int, j: int, t: int) -> bool:
        return (
            demand_event.get((int(i), int(t), "public"), 0.0)
            + demand_event.get((int(j), int(t), "public"), 0.0)
        ) > float(cfg["arc_activity_threshold_kwh"])


    allowed_st = {
        (int(i), int(j), m, int(t))
        for (i, j) in allowed
        for m in MONTHS
        for t in INTERVALS
        if arc_active(i, j, t)
    }

    g = nx.Graph()
    g.add_nodes_from(hex_ids)
    g.add_edges_from(allowed)
    pub_demand = {i: sum(demand_event[(i, t, "public")] for t in time_indices) for i in hex_ids}
    for comp in nx.connected_components(g):
        if any(pub_demand[i] > 0 for i in comp) and all(cl[i] == 0 for i in comp):
            i_star = max(comp, key=lambda i: pub_demand[i])
            cl[i_star] = 2

    if "Panels" not in parking_gdf.columns:
        raise KeyError("Parking shapefile must contain a 'Panels' column for PV upper bounds.")
    pv_upper = parking_gdf.set_index("HexID")["Panels"].to_dict()
    for i in hex_ids:
        pv_upper.setdefault(int(i), 0)

    out = defaultdict(list)
    incoming = defaultdict(list)
    for (i, j, mon, t) in allowed_st:
        out[(i, mon, t)].append(j)
        incoming[(j, mon, t)].append(i)
    origin_st = sorted(out.keys())
    dest_st = sorted(incoming.keys())

    prev_month = {MONTHS[i]: MONTHS[i - 1] if i > 0 else MONTHS[-1] for i in range(len(MONTHS))}
    k_batt = float(cfg["battery_cell_cap_kwh"]) / (float(cfg["battery_duration_h"]) * float(cfg["rho_half_hours_per_hour"]))
    m_batt = {int(i): k_batt * int(cfg["battery_max_units_per_hex"]) for i in hex_ids}
    max_k_per_footprint = max(charger_capacity_pub[c] / charger_footprint[c] for c in PUB_TYPES)
    m_redir = {int(j): float(max_k_per_footprint * cl[int(j)]) for j in hex_ids}

    return {
        "MONTHS": MONTHS,
        "N_MONTH": N_MONTH,
        "DAYS": DAYS,
        "INTERVALS": INTERVALS,
        "HSOC": HSOC,
        "PUB_TYPES": PUB_TYPES,
        "DEMAND_CLASSES": DEMAND_CLASSES,
        "hex_ids": hex_ids,
        "time_indices": time_indices,
        "cl": cl,
        "home_avail": home_avail,
        "demand_event": demand_event,
        "demand_event_annual": demand_event_annual,
        "allowed": sorted(allowed),
        "allowed_st": sorted(allowed_st),
        "ORIGIN_ST": origin_st,
        "DEST_ST": dest_st,
        "OUT": out,
        "IN": incoming,
        "dist_dict": dist_dict,
        "T_dict": t_dict,
        "beta": beta,
        "tou": tou,
        "pv_cf": pv_cf,
        "pv_diag": pv_diag,
        "pv_upper": pv_upper,
        "daily_cost": daily_cost,
        "charger_capacity_pub": charger_capacity_pub,
        "charger_capacity": charger_capacity,
        "charger_price": charger_price,
        "charger_footprint": charger_footprint,
        "delta_price": delta_price,
        "eligible": eligible,
        "prev_month": prev_month,
        "pv_kwh_per_panel_slot_at_cf1": float(cfg["panel_kw"]) * float(cfg["slot_hours"]),
        "K_BATT": k_batt,
        "M_BATT": m_batt,
        "M_REDIR": m_redir,
    }
