#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import math
import traceback
from pathlib import Path
from typing import Callable

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import FancyArrowPatch, Patch
import numpy as np
import pandas as pd

MONTHS = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December",
]
MONTH_DAYS = {
    "January": 31, "February": 28, "March": 31, "April": 30,
    "May": 31, "June": 30, "July": 31, "August": 31,
    "September": 30, "October": 31, "November": 30, "December": 31,
}
REPRESENTATIVE_MONTHS = ["January", "April", "July", "October"]


def _read_csv(path: Path, required: bool = False) -> pd.DataFrame:
    if not path.exists():
        if required:
            raise FileNotFoundError(path)
        return pd.DataFrame()
    try:
        return pd.read_csv(path)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()


def _numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def _summary_dict(results_dir: Path) -> dict[str, object]:
    df = _read_csv(results_dir / "model_summary.csv", required=True)
    if not {"Metric", "Value"}.issubset(df.columns):
        raise ValueError("model_summary.csv must contain Metric and Value columns")
    result: dict[str, object] = {}
    for _, row in df.iterrows():
        key = str(row["Metric"])
        value = row["Value"]
        try:
            result[key] = float(value)
        except (TypeError, ValueError):
            result[key] = value
    return result


def _infer_dataset(run_dir: Path) -> str | None:
    manifest = run_dir / "logs" / "lbbd_manifest.json"
    if manifest.exists():
        try:
            value = json.loads(manifest.read_text(encoding="utf-8")).get("dataset")
            if value in {"small", "full"}:
                return value
        except Exception:
            pass
    for value in ("small", "full"):
        if f"_{value}_" in run_dir.name.lower():
            return value
    try:
        value = _summary_dict(run_dir / "results").get("dataset")
        if str(value) in {"small", "full"}:
            return str(value)
    except Exception:
        pass
    return None


def _resolve_geometry(project_root: Path, dataset: str | None, parking_shapefile: str | None) -> Path | None:
    if parking_shapefile:
        path = Path(parking_shapefile)
        return path if path.is_absolute() else (project_root / path).resolve()
    if dataset is None:
        return None
    cfg_path = project_root / "config" / "paths.json"
    if not cfg_path.exists():
        return None
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    raw = cfg.get("datasets", {}).get(dataset, {}).get("parking_shapefile")
    if not raw:
        return None
    return (project_root / raw).resolve()


def _setup_style() -> None:
    plt.rcParams.update({
        "font.size": 11,
        "axes.titlesize": 14,
        "axes.labelsize": 12,
        "legend.fontsize": 9,
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "figure.autolayout": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "grid.linestyle": "--",
    })


def _boxed_legend_below(fig: plt.Figure, handles, labels, ncol: int, bottom: float = 0.20) -> None:
    if not handles:
        return
    fig.legend(
        handles,
        labels,
        loc="lower center",
        bbox_to_anchor=(0.5, 0.015),
        ncol=max(1, int(ncol)),
        frameon=True,
        fancybox=True,
        framealpha=0.96,
        edgecolor="0.65",
        columnspacing=1.4,
        handlelength=2.4,
    )
    fig.subplots_adjust(bottom=bottom)


def _sem(series: pd.Series) -> float:
    values = _numeric(series).dropna()
    if len(values) <= 1:
        return 0.0
    return float(values.std(ddof=1) / math.sqrt(len(values)))


def _add_basemap(ax: plt.Axes, alpha: float = 0.30) -> bool:
    """Add a faint CartoDB basemap when contextily and internet access are available."""
    try:
        import contextily as ctx
        xlim, ylim = ax.get_xlim(), ax.get_ylim()
        ctx.add_basemap(
            ax,
            source=ctx.providers.CartoDB.PositronNoLabels,
            crs="EPSG:3857",
            alpha=float(alpha),
            reset_extent=False,
            attribution_size=6,
        )
        ax.set_xlim(xlim)
        ax.set_ylim(ylim)
        return True
    except Exception as exc:
        print(f"WARNING: Basemap unavailable; map generated with vector layers only ({exc})")
        return False


def _save(fig: plt.Figure, figures_dir: Path, stem: str, dpi: int) -> list[str]:
    figures_dir.mkdir(parents=True, exist_ok=True)
    png = figures_dir / f"{stem}.png"
    fig.savefig(png, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    return [png.name]


def _hour_axis(ax: plt.Axes) -> None:
    slots = np.arange(1, 49)
    ticks = np.arange(1, 49, 4)
    labels = [f"{(t - 1) / 2:.0f}:00" for t in ticks]
    ax.set_xlim(1, 48)
    ax.set_xticks(ticks)
    ax.set_xticklabels(labels)
    ax.set_xlabel("Time of representative day")


def _plot_economic_breakdown(results_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    metrics = _summary_dict(results_dir)
    types = ["slow", "medium", "fast"]
    type_colors = {"slow": "#4C78A8", "medium": "#F58518", "fast": "#54A24B"}
    component_colors = {
        "grid_direct": "#E45756",
        "grid_battery": "#B279A2",
        "distance": "#9D755D",
        "compensation": "#FF9DA6",
        "slack": "#BAB0AC",
        "pv": "#ECA82C",
        "bess": "#72B7B2",
    }

    revenue_by_type = {c: float(metrics.get(f"revenue_{c}_SEK", 0.0) or 0.0) / 1e6 for c in types}
    charger_capex_by_type = {c: float(metrics.get(f"capex_chargers_{c}_SEK", 0.0) or 0.0) / 1e6 for c in types}

    # Backward-compatible fallback for run folders exported before the detailed metrics were added.
    if sum(revenue_by_type.values()) <= 0:
        energies = np.array([float(metrics.get(f"energy_{c}_kWh", 0.0) or 0.0) for c in types])
        shares = energies / energies.sum() if energies.sum() > 0 else np.array([1.0, 0.0, 0.0])
        total = float(metrics.get("revenue_all_chargers_SEK", 0.0) or 0.0) / 1e6
        revenue_by_type = {c: total * shares[k] for k, c in enumerate(types)}
    if sum(charger_capex_by_type.values()) <= 0:
        counts = np.array([float(metrics.get(f"chargers_{c}_installed", 0.0) or 0.0) for c in types])
        shares = counts / counts.sum() if counts.sum() > 0 else np.array([1.0, 0.0, 0.0])
        total = float(metrics.get("capex_chargers_SEK", 0.0) or 0.0) / 1e6
        charger_capex_by_type = {c: total * shares[k] for k, c in enumerate(types)}

    grid_direct = float(metrics.get("grid_direct_cost_SEK", metrics.get("grid_cost_SEK", 0.0)) or 0.0) / 1e6
    grid_battery = float(metrics.get("grid_to_battery_cost_SEK", 0.0) or 0.0) / 1e6
    if grid_direct + grid_battery > 0 and "grid_direct_cost_SEK" not in metrics:
        grid_direct = float(metrics.get("grid_cost_SEK", 0.0) or 0.0) / 1e6
        grid_battery = 0.0

    rows = [
        ("Charging revenue", [(revenue_by_type[c], type_colors[c], c.capitalize()) for c in types]),
        ("Grid electricity", [(-grid_direct, component_colors["grid_direct"], "Grid direct"), (-grid_battery, component_colors["grid_battery"], "Grid to BESS")]),
        ("Redirection cost", [(-float(metrics.get("redirection_distance_cost_SEK", 0.0) or 0.0) / 1e6, component_colors["distance"], "Distance incentive"), (-float(metrics.get("redirection_price_compensation_SEK", 0.0) or 0.0) / 1e6, component_colors["compensation"], "Type compensation")]),
        ("Slack penalty", [(-float(metrics.get("slack_penalty_SEK", 0.0) or 0.0) / 1e6, component_colors["slack"], "Slack penalty")]),
        ("Charger capex", [(-charger_capex_by_type[c], type_colors[c], c.capitalize()) for c in types]),
        ("PV and BESS capex", [(-float(metrics.get("capex_PV_SEK", metrics.get("capex_PV_BESS_SEK", 0.0)) or 0.0) / 1e6, component_colors["pv"], "PV"), (-float(metrics.get("capex_BESS_SEK", 0.0) or 0.0) / 1e6, component_colors["bess"], "BESS")]),
    ]

    fig, ax = plt.subplots(figsize=(13.6, 7.0))
    y = np.arange(len(rows))
    totals = []
    for row_index, (_, segments) in enumerate(rows):
        left_positive = 0.0
        left_negative = 0.0
        total = 0.0
        for value, color, _ in segments:
            if abs(value) <= 1e-12:
                continue
            left = left_positive if value >= 0 else left_negative
            ax.barh(row_index, value, left=left, color=color, edgecolor="white", linewidth=0.5, height=0.68, zorder=3)
            if value >= 0:
                left_positive += value
            else:
                left_negative += value
            total += value
        totals.append(total)

    max_positive = max([v for v in totals if v > 0] + [1.0])
    min_negative = min([v for v in totals if v < 0] + [-1.0])
    span = max_positive - min_negative
    ax.set_xlim(min_negative - 0.07 * span, max_positive + 0.07 * span)
    label_pad = 0.012 * span
    for row_index, total in enumerate(totals):
        if total >= 0:
            ax.text(total + label_pad, row_index, f"{total:,.3f}", va="center", ha="left", fontweight="bold", clip_on=False)
        else:
            ax.text(total - label_pad, row_index, f"{total:,.3f}", va="center", ha="right", fontweight="bold", clip_on=False)

    ax.axvline(0, color="0.25", linewidth=0.9, zorder=4)
    ax.set_yticks(y)
    ax.set_yticklabels([row[0] for row in rows])
    ax.invert_yaxis()
    ax.set_xlabel("Annual cash flow (million SEK/year)")
    ax.set_title("Annual CPO objective composition")
    ax.grid(axis="x", alpha=0.28)
    ax.grid(axis="y", visible=False)

    profit = float(metrics.get("annual_profit_SEK", 0.0) or 0.0) / 1e6
    ax.text(0.985, 0.025, f"Net profit: {profit:,.3f} MSEK/year", transform=ax.transAxes,
            ha="right", va="bottom", bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.92, "edgecolor": "0.45"})

    counts = {c: int(round(float(metrics.get(f"chargers_{c}_installed", 0.0) or 0.0))) for c in types}
    pv_units = int(round(float(metrics.get("PV_panels_installed", 0.0) or 0.0)))
    bess_units = int(round(float(metrics.get("battery_units_installed", 0.0) or 0.0)))
    trip_eq = float(metrics.get("redirection_trip_equivalents_annual", 0.0) or 0.0)
    if trip_eq <= 0:
        redirected = float(metrics.get("energy_redirected_kWh", 0.0) or 0.0)
        trip_eq = redirected / 20.0 if redirected > 0 else 0.0

    legend_handles = [
        Patch(facecolor=type_colors["slow"], label=f"Slow: {counts['slow']:,} chargers"),
        Patch(facecolor=type_colors["medium"], label=f"Medium: {counts['medium']:,} chargers"),
        Patch(facecolor=type_colors["fast"], label=f"Fast: {counts['fast']:,} chargers"),
        Patch(facecolor=component_colors["pv"], label=f"PV: {pv_units:,} panels"),
        Patch(facecolor=component_colors["bess"], label=f"BESS: {bess_units:,} units"),
        Patch(facecolor=component_colors["grid_direct"], label="Grid direct"),
        Patch(facecolor=component_colors["grid_battery"], label="Grid to BESS"),
        Patch(facecolor=component_colors["distance"], label="Distance incentive"),
        Patch(facecolor=component_colors["compensation"], label="Type compensation"),
        Line2D([], [], color="none", label=f"Redirected: {trip_eq:,.0f} trip-equivalents/year"),
    ]
    fig.legend(
        handles=legend_handles,
        loc="upper right",
        bbox_to_anchor=(0.99, 0.90),
        ncol=1,
        frameon=True,
        fancybox=True,
        framealpha=0.96,
        edgecolor="0.65",
        title="Optimized deployment and flows",
    )
    fig.subplots_adjust(left=0.18, right=0.73, bottom=0.12, top=0.90)
    return _save(fig, figures_dir, "01_economic_breakdown", dpi)


def _plot_charger_deployment(results_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    df = _read_csv(results_dir / "energy_by_charger_type.csv", required=True)
    if df.empty:
        raise ValueError("energy_by_charger_type.csv is empty")
    all_rows = df[df["DemandClass"].astype(str).str.upper() == "ALL"].copy()
    all_rows["InstalledChargers"] = _numeric(all_rows["InstalledChargers"]).fillna(0)
    all_rows["CapacityRatio_all_classes"] = _numeric(all_rows["CapacityRatio_all_classes"]).fillna(0)
    all_rows = all_rows.set_index("ChargerType").reindex(["slow", "medium", "fast"]).fillna(0).reset_index()
    x = np.arange(len(all_rows))
    colors = ["#4C78A8", "#4C78A8", "#4C78A8"]
    fig, ax = plt.subplots(figsize=(8.8, 5.7))
    bars = ax.bar(x, all_rows["InstalledChargers"].to_numpy(), color=colors, alpha=0.88, zorder=2)
    ax.set_xticks(x)
    ax.set_xticklabels([str(v).capitalize() for v in all_rows["ChargerType"]])
    ax.set_ylabel("Installed public chargers")
    ax.set_title("Public charger deployment and annual utilization")
    ax.set_axisbelow(True)
    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{bar.get_height():,.0f}", ha="center", va="bottom", zorder=5)

    ax2 = ax.twinx()
    utilization = 100 * all_rows["CapacityRatio_all_classes"].to_numpy()
    line, = ax2.plot(
        x,
        utilization,
        marker="o",
        linewidth=2.8,
        markersize=7,
        color="#F58518",
        markerfacecolor="#F58518",
        markeredgecolor="white",
        markeredgewidth=0.8,
        label="Capacity utilization",
        zorder=6,
    )
    ax2.set_ylabel("Annual capacity utilization (%)")
    ax2.set_ylim(0, max(55.0, 1.15 * float(np.max(utilization)) if len(utilization) else 55.0))
    ax2.grid(False)
    ax2.legend(handles=[line], loc="upper left", bbox_to_anchor=(0.015, 0.985), frameon=True, framealpha=0.94, edgecolor="0.65")
    fig.subplots_adjust(left=0.12, right=0.88, bottom=0.14, top=0.88)
    return _save(fig, figures_dir, "02_charger_deployment_and_utilization", dpi)


def _prepare_hourly(results_dir: Path) -> pd.DataFrame:
    df = _read_csv(results_dir / "hourly_energy.csv", required=True)
    if df.empty:
        raise ValueError("hourly_energy.csv is empty")
    df["Month"] = pd.Categorical(df["Month"], categories=MONTHS, ordered=True)
    numeric_cols = [c for c in df.columns if c not in {"HexID", "Month", "TimeIndex"}]
    for col in numeric_cols:
        df[col] = _numeric(df[col]).fillna(0.0)
    return df


def _served_columns(df: pd.DataFrame) -> list[str]:
    return [c for c in df.columns if c.startswith("E_") and c.endswith("_kWh_day")]


def _plot_monthly_energy(results_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    df = _prepare_hourly(results_dir)
    grouped = df.groupby("Month", observed=False)[[
        "Grid_direct_kWh_day", "PV_direct_kWh_day", "Batt_discharge_kWh_day",
        "Grid_batt_kWh_day", "PV_batt_kWh_day",
    ]].sum().reindex(MONTHS).fillna(0.0)
    for month in MONTHS:
        grouped.loc[month] *= MONTH_DAYS[month]
    x = np.arange(12)
    fig, ax = plt.subplots(figsize=(11, 6.4))
    bottom = np.zeros(12)
    for col, label in [
        ("Grid_direct_kWh_day", "Grid to chargers"),
        ("PV_direct_kWh_day", "PV to chargers"),
        ("Batt_discharge_kWh_day", "BESS to chargers"),
    ]:
        vals = grouped[col].to_numpy() / 1e6
        ax.bar(x, vals, bottom=bottom, label=label)
        bottom += vals
    ax.set_xticks(x)
    ax.set_xticklabels([m[:3] for m in MONTHS])
    ax.set_ylabel("Energy supplied (GWh/month)")
    ax.set_title("Monthly charging-energy supply mix")
    handles, labels = ax.get_legend_handles_labels()
    if ax.get_legend() is not None:
        ax.get_legend().remove()
    _boxed_legend_below(fig, handles, labels, ncol=3, bottom=0.20)
    return _save(fig, figures_dir, "03_monthly_energy_supply_mix", dpi)


def _plot_dispatch_month(df: pd.DataFrame, month: str, figures_dir: Path, dpi: int) -> list[str]:
    sub = df[df["Month"].astype(str) == month]
    if sub.empty:
        raise ValueError(f"No hourly rows for {month}")
    cols = ["Grid_direct_kWh_day", "PV_direct_kWh_day", "Batt_discharge_kWh_day"]
    agg = sub.groupby("TimeIndex")[cols].sum().reindex(range(1, 49), fill_value=0.0)
    served_cols = _served_columns(sub)
    served = sub.groupby("TimeIndex")[served_cols].sum().sum(axis=1).reindex(range(1, 49), fill_value=0.0) if served_cols else agg.sum(axis=1)
    x = np.arange(1, 49)
    fig, ax = plt.subplots(figsize=(10.8, 6.1))
    ax.stackplot(x, agg[cols[0]], agg[cols[1]], agg[cols[2]], labels=["Grid", "Direct PV", "BESS discharge"], alpha=0.85)
    ax.plot(x, served.to_numpy(), linewidth=1.8, label="Energy served")
    _hour_axis(ax)
    ax.set_ylabel("Energy (kWh per 30-minute slot)")
    ax.set_title(f"{month}: aggregate charging-energy dispatch")
    handles, labels = ax.get_legend_handles_labels()
    if ax.get_legend() is not None:
        ax.get_legend().remove()
    _boxed_legend_below(fig, handles, labels, ncol=4, bottom=0.21)
    return _save(fig, figures_dir, f"04_dispatch_{month.lower()}", dpi)


def _plot_soc_by_month(results_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    hourly = _prepare_hourly(results_dir)
    infra = _read_csv(results_dir / "infrastructure_by_hex.csv", required=True)
    if "Battery_units" not in infra.columns:
        raise ValueError("Battery_units is missing from infrastructure_by_hex.csv")
    infra["Battery_units"] = _numeric(infra["Battery_units"]).fillna(0.0)
    hourly = hourly.merge(infra[["HexID", "Battery_units"]], on="HexID", how="left")
    hourly = hourly[hourly["Battery_units"] > 0].copy()
    if hourly.empty:
        raise ValueError("No installed BESS units")
    hourly["SOC_per_unit_kWh"] = hourly["SOC_end_kWh"] / hourly["Battery_units"]
    pivot = hourly.groupby(["TimeIndex", "Month"], observed=False)["SOC_per_unit_kWh"].mean().unstack("Month").reindex(index=range(1, 49), columns=MONTHS)
    fig, ax = plt.subplots(figsize=(11, 6.8))
    for month in MONTHS:
        if month in pivot and pivot[month].notna().any():
            ax.plot(pivot.index, pivot[month], linewidth=1.25, label=month[:3])
    _hour_axis(ax)
    ax.set_ylabel("Mean BESS state of charge (kWh per installed unit)")
    ax.set_title("Mean BESS state of charge by representative month")
    handles, labels = ax.get_legend_handles_labels()
    if ax.get_legend() is not None:
        ax.get_legend().remove()
    _boxed_legend_below(fig, handles, labels, ncol=6, bottom=0.24)
    return _save(fig, figures_dir, "05_bess_soc_by_month", dpi)


def _plot_battery_operation_month(df: pd.DataFrame, month: str, figures_dir: Path, dpi: int, results_dir: Path | None = None) -> list[str]:
    sub = df[df["Month"].astype(str) == month].copy()
    if sub.empty:
        raise ValueError(f"No hourly rows for {month}")
    if results_dir is None:
        raise ValueError("Results directory is required for BESS-unit normalization")
    infra = _read_csv(results_dir / "infrastructure_by_hex.csv", required=True)
    if "Battery_units" not in infra.columns:
        raise ValueError("Battery_units is missing from infrastructure_by_hex.csv")
    infra = infra[["HexID", "Battery_units"]].copy()
    infra["Battery_units"] = _numeric(infra["Battery_units"]).fillna(0.0)
    sub = sub.merge(infra, on="HexID", how="left")
    sub = sub[sub["Battery_units"] > 0].copy()
    if sub.empty:
        raise ValueError(f"No installed BESS units in {month}")

    sub["PV_charge_per_unit"] = sub["PV_batt_kWh_day"] / sub["Battery_units"]
    sub["Grid_charge_per_unit"] = sub["Grid_batt_kWh_day"] / sub["Battery_units"]
    sub["Discharge_per_unit"] = sub["Batt_discharge_kWh_day"] / sub["Battery_units"]
    sub["SOC_per_unit"] = sub["SOC_end_kWh"] / sub["Battery_units"]

    grp = sub.groupby("TimeIndex")
    stats = pd.DataFrame({
        "mean_pv": grp["PV_charge_per_unit"].mean(),
        "sem_pv": grp["PV_charge_per_unit"].apply(_sem),
        "mean_grid": grp["Grid_charge_per_unit"].mean(),
        "sem_grid": grp["Grid_charge_per_unit"].apply(_sem),
        "mean_discharge": grp["Discharge_per_unit"].mean(),
        "sem_discharge": grp["Discharge_per_unit"].apply(_sem),
        "mean_soc": grp["SOC_per_unit"].mean(),
        "sem_soc": grp["SOC_per_unit"].apply(_sem),
    }).reindex(range(1, 49), fill_value=0.0)
    if float(stats[["mean_pv", "mean_grid", "mean_discharge"]].to_numpy().sum()) <= 1e-9:
        raise ValueError(f"No BESS operation in {month}")

    x = stats.index.to_numpy(dtype=float)
    fig, ax1 = plt.subplots(figsize=(11.5, 7.4))
    ax2 = ax1.twinx()
    ax1.bar(x, stats["mean_pv"], yerr=stats["sem_pv"], label="PV charge per BESS unit", alpha=0.82, capsize=2.5)
    ax1.bar(x, stats["mean_grid"], bottom=stats["mean_pv"], yerr=stats["sem_grid"], label="Grid charge per BESS unit", alpha=0.82, capsize=2.5)
    ax1.bar(x, -stats["mean_discharge"], yerr=stats["sem_discharge"], label="Discharge per BESS unit", alpha=0.82, capsize=2.5)

    for _, trace in sub.sort_values("TimeIndex").groupby("HexID"):
        ax2.plot(trace["TimeIndex"], trace["SOC_per_unit"], linewidth=0.45, alpha=0.12, color="grey")
    ax2.plot(x, stats["mean_soc"], color="red", linewidth=2.0, linestyle="--", label="Mean SoC per BESS unit")
    ax2.fill_between(x, stats["mean_soc"] - stats["sem_soc"], stats["mean_soc"] + stats["sem_soc"], color="red", alpha=0.14)
    ax2.plot([], [], color="grey", linewidth=0.7, alpha=0.5, label="Cell-level SoC traces")

    ax1.axhline(0, color="black", linewidth=0.8)
    ax1.set_xlim(0.4, 48.6)
    ax1.set_xticks(np.arange(1, 49, 4))
    ax1.set_xlabel("30-minute time-interval slots (1–48)")
    ax1.set_ylabel("Mean charge/discharge (kWh per BESS unit per 30-minute slot)")
    ax2.set_ylabel("State of charge (kWh per BESS unit)")
    ax2.grid(False)
    ax1.set_title(f"{month}: BESS operation across cells with installed storage")
    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    _boxed_legend_below(fig, h1 + h2, l1 + l2, ncol=3, bottom=0.25)
    return _save(fig, figures_dir, f"06_bess_operation_{month.lower()}", dpi)


def _plot_demand_supply_balance(results_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    df = _read_csv(results_dir / "supply_by_demand_class.csv", required=True)
    if df.empty:
        raise ValueError("supply_by_demand_class.csv is empty")
    required = [
        "Month", "TimeIndex", "DaysInMonth",
        "Demand_home_total_kWh_day", "Demand_public_base_kWh_day",
        "Home_private_served_kWh_day",
        "Grid_to_home_residual_allocated_kWh_day",
        "PV_to_home_residual_allocated_kWh_day",
        "BESS_to_home_residual_allocated_kWh_day",
        "Grid_to_public_allocated_kWh_day",
        "PV_to_public_allocated_kWh_day",
        "BESS_to_public_allocated_kWh_day",
        "Slack_home_kWh_day", "Slack_public_kWh_day",
    ]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"Missing supply-accounting columns: {missing}")
    for col in required[1:]:
        df[col] = _numeric(df[col]).fillna(0.0)

    weighted_cols = [c for c in required if c not in {"Month", "TimeIndex", "DaysInMonth"}]
    for col in weighted_cols:
        df[col] = df[col] * df["DaysInMonth"]
    annual = df.groupby("TimeIndex")[weighted_cols].sum().reindex(range(1, 49), fill_value=0.0) / 365.0
    x = np.arange(1, 49)

    fig, ax = plt.subplots(figsize=(15.5, 8.5))
    positive_bottom = np.zeros(48)
    for col, label in [
        ("Demand_home_total_kWh_day", "Home demand"),
        ("Demand_public_base_kWh_day", "Public demand (work + public)"),
    ]:
        vals = annual[col].to_numpy() / 1e3
        ax.bar(x, vals, bottom=positive_bottom, label=label, width=0.82)
        positive_bottom += vals

    negative_bottom = np.zeros(48)
    negative_series = [
        ("Home_private_served_kWh_day", "Home chargers (private)"),
        ("Grid_to_home_residual_allocated_kWh_day", "Residual home via public chargers: grid"),
        ("PV_to_home_residual_allocated_kWh_day", "Residual home via public chargers: PV"),
        ("BESS_to_home_residual_allocated_kWh_day", "Residual home via public chargers: BESS"),
        ("Grid_to_public_allocated_kWh_day", "Public demand: grid"),
        ("PV_to_public_allocated_kWh_day", "Public demand: PV"),
        ("BESS_to_public_allocated_kWh_day", "Public demand: BESS"),
    ]
    slack = annual["Slack_home_kWh_day"].to_numpy() + annual["Slack_public_kWh_day"].to_numpy()
    if float(np.max(slack)) > 1e-8:
        negative_series.append(("_slack_total", "Unserved demand (slack)"))
        annual["_slack_total"] = slack
    for col, label in negative_series:
        vals = annual[col].to_numpy() / 1e3
        ax.bar(x, -vals, bottom=-negative_bottom, label=label, width=0.82)
        negative_bottom += vals

    ax.axhline(0, color="black", linewidth=1.0)
    ax.set_xlim(0.4, 48.6)
    ax.set_xticks(np.arange(1, 49, 2))
    ax.set_xlabel("Time of day (30-minute interval: 1–48)")
    ax.set_ylabel("Annual weighted-average representative-day energy (MWh per 30-minute slot)")
    ax.set_title("Charging demand and supply balance by demand class and energy source", pad=18)
    ax.text(0.5, 1.005, "Supply-source attribution across demand classes is a proportional ex-post allocation; source totals and class totals are preserved.", transform=ax.transAxes, ha="center", va="bottom", fontsize=9, color="0.35", style="italic")
    handles, labels = ax.get_legend_handles_labels()
    _boxed_legend_below(fig, handles, labels, ncol=3, bottom=0.27)
    return _save(fig, figures_dir, "16_demand_supply_balance_annual_average", dpi)


def _plot_redirection_heatmap(results_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    df = _read_csv(results_dir / "redirections.csv")
    if df.empty:
        raise ValueError("No positive redirection flows")
    df["Energy_kWh_day"] = _numeric(df["Energy_kWh_day"]).fillna(0.0)
    pivot = df.groupby(["Month", "TimeIndex"])["Energy_kWh_day"].sum().unstack("TimeIndex").reindex(index=MONTHS, columns=range(1, 49), fill_value=0.0)
    fig, ax = plt.subplots(figsize=(12, 5.2))
    image = ax.imshow(pivot.to_numpy(), aspect="auto", interpolation="nearest")
    ax.set_yticks(range(12))
    ax.set_yticklabels([m[:3] for m in MONTHS])
    ticks = np.arange(0, 48, 4)
    ax.set_xticks(ticks)
    ax.set_xticklabels([f"{t / 2:.0f}:00" for t in ticks])
    ax.set_xlabel("Time of representative day")
    ax.set_ylabel("Month")
    ax.set_title("Aggregate redirected energy by month and time")
    cbar = fig.colorbar(image, ax=ax)
    cbar.set_label("Redirected energy (kWh per representative day slot)")
    return _save(fig, figures_dir, "07_redirection_month_time_heatmap", dpi)


def _plot_redirection_type_matrix(results_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    df = _read_csv(results_dir / "redirections_by_type.csv")
    if df.empty:
        raise ValueError("No type-pair redirection reconstruction")
    df["Energy_kWh_annual"] = _numeric(df["Energy_kWh_annual"]).fillna(0.0)
    types = ["slow", "medium", "fast"]
    pivot = df.pivot_table(index="OriginType", columns="DestinationType", values="Energy_kWh_annual", aggfunc="sum", fill_value=0.0).reindex(index=types, columns=types, fill_value=0.0) / 1e3
    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    image = ax.imshow(pivot.to_numpy(), interpolation="nearest")
    ax.set_xticks(range(3)); ax.set_xticklabels([v.capitalize() for v in types])
    ax.set_yticks(range(3)); ax.set_yticklabels([v.capitalize() for v in types])
    ax.set_xlabel("Destination charger type")
    ax.set_ylabel("Origin tariff-reference type")
    ax.set_title("Annual type-aware redirection matrix")
    for r in range(3):
        for c in range(3):
            ax.text(c, r, f"{pivot.iloc[r, c]:,.1f}", ha="center", va="center")
    cbar = fig.colorbar(image, ax=ax)
    cbar.set_label("Redirected energy (MWh/year)")
    return _save(fig, figures_dir, "08_redirection_type_matrix", dpi)


def _find_history(run_dir: Path) -> Path | None:
    candidates = [
        run_dir / "iterations" / "benders_iteration_history.csv",
        run_dir / "results" / "benders_iteration_history.csv",
        run_dir / "results" / "lbbd_history.csv",
        run_dir / "results" / "alternative_c_history.csv",
        # Legacy names remain readable for existing result folders.
        run_dir / "iterations" / "lbbd_iteration_history.csv",
        run_dir / "results" / "lbbd_iteration_history.csv",
    ]
    return next((p for p in candidates if p.exists()), None)


def _history_method(df: pd.DataFrame, path: Path) -> str:
    if "lbbd_gap" in df.columns or path.name in {"lbbd_history.csv", "alternative_c_history.csv"}:
        return "LBBD"
    return "Benders"


def _first_present(df: pd.DataFrame, names: list[str]) -> str | None:
    return next((name for name in names if name in df.columns), None)



def _compact_number(value: float, unit: str = "") -> str:
    if value is None or not np.isfinite(value):
        return "n/a"
    abs_value = abs(float(value))
    if abs_value >= 1e6:
        return f"{value / 1e6:.3f}M{unit}"
    if abs_value >= 1e3:
        return f"{value / 1e3:.1f}k{unit}"
    if abs_value >= 10:
        return f"{value:.1f}{unit}"
    return f"{value:.3g}{unit}"


def _annotate_xy(
    ax: plt.Axes,
    x_value: float,
    y_value: float,
    label: str,
    *,
    color: str = "0.20",
    xytext: tuple[int, int] = (0, 8),
    fontsize: int = 8,
    ha: str = "center",
) -> None:
    if not np.isfinite(x_value) or not np.isfinite(y_value):
        return
    ax.annotate(
        label,
        (x_value, y_value),
        xytext=xytext,
        textcoords="offset points",
        ha=ha,
        va="bottom" if xytext[1] >= 0 else "top",
        fontsize=fontsize,
        color=color,
        bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="0.75", alpha=0.86),
    )


def _annotate_selected_points(
    ax: plt.Axes,
    x_values: pd.Series | np.ndarray,
    y_values: pd.Series | np.ndarray,
    formatter: Callable[[float], str],
    *,
    color: str = "0.20",
    every: bool = False,
    final: bool = True,
    max_points: int = 8,
    fontsize: int = 8,
) -> None:
    xs = np.asarray(x_values, dtype=float)
    ys = np.asarray(y_values, dtype=float)
    valid = [k for k, (x, y) in enumerate(zip(xs, ys)) if np.isfinite(x) and np.isfinite(y)]
    if not valid:
        return
    if every and len(valid) <= max_points:
        selected = valid
    else:
        selected = sorted(set([valid[0], valid[-1]] + ([int(valid[np.nanargmax(ys[valid])])] if len(valid) else [])))
    if final and valid[-1] not in selected:
        selected.append(valid[-1])
    for offset_idx, k in enumerate(selected):
        y_offset = 9 if offset_idx % 2 == 0 else -14
        _annotate_xy(
            ax,
            float(xs[k]),
            float(ys[k]),
            formatter(float(ys[k])),
            color=color,
            xytext=(0, y_offset),
            fontsize=fontsize,
        )


def _lbbd_cut_columns(df: pd.DataFrame) -> list[tuple[str, str]]:
    return [
        ("hall_profit_cuts_added", "Hall/min-cut"),
        ("component_lp_cuts_added", "Component LP"),
        ("annual_lp_cut_added", "Annual LP"),
        ("annual_core_cut_added", "Core-point LP"),
        ("exact_config_cut_added", "Exact configuration"),
        ("partial_logic_cuts_added", "Partial logic"),
    ]


def _sum_columns(df: pd.DataFrame, columns: list[str]) -> pd.Series:
    present = [col for col in columns if col in df.columns]
    if not present:
        return pd.Series(0.0, index=df.index)
    return sum((_numeric(df[col]).fillna(0.0) for col in present), start=pd.Series(0.0, index=df.index))

def _plot_decomposition_convergence(run_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    path = _find_history(run_dir)
    if path is None:
        raise ValueError("No decomposition iteration history")
    df = _read_csv(path, required=True)
    if df.empty or "iteration" not in df.columns:
        raise ValueError("Decomposition iteration history is empty")
    method = _history_method(df, path)
    iteration = _numeric(df["iteration"])
    ub_col = _first_present(df, ["global_best_UB_SEK", "global_ub_SEK", "master_best_bound_UB_SEK", "master_bound_SEK"])
    lb_col = _first_present(df, ["best_LB_SEK", "best_lb_SEK"])
    gap_col = _first_present(df, ["Benders_gap", "lbbd_gap"])
    if ub_col is None or lb_col is None:
        raise ValueError("Decomposition history lacks upper/lower-bound columns")
    ub = _numeric(df[ub_col]) / 1e6
    lb = _numeric(df[lb_col]) / 1e6
    fig, ax = plt.subplots(figsize=(9.8, 6.2))
    upper_line, = ax.plot(iteration, ub, marker="o", linewidth=1.8, label="Global master upper bound")
    lower_line, = ax.plot(iteration, lb, marker="o", linewidth=1.8, label="Best certified lower bound")
    ax.set_xlabel(f"{method} iteration")
    ax.set_ylabel("Objective bound (million SEK/year)")
    ax.set_title(f"{method} convergence")
    handles, labels = [upper_line, lower_line], ["Global master upper bound", "Best certified lower bound"]
    if gap_col is not None:
        ax2 = ax.twinx()
        gap_values = 100 * _numeric(df[gap_col])
        gap_line, = ax2.plot(iteration, gap_values, linestyle="--", linewidth=1.8, marker=".", markersize=5, label=f"Certified {method} gap")
        finite_gap = gap_values[np.isfinite(gap_values)]
        if len(finite_gap):
            ax2.set_ylim(0, max(0.01, 1.22 * float(finite_gap.max())))
        ax2.set_ylabel(f"Certified {method} gap (%)")
        ax2.grid(False)
        for k, (x_value, gap) in enumerate(zip(iteration, gap_values)):
            if not np.isfinite(gap):
                continue
            label = f"{gap:.4f}%" if gap < 0.1 else f"{gap:.3f}%"
            offset = 8 if k % 2 == 0 else -13
            ax2.annotate(label, (x_value, gap), xytext=(0, offset), textcoords="offset points", ha="center", va="bottom" if offset > 0 else "top", fontsize=8, color=gap_line.get_color())
        handles.append(gap_line)
        labels.append(f"Certified {method} gap")
    _boxed_legend_below(fig, handles, labels, ncol=3, bottom=0.23)
    return _save(fig, figures_dir, "09_decomposition_convergence", dpi)


def _plot_decomposition_cut_generation(run_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    path = _find_history(run_dir)
    if path is None:
        raise ValueError("No decomposition iteration history")
    df = _read_csv(path, required=True)
    if df.empty or "iteration" not in df.columns:
        raise ValueError("Decomposition history lacks iteration data")

    method = _history_method(df, path)
    iteration = _numeric(df["iteration"]).astype(int)
    x = np.arange(len(iteration))

    if method != "LBBD":
        cuts = _numeric(df["cuts_added"]).fillna(0.0) if "cuts_added" in df.columns else pd.Series(0.0, index=df.index)
        candidates = _numeric(df["cut_candidates"]).fillna(cuts) if "cut_candidates" in df.columns else cuts.copy()
        cumulative = cuts.cumsum()
        width = 0.36

        fig, ax = plt.subplots(figsize=(9.8, 5.9))
        bars_candidates = ax.bar(
            x - width / 2, candidates, width=width,
            label="Cut candidates / triggers", alpha=0.72, zorder=2,
        )
        bars_added = ax.bar(
            x + width / 2, cuts, width=width,
            label="Cuts added", alpha=0.90, zorder=3,
        )
        ax.set_xticks(x)
        ax.set_xticklabels(iteration.astype(str))
        ax.set_xlabel(f"{method} iteration")
        ax.set_ylabel("Cuts in iteration")
        ax.set_title(f"{method} cut generation and cumulative master enrichment")

        for container in (bars_candidates, bars_added):
            labels = [f"{int(v)}" if v > 0 else "" for v in container.datavalues]
            ax.bar_label(container, labels=labels, padding=2, fontsize=8)

        ax2 = ax.twinx()
        cumulative_line, = ax2.plot(
            x, cumulative, marker="o", linewidth=2.3,
            label="Cumulative cuts", zorder=5,
        )
        ax2.set_ylabel("Cumulative cuts in master")
        ax2.set_ylim(
            0,
            max(1.0, 1.15 * float(cumulative.max()) if len(cumulative) else 1.0),
        )
        ax2.grid(False)

        h1, l1 = ax.get_legend_handles_labels()
        _boxed_legend_below(
            fig,
            h1 + [cumulative_line],
            l1 + ["Cumulative cuts"],
            ncol=3,
            bottom=0.23,
        )
        return _save(fig, figures_dir, "17_decomposition_cut_generation", dpi)

    families = [
        (column, label)
        for column, label in _lbbd_cut_columns(df)
        if column in df.columns
    ]
    if not families:
        raise ValueError("LBBD history lacks cut-family columns")

    values = {
        label: _numeric(df[column]).fillna(0.0)
        for column, label in families
    }
    active = [
        (label, series)
        for label, series in values.items()
        if float(series.sum()) > 0
    ]

    if not active:
        raise ValueError("No LBBD cuts were accepted")

    total = sum(
        (series for _, series in active),
        start=pd.Series(0.0, index=df.index),
    )
    cumulative = total.cumsum()

    fig, ax = plt.subplots(figsize=(10.5, 6.1))
    bottom = np.zeros(len(df), dtype=float)

    for label, series in active:
        vals = series.to_numpy(dtype=float)
        ax.bar(
            x,
            vals,
            bottom=bottom,
            width=0.64,
            label=label,
            zorder=3,
        )
        bottom += vals

    for k, value in enumerate(bottom):
        if value > 0:
            ax.text(
                x[k],
                value,
                f"{int(round(value))}",
                ha="center",
                va="bottom",
                fontsize=8,
            )

    ax.set_xticks(x)
    ax.set_xticklabels(iteration.astype(str))
    ax.set_xlabel("LBBD iteration")
    ax.set_ylabel("Cuts added in iteration")
    ax.set_title("LBBD cut generation and cumulative master enrichment")
    ax.set_ylim(0, max(1.0, 1.25 * float(max(bottom))))

    ax2 = ax.twinx()
    cumulative_line, = ax2.plot(
        x,
        cumulative.to_numpy(dtype=float),
        marker="o",
        linewidth=2.3,
        label="Cumulative cuts",
        zorder=5,
    )
    ax2.set_ylabel("Cumulative cuts in master")
    ax2.set_ylim(0, max(1.0, 1.15 * float(cumulative.max())))
    ax2.grid(False)

    cumulative_values = cumulative.to_numpy(dtype=float)
    for k, value in enumerate(cumulative_values):
        changed = k == 0 or value != cumulative_values[k - 1]
        final = k == len(cumulative_values) - 1
        if changed or final:
            _annotate_xy(
                ax2,
                float(x[k]),
                float(value),
                f"{int(round(value))}",
                color=cumulative_line.get_color(),
                xytext=(0, 8),
                fontsize=8,
            )

    h1, l1 = ax.get_legend_handles_labels()
    _boxed_legend_below(
        fig,
        h1 + [cumulative_line],
        l1 + ["Cumulative cuts"],
        ncol=min(4, len(h1) + 1),
        bottom=0.23,
    )
    return _save(fig, figures_dir, "17_decomposition_cut_generation", dpi)



def _load_lbbd_history(run_dir: Path) -> pd.DataFrame:
    path = _find_history(run_dir)
    if path is None:
        raise ValueError("No LBBD iteration history")
    df = _read_csv(path, required=True)
    if df.empty or "iteration" not in df.columns or _history_method(df, path) != "LBBD":
        raise ValueError("Run does not contain LBBD iteration history")
    return df.copy()


def _plot_lbbd_cut_families(run_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    df = _load_lbbd_history(run_dir)

    families = [
        (column, label)
        for column, label in _lbbd_cut_columns(df)
        if column in df.columns
    ]
    if not families:
        raise ValueError("LBBD history lacks cut-family columns")

    totals = pd.Series({
        label: float(_numeric(df[column]).fillna(0.0).sum())
        for column, label in families
    })

    active = totals[totals > 0]
    if active.empty:
        raise ValueError("No LBBD cuts were accepted")

    fig, ax = plt.subplots(figsize=(8.8, 5.2))
    y = np.arange(len(active))
    bars = ax.barh(y, active.to_numpy(dtype=float), height=0.60)

    ax.set_yticks(y)
    ax.set_yticklabels(active.index)
    ax.invert_yaxis()
    ax.set_xlabel("Cuts accepted into master")
    ax.set_title(
        f"Accepted LBBD cuts by family "
        f"({len(active)} of {len(families)} families active)"
    )

    maximum = max(1.0, float(active.max()))
    ax.set_xlim(0, 1.20 * maximum)

    for bar, value in zip(bars, active):
        ax.text(
            bar.get_width() + 0.025 * maximum,
            bar.get_y() + bar.get_height() / 2,
            f"{int(round(value))}",
            ha="left",
            va="center",
        )

    ax.grid(axis="x", alpha=0.25)
    ax.grid(axis="y", visible=False)

    return _save(fig, figures_dir, "18_lbbd_cut_families", dpi)



def _plot_lbbd_candidate_bounds(run_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    """Show exact certification quality of evaluated infrastructures.

    Master/global bounds are intentionally excluded here.  Bootstrap and LP-fallback
    candidates are not primal solutions of the same master MIP, so mixing their Eta
    values with exact recourse can create visually dramatic but algorithmically
    meaningless "relaxation errors".  Global bound convergence is shown in figure 09.
    """
    df = _load_lbbd_history(run_dir)
    if "candidate_exact_objective_SEK" not in df.columns:
        raise ValueError("LBBD history lacks exact candidate objectives")
    iteration = _numeric(df["iteration"])
    exact = _numeric(df["candidate_exact_objective_SEK"]) / 1e6
    fixed_ub = (
        _numeric(df["candidate_fixed_upper_bound_SEK"]) / 1e6
        if "candidate_fixed_upper_bound_SEK" in df.columns
        else pd.Series(np.nan, index=df.index)
    )
    best_lb = (
        _numeric(df["best_lb_SEK"]) / 1e6
        if "best_lb_SEK" in df.columns
        else exact.cummax()
    )
    fixed_gap = (
        100.0 * _numeric(df["candidate_fixed_gap"])
        if "candidate_fixed_gap" in df.columns
        else pd.Series(np.nan, index=df.index)
    )

    if exact.notna().sum() == 0:
        raise ValueError("No exact candidate certifications in LBBD history")

    fig, (ax_top, ax_bottom) = plt.subplots(
        2, 1, figsize=(11.4, 8.2), sharex=True,
        gridspec_kw={"height_ratios": [1.2, 0.8]},
    )
    ax_top.ticklabel_format(axis="y", style="plain", useOffset=False)
    line_exact, = ax_top.plot(iteration, exact, marker="o", linewidth=1.9, label="Exact feasible candidate")
    if fixed_ub.notna().any():
        ax_top.plot(iteration, fixed_ub, marker="o", linewidth=1.5, linestyle="--", label="Fixed-layout exact upper bound")
    if best_lb.notna().any():
        ax_top.step(iteration, best_lb, where="post", linewidth=2.2, label="Best certified incumbent")

    _annotate_selected_points(ax_top, iteration, exact, lambda y: f"{y:.3f} MSEK", color=line_exact.get_color(), every=False, final=True, max_points=4)
    ax_top.margins(x=0.08, y=0.22)
    ax_top.set_ylabel("Objective (million SEK/year)")
    ax_top.set_title("Exact certification of evaluated LBBD infrastructures", pad=12)

    positive_gap = fixed_gap.where(fixed_gap > 0)
    if positive_gap.notna().any():
        line_gap, = ax_bottom.semilogy(iteration, positive_gap, marker="o", linewidth=1.9, label="Fixed-layout exact MIP gap")
        _annotate_selected_points(ax_bottom, iteration, positive_gap, lambda y: f"{y:.5f}%", color=line_gap.get_color(), every=False, final=True, max_points=4)
    else:
        ax_bottom.text(0.5, 0.5, "No positive fixed-layout certification gaps", transform=ax_bottom.transAxes, ha="center", va="center")
    ax_bottom.set_xlabel("LBBD iteration")
    ax_bottom.set_ylabel("Exact fixed-layout gap (%)")
    ax_bottom.set_title("Exact certification precision for each evaluated infrastructure")

    handles1, labels1 = ax_top.get_legend_handles_labels()
    handles2, labels2 = ax_bottom.get_legend_handles_labels()
    _boxed_legend_below(fig, handles1 + handles2, labels1 + labels2, ncol=2, bottom=0.27)
    return _save(fig, figures_dir, "19_lbbd_candidate_bounds", dpi)


def _plot_lbbd_infrastructure_evolution(
    run_dir: Path,
    figures_dir: Path,
    dpi: int,
) -> list[str]:
    df = _load_lbbd_history(run_dir)

    best_columns = {
        "Slow": "best_slow",
        "Medium": "best_medium",
        "Fast": "best_fast",
        "PV": "best_PV",
        "BESS": "best_BESS",
    }
    legacy_columns = {
        "Slow": "slow",
        "Medium": "medium",
        "Fast": "fast",
        "PV": "PV",
        "BESS": "BESS",
    }

    if all(column in df.columns for column in best_columns.values()):
        columns = best_columns
        title = "Best-certified LBBD infrastructure by iteration"
    else:
        columns = legacy_columns
        title = "Evaluated LBBD infrastructure by iteration"

    if not any(column in df.columns for column in columns.values()):
        raise ValueError("LBBD history lacks infrastructure counts")

    iteration = _numeric(df["iteration"]).to_numpy(dtype=float)

    fig, axes = plt.subplots(
        1,
        3,
        figsize=(14.0, 4.8),
        sharex=True,
    )

    for label in ("Slow", "Medium", "Fast"):
        column = columns[label]
        if column not in df.columns:
            continue
        values = _numeric(df[column]).ffill()
        line, = axes[0].step(
            iteration,
            values,
            where="post",
            marker="o",
            linewidth=1.8,
            label=label,
        )
        valid = values.dropna()
        if not valid.empty:
            _annotate_xy(
                axes[0],
                float(iteration[-1]),
                float(valid.iloc[-1]),
                f"{int(round(valid.iloc[-1])):,}",
                color=line.get_color(),
                xytext=(0, 8),
                fontsize=8,
            )

    axes[0].set_title("Public chargers")
    axes[0].set_ylabel("Installed chargers")
    axes[0].legend(frameon=True)

    if columns["PV"] in df.columns:
        values = _numeric(df[columns["PV"]]).ffill()
        line, = axes[1].step(
            iteration,
            values,
            where="post",
            marker="o",
            linewidth=1.8,
        )
        valid = values.dropna()
        if not valid.empty:
            _annotate_xy(
                axes[1],
                float(iteration[-1]),
                float(valid.iloc[-1]),
                f"{int(round(valid.iloc[-1])):,}",
                color=line.get_color(),
                xytext=(0, 8),
                fontsize=8,
            )

    axes[1].set_title("Photovoltaic deployment")
    axes[1].set_ylabel("Installed PV panels")

    if columns["BESS"] in df.columns:
        values = _numeric(df[columns["BESS"]]).ffill()
        line, = axes[2].step(
            iteration,
            values,
            where="post",
            marker="o",
            linewidth=1.8,
        )
        valid = values.dropna()
        if not valid.empty:
            _annotate_xy(
                axes[2],
                float(iteration[-1]),
                float(valid.iloc[-1]),
                f"{int(round(valid.iloc[-1])):,}",
                color=line.get_color(),
                xytext=(0, 8),
                fontsize=8,
            )

    axes[2].set_title("Battery storage deployment")
    axes[2].set_ylabel("Installed BESS units")

    for ax in axes:
        ax.set_xlabel("LBBD iteration")
        ax.set_xticks(iteration)
        ax.set_xticklabels([str(int(v)) for v in iteration])
        ax.margins(x=0.07, y=0.16)

    fig.suptitle(title, y=0.98)
    fig.subplots_adjust(
        left=0.07,
        right=0.98,
        bottom=0.16,
        top=0.84,
        wspace=0.30,
    )

    return _save(fig,figures_dir, "20_lbbd_infrastructure_evolution", dpi)


def _plot_lbbd_iteration_timing(run_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    df = _load_lbbd_history(run_dir)
    if "master_solve_seconds" not in df.columns or "elapsed_seconds" not in df.columns:
        raise ValueError("LBBD history lacks timing diagnostics")
    iteration = _numeric(df["iteration"]).astype(int).to_numpy()
    master = _numeric(df["master_solve_seconds"]).fillna(0.0).to_numpy(dtype=float)
    elapsed = _numeric(df["elapsed_seconds"]).ffill().fillna(0.0).to_numpy(dtype=float)
    iteration_total = np.diff(np.concatenate(([0.0], elapsed)))
    other = np.maximum(0.0, iteration_total - master)
    x = np.arange(len(iteration))
    fig, ax = plt.subplots(figsize=(10.6, 6.3))
    ax.bar(x, master / 60.0, label="Master solve", width=0.72)
    ax.bar(x, other / 60.0, bottom=master / 60.0, label="Oracles, cuts and export", width=0.72)
    ax.set_xticks(x)
    ax.set_xticklabels(iteration.astype(str))
    ax.set_xlabel("LBBD iteration")
    ax.set_ylabel("Iteration time (minutes)")
    ax.set_title("LBBD iteration runtime composition")
    ax2 = ax.twinx()
    line, = ax2.plot(x, elapsed / 60.0, marker="o", linewidth=2.0, linestyle="--", label="Cumulative runtime")
    ax2.set_ylabel("Cumulative runtime (minutes)")
    ax2.grid(False)
    h1, l1 = ax.get_legend_handles_labels()
    _boxed_legend_below(fig, h1 + [line], l1 + ["Cumulative runtime"], ncol=3, bottom=0.23)
    return _save(fig, figures_dir, "21_lbbd_iteration_timing", dpi)


def _plot_lbbd_gap_diagnostics(run_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    df = _load_lbbd_history(run_dir)
    iteration = _numeric(df["iteration"])
    master_col = "master_mip_gap" if "master_mip_gap" in df.columns else "master_internal_gap"
    series = [
        ("lbbd_gap", "Certified global LBBD gap"),
        (master_col, "Achieved master MIP gap (incumbent solves only)"),
        ("candidate_fixed_gap", "Fixed-layout exact MIP gap"),
    ]
    present = [(column, label) for column, label in series if column in df.columns and _numeric(df[column]).notna().any()]
    if not present:
        raise ValueError("LBBD history lacks gap diagnostics")
    fig, ax = plt.subplots(figsize=(10.4, 6.2))
    for column, label in present:
        values = 100.0 * _numeric(df[column])
        if column == master_col and "master_gap_is_mip" in df.columns:
            values = values.where(_numeric(df["master_gap_is_mip"]).fillna(0) > 0.5)
        positive = values.where(values > 0)
        if positive.notna().any():
            ax.semilogy(iteration, positive, marker="o", linewidth=1.8, label=label)
    ax.set_xlabel("LBBD iteration")
    ax.set_ylabel("Gap (%) — logarithmic scale")
    ax.set_title("Comparable LBBD optimality-gap diagnostics")
    handles, labels = ax.get_legend_handles_labels()
    _boxed_legend_below(fig, handles, labels, ncol=3, bottom=0.23)
    return _save(fig, figures_dir, "22_lbbd_gap_diagnostics", dpi)

def _plot_lbbd_adaptive_master_control(run_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    df = _load_lbbd_history(run_dir)
    required = {"iteration", "lbbd_gap", "master_gap_requested"}
    if not required.issubset(df.columns):
        raise ValueError("LBBD history lacks adaptive master-gap diagnostics")
    iteration = _numeric(df["iteration"])
    certified = 100.0 * _numeric(df["lbbd_gap"])
    requested = 100.0 * _numeric(df["master_gap_requested"])
    master_col = "master_mip_gap" if "master_mip_gap" in df.columns else "master_internal_gap"
    master_actual = (
        100.0 * _numeric(df[master_col])
        if master_col in df.columns else pd.Series(np.nan, index=df.index)
    )
    if "master_gap_is_mip" in df.columns:
        master_actual = master_actual.where(_numeric(df["master_gap_is_mip"]).fillna(0) > 0.5)

    fig, ax = plt.subplots(figsize=(11.0, 6.7))
    for values, label, style in [
        (certified, "Certified LBBD gap", "-"),
        (requested, "Requested master MIP gap", "--"),
        (master_actual, "Achieved master MIP gap", ":"),
    ]:
        positive = values.where(values > 0)
        if positive.notna().any():
            line, = ax.semilogy(iteration, positive, marker="o", linewidth=1.9, linestyle=style, label=label)
            _annotate_selected_points(ax, iteration, positive, lambda y: f"{y:.4f}%", color=line.get_color(), every=True, max_points=8)

    plotted_values = pd.concat([certified, requested, master_actual], axis=0).dropna()
    plotted_values = plotted_values[plotted_values > 0]
    if not plotted_values.empty:
        ax.set_ylim(float(plotted_values.min()) / 1.55, float(plotted_values.max()) * 1.85)
    ax.margins(x=0.07)
    ax.set_xlabel("LBBD iteration")
    ax.set_ylabel("Gap (%) — logarithmic scale")
    ax.set_title("Adaptive LBBD master control (comparable MIP gaps only)", pad=12)

    handles, labels = ax.get_legend_handles_labels()
    if "candidate_source" in df.columns:
        # Mark non-MIP candidate-generation iterations without assigning them a fake
        # master MIP gap.  They are algorithmic events, not failed convergence points.
        sources = df["candidate_source"].astype(str)
        non_mip = ~sources.eq("master_mip_incumbent")
        if non_mip.any() and not plotted_values.empty:
            y_marker = float(plotted_values.max()) * 1.35
            xs = iteration[non_mip]
            ax.scatter(xs, [y_marker] * len(xs), marker="x", label="Bootstrap/fallback/bound-only iteration")
            handles, labels = ax.get_legend_handles_labels()

    if "candidate_repeat_count" in df.columns:
        ax2 = ax.twinx()
        repeats = _numeric(df["candidate_repeat_count"]).fillna(0.0)
        repeat_line, = ax2.step(iteration, repeats, where="mid", linewidth=1.6, label="Consecutive repeated candidate count")
        ax2.set_ylabel("Repeated-candidate count")
        ax2.set_ylim(0, max(1.0, 1.20 * float(repeats.max())))
        ax2.grid(False)
        handles.append(repeat_line)
        labels.append("Consecutive repeated candidate count")
    _boxed_legend_below(fig, handles, labels, ncol=2, bottom=0.27)
    return _save(fig, figures_dir, "23_lbbd_adaptive_master_control", dpi)

def _plot_lbbd_candidate_reuse(run_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    df = _load_lbbd_history(run_dir)
    required = {"iteration", "candidate_cached", "candidate_repeat_count", "new_cuts_total"}
    if not required.issubset(df.columns):
        raise ValueError("LBBD history lacks candidate-cache diagnostics")
    iteration = _numeric(df["iteration"]).astype(int).to_numpy()
    cached = _numeric(df["candidate_cached"]).fillna(0.0).clip(0, 1).to_numpy(dtype=float)
    evaluated = 1.0 - cached
    cuts = _numeric(df["new_cuts_total"]).fillna(0.0).to_numpy(dtype=float)
    repeats = _numeric(df["candidate_repeat_count"]).fillna(0.0).to_numpy(dtype=float)
    x = np.arange(len(iteration))

    fig, ax = plt.subplots(figsize=(10.7, 6.2))
    ax.bar(x, evaluated, label="New candidate evaluated", width=0.70)
    ax.bar(x, cached, bottom=evaluated, label="Exact result reused from cache", width=0.70)
    ax.set_xticks(x)
    ax.set_xticklabels(iteration.astype(str))
    ax.set_xlabel("LBBD iteration")
    ax.set_ylabel("Candidate evaluation indicator")
    ax.set_ylim(0, 1.25)
    ax.set_title("LBBD candidate reuse, repetition and new inference")

    ax2 = ax.twinx()
    repeat_line, = ax2.plot(x, repeats, marker="o", linewidth=1.8, label="Repeated-candidate count")
    cut_line, = ax2.plot(x, cuts, marker="s", linestyle="--", linewidth=1.6, label="New cuts added")
    ax2.set_ylabel("Count")
    ax2.set_ylim(0, max(1.0, 1.20 * float(max(repeats.max(initial=0), cuts.max(initial=0)))))
    ax2.grid(False)
    h1, l1 = ax.get_legend_handles_labels()
    _boxed_legend_below(fig, h1 + [repeat_line, cut_line], l1 + ["Repeated-candidate count", "New cuts added"], ncol=2, bottom=0.25)
    return _save(fig, figures_dir, "24_lbbd_candidate_reuse", dpi)

def _plot_slack(results_dir: Path, figures_dir: Path, dpi: int) -> list[str]:
    df = _read_csv(results_dir / "slack.csv")
    if df.empty:
        raise ValueError("No positive slack")
    df["Slack_kWh_annual"] = _numeric(df["Slack_kWh_annual"]).fillna(0.0)
    agg = df.groupby("Month")["Slack_kWh_annual"].sum().reindex(MONTHS, fill_value=0.0)
    if float(agg.sum()) <= 1e-8:
        raise ValueError("No positive slack")
    fig, ax = plt.subplots(figsize=(9.5, 5))
    ax.bar(np.arange(12), agg.to_numpy())
    ax.set_xticks(np.arange(12)); ax.set_xticklabels([m[:3] for m in MONTHS])
    ax.set_ylabel("Unmet demand (kWh/year)")
    ax.set_title("Annualized unmet charging demand by month")
    return _save(fig, figures_dir, "10_slack_by_month", dpi)


def _load_geometry(path: Path):
    import geopandas as gpd
    gdf = gpd.read_file(path)[["HexID", "geometry"]].copy()
    gdf = gdf.loc[:, ~gdf.columns.duplicated()].copy()
    gdf["HexID"] = pd.to_numeric(gdf["HexID"], errors="coerce")
    gdf = gdf.dropna(subset=["HexID", "geometry"]).drop_duplicates("HexID")
    gdf["HexID"] = gdf["HexID"].astype(int)
    if gdf.crs is None:
        raise ValueError(f"Geometry file has no CRS: {path}")
    return gdf


def _merge_geometry(results_dir: Path, geometry_path: Path):
    gdf = _load_geometry(geometry_path)
    infra = _read_csv(results_dir / "infrastructure_by_hex.csv", required=True)
    infra = infra.loc[:, ~infra.columns.duplicated()].copy()
    if "HexID" not in infra.columns:
        raise ValueError("infrastructure_by_hex.csv lacks HexID")
    infra["HexID"] = pd.to_numeric(infra["HexID"], errors="coerce").astype("Int64")
    infra = infra.dropna(subset=["HexID"]).drop_duplicates("HexID").copy()
    infra["HexID"] = infra["HexID"].astype(int)
    for col in [c for c in infra.columns if c != "HexID"]:
        infra[col] = pd.to_numeric(infra[col], errors="coerce").fillna(0.0)
    merged = gdf.merge(infra, on="HexID", how="left", validate="one_to_one")
    for col in [c for c in infra.columns if c != "HexID"]:
        merged[col] = pd.to_numeric(merged[col], errors="coerce").fillna(0.0)
    return gdf, merged


def _plot_choropleth(
    merged,
    base,
    column: str,
    title: str,
    cbar_label: str,
    figures_dir: Path,
    stem: str,
    dpi: int,
    cmap: str = "viridis",
    symmetric: bool = False,
    basemap_alpha: float = 0.25,
) -> list[str]:
    if column not in merged.columns:
        raise ValueError(f"Missing map column: {column}")
    merged3857 = merged.to_crs(epsg=3857)
    base3857 = base.to_crs(epsg=3857)
    fig, ax = plt.subplots(figsize=(10.5, 10.5))
    base3857.boundary.plot(ax=ax, linewidth=0.15, alpha=0.15, color="0.35", zorder=1)
    _add_basemap(ax, alpha=basemap_alpha)
    values = pd.to_numeric(merged3857[column], errors="coerce").fillna(0.0)
    merged3857[column] = values
    kwargs = {
        "column": column,
        "ax": ax,
        "cmap": cmap,
        "legend": True,
        "edgecolor": "white",
        "linewidth": 0.15,
        "alpha": 0.78,
        "zorder": 2,
    }
    if symmetric:
        vmax = float(np.nanmax(np.abs(values.to_numpy()))) if len(values) else 0.0
        if vmax > 0:
            kwargs.update({"vmin": -vmax, "vmax": vmax})
    merged3857.plot(**kwargs)
    base3857.boundary.plot(ax=ax, linewidth=0.20, alpha=0.35, color="0.25", zorder=3)
    ax.set_axis_off()
    ax.set_aspect("equal")
    ax.set_title(title)
    if len(fig.axes) > 1:
        fig.axes[-1].set_ylabel(cbar_label)
    return _save(fig, figures_dir, stem, dpi)


def _plot_redirection_corridors(
    redir: pd.DataFrame,
    merged,
    base,
    figures_dir: Path,
    dpi: int,
    max_flow_arcs: int,
    month: str,
    basemap_alpha: float,
) -> list[str]:
    required = {"from_HexID", "to_HexID", "Month", "Energy_kWh_day"}
    if not required.issubset(redir.columns):
        raise ValueError(f"redirections.csv lacks columns: {sorted(required - set(redir.columns))}")
    sub = redir[redir["Month"].astype(str) == month].copy()
    if sub.empty:
        raise ValueError(f"No positive redirection flows for {month}")
    sub["Energy_kWh_day"] = pd.to_numeric(sub["Energy_kWh_day"], errors="coerce").fillna(0.0)
    agg = (
        sub.groupby(["from_HexID", "to_HexID"], as_index=False)["Energy_kWh_day"]
        .sum()
        .query("Energy_kWh_day > 0")
        .nlargest(max(1, int(max_flow_arcs)), "Energy_kWh_day")
    )
    if agg.empty:
        raise ValueError(f"No positive aggregated redirection corridors for {month}")

    merged3857 = merged.to_crs(epsg=3857)
    base3857 = base.to_crs(epsg=3857)
    cent = merged3857.set_index("HexID").geometry.centroid
    rows = []
    for _, row in agg.iterrows():
        i, j = int(row["from_HexID"]), int(row["to_HexID"])
        if i not in cent.index or j not in cent.index:
            continue
        p1, p2 = cent.loc[i], cent.loc[j]
        if p1.equals(p2):
            continue
        rows.append((p1.x, p1.y, p2.x, p2.y, float(row["Energy_kWh_day"])))
    if not rows:
        raise ValueError(f"No redirection corridors could be matched to geometry for {month}")

    weights = np.asarray([r[4] for r in rows], dtype=float)
    max_weight = max(float(weights.max()), 1e-12)
    fig, ax = plt.subplots(figsize=(12, 12))
    base3857.boundary.plot(ax=ax, color="0.45", linewidth=0.30, alpha=0.20, zorder=1)
    _add_basemap(ax, alpha=basemap_alpha)
    base3857.boundary.plot(ax=ax, color="0.35", linewidth=0.28, alpha=0.28, zorder=2)

    for fx, fy, tx, ty, energy in sorted(rows, key=lambda r: r[4]):
        lw = 0.6 + 3.6 * math.sqrt(max(energy, 0.0) / max_weight)
        arrow = FancyArrowPatch(
            (fx, fy),
            (tx, ty),
            arrowstyle="-|>",
            linewidth=lw,
            edgecolor="black",
            facecolor="lightgray",
            mutation_scale=5.5 + 2.4 * lw,
            alpha=0.78,
            shrinkA=1.5,
            shrinkB=1.5,
            zorder=3,
        )
        ax.add_patch(arrow)

    quantiles = np.unique(np.quantile(weights[weights > 0], [0.10, 0.50, 1.00]))
    legend_handles = []
    for value in quantiles:
        lw = 0.6 + 3.6 * math.sqrt(float(value) / max_weight)
        if value >= 1000.0:
            label = f"{value / 1e3:,.2f} MWh/day"
        else:
            label = f"{value:,.1f} kWh/day"
        legend_handles.append(Line2D([], [], color="black", linewidth=lw, label=label))
    fig.legend(
        handles=legend_handles,
        title="Corridor energy",
        loc="lower center",
        bbox_to_anchor=(0.5, 0.012),
        ncol=max(1, len(legend_handles)),
        frameon=True,
        fancybox=True,
        framealpha=0.96,
        edgecolor="0.6",
    )
    ax.set_axis_off()
    ax.set_aspect("equal")
    ax.set_title(f"{month}: redirected charging-demand corridors\nTop {len(rows)} origin–destination flows")
    fig.subplots_adjust(bottom=0.105, top=0.92)
    return _save(fig, figures_dir, f"15_map_redirection_corridors_{month.lower()}", dpi)


def _plot_maps(
    results_dir: Path,
    figures_dir: Path,
    geometry_path: Path,
    dpi: int,
    max_flow_arcs: int,
    redirection_month: str = "June",
    basemap_alpha: float = 0.28,
) -> list[str]:
    base, merged = _merge_geometry(results_dir, geometry_path)
    outputs: list[str] = []
    outputs += _plot_choropleth(
        merged, base, "Total_public_capacity_kWh_slot", "Installed public charging capacity",
        "kWh per 30-minute slot", figures_dir, "11_map_public_charging_capacity", dpi,
        basemap_alpha=basemap_alpha,
    )
    outputs += _plot_choropleth(
        merged, base, "PV_panels", "Installed PV panels", "PV panels",
        figures_dir, "12_map_pv_installation", dpi, basemap_alpha=basemap_alpha,
    )
    outputs += _plot_choropleth(
        merged, base, "Battery_units", "Installed BESS units", "10-kWh BESS units",
        figures_dir, "13_map_bess_installation", dpi, basemap_alpha=basemap_alpha,
    )

    redir = _read_csv(results_dir / "redirections.csv")
    if not redir.empty:
        redir["Energy_kWh_annual"] = _numeric(redir["Energy_kWh_annual"]).fillna(0.0)
        out = redir.groupby("from_HexID")["Energy_kWh_annual"].sum()
        inc = redir.groupby("to_HexID")["Energy_kWh_annual"].sum()
        merged["Net_redirection_in_kWh_annual"] = merged["HexID"].map(inc).fillna(0.0) - merged["HexID"].map(out).fillna(0.0)
        outputs += _plot_choropleth(
            merged, base, "Net_redirection_in_kWh_annual", "Net annual redirected energy by cell",
            "Incoming minus outgoing kWh/year", figures_dir, "14_map_net_redirection", dpi,
            cmap="coolwarm", symmetric=True, basemap_alpha=basemap_alpha,
        )
        outputs += _plot_redirection_corridors(
            redir, merged, base, figures_dir, dpi, max_flow_arcs,
            month=redirection_month, basemap_alpha=basemap_alpha,
        )
    return outputs


def _write_figures_readme(figures_dir: Path) -> None:
    text = """# Generated optimization figures

Figures are generated automatically after successful monolithic, Benders, and LBBD result export.
PNG files use the run-level resolution setting (default: 300 dpi). The figure manifest records
which figure groups were generated, skipped, or failed.

## How to read the common result figures

- `01_economic_breakdown.png` separates annual revenue, grid electricity, redirection incentives,
  slack penalty, charger capex, and PV/BESS capex. Positive bars increase profit; negative bars reduce it.
- `02_charger_deployment_and_utilization.png` compares installed slow, medium, and fast chargers
  with the annual utilization of their available capacity.
- `03_monthly_energy_supply_mix.png` shows whether charger energy is supplied directly from the
  grid, directly from PV, or through battery discharge.
- `04_dispatch_<month>.png` gives the representative-day dispatch profile for selected months.
- `05_bess_soc_by_month.png` and `06_bess_operation_<month>.png` describe the linked BESS state of
  charge and charge/discharge operation. They are generated only when BESS output files exist.
- `07_redirection_month_time_heatmap.png` shows when redirected charging is used most strongly.
- `08_redirection_type_matrix.png` shows the origin charger-type to destination charger-type energy
  assignment in the exact exported solution.
- `10_slack_by_month.png` is generated only when positive unmet demand exists. A skipped slack figure
  normally means the optimized solution had zero positive slack.
- `11_map_public_charging_capacity.png` through `15_map_redirection_corridors_<month>.png` are spatial
  maps. If `contextily` or internet access is unavailable, maps are still generated from the vector geometry.
- `16_demand_supply_balance_annual_average.png` compares home and public charging supply accounting.

## How to read decomposition figures

- `09_decomposition_convergence.png` is the main certificate plot. The upper-bound line is the valid
  global master bound. The lower-bound line is the best exact feasible incumbent. The dashed gap line
  is `(UB - LB) / max(1, |UB|)` in percent.

- `17_decomposition_cut_generation.png` shows cuts accepted in each decomposition iteration and the cumulative enrichment of the master.
  For LBBD, accepted cuts are stacked by cut family.

- `18_lbbd_cut_families.png` summarizes the LBBD cut families that actually contributed constraints to the master.

- `19_lbbd_candidate_bounds.png` shows exact candidate profit, fixed-infrastructure upper bounds, the best certified incumbent,
  and exact fixed-infrastructure certification gaps.

- `20_lbbd_infrastructure_evolution.png` shows the actual charger, photovoltaic-panel, and battery-unit counts of the best certified
  infrastructure across LBBD iterations.

- `21_lbbd_iteration_timing.png` separates master-solve time from oracle/cut/export time and shows the cumulative runtime.

- `22_lbbd_gap_diagnostics.png` compares the global LBBD gap, master MIP gap, and exact fixed-layout MIP gap on a logarithmic scale.

- `23_lbbd_adaptive_master_control.png` verifies that the requested trial-master gap tightens as the certified LBBD gap decreases. This is important because a loose trial-master MIP gap can stall outer-loop
  convergence.
  
- `24_lbbd_candidate_reuse.png` shows whether an iteration evaluated a new infrastructure candidate or
  reused an exact result from the internal cache, together with repeated-candidate counts and new cuts.

## Regenerating figures

```powershell
python src\\visualize_results.py --run-dir "runs\\<RUN_FOLDER>" --dataset small --dpi 300 --redirection-map-month June
```
"""
    (figures_dir / "README_FIGURES.md").write_text(text, encoding="utf-8")



def generate_run_figures(
    run_dir: str | Path,
    project_root: str | Path | None = None,
    dataset: str | None = None,
    parking_shapefile: str | None = None,
    dpi: int = 300,
    max_flow_arcs: int = 150,
    redirection_map_month: str = "June",
    basemap_alpha: float = 0.28,
) -> pd.DataFrame:
    run_dir = Path(run_dir).resolve()
    project_root = Path(project_root).resolve() if project_root else Path(__file__).resolve().parents[1]
    results_dir = run_dir / "results"
    if not results_dir.exists():
        raise FileNotFoundError(f"Results folder not found: {results_dir}")
    figures_dir = run_dir / "figures"
    figures_dir.mkdir(parents=True, exist_ok=True)
    _setup_style()
    dataset = dataset or _infer_dataset(run_dir)
    geometry_path = _resolve_geometry(project_root, dataset, parking_shapefile)

    tasks: list[tuple[str, Callable[[], list[str]]]] = [
        ("economic_breakdown", lambda: _plot_economic_breakdown(results_dir, figures_dir, dpi)),
        ("charger_deployment", lambda: _plot_charger_deployment(results_dir, figures_dir, dpi)),
        ("monthly_energy", lambda: _plot_monthly_energy(results_dir, figures_dir, dpi)),
    ]
    hourly = None
    try:
        hourly = _prepare_hourly(results_dir)
        for month in REPRESENTATIVE_MONTHS:
            tasks.append((f"dispatch_{month}", lambda month=month: _plot_dispatch_month(hourly, month, figures_dir, dpi)))
        tasks.append(("bess_soc", lambda: _plot_soc_by_month(results_dir, figures_dir, dpi)))
        for month in ["January", "July"]:
            tasks.append((f"bess_operation_{month}", lambda month=month: _plot_battery_operation_month(hourly, month, figures_dir, dpi, results_dir=results_dir)))
    except Exception:
        pass
    tasks += [
        ("demand_supply_balance", lambda: _plot_demand_supply_balance(results_dir, figures_dir, dpi)),
        ("redirection_heatmap", lambda: _plot_redirection_heatmap(results_dir, figures_dir, dpi)),
        ("redirection_type_matrix", lambda: _plot_redirection_type_matrix(results_dir, figures_dir, dpi)),
        ("decomposition_convergence", lambda: _plot_decomposition_convergence(run_dir, figures_dir, dpi)),
        ("decomposition_cut_generation", lambda: _plot_decomposition_cut_generation(run_dir, figures_dir, dpi)),
        ("lbbd_cut_families", lambda: _plot_lbbd_cut_families(run_dir, figures_dir, dpi)),
        ("lbbd_candidate_bounds", lambda: _plot_lbbd_candidate_bounds(run_dir, figures_dir, dpi)),
        ("lbbd_infrastructure_evolution", lambda: _plot_lbbd_infrastructure_evolution(run_dir, figures_dir, dpi)),
        ("lbbd_iteration_timing", lambda: _plot_lbbd_iteration_timing(run_dir, figures_dir, dpi)),
        ("lbbd_gap_diagnostics", lambda: _plot_lbbd_gap_diagnostics(run_dir, figures_dir, dpi)),
        ("lbbd_adaptive_master_control", lambda: _plot_lbbd_adaptive_master_control(run_dir, figures_dir, dpi)),
        ("lbbd_candidate_reuse", lambda: _plot_lbbd_candidate_reuse(run_dir, figures_dir, dpi)),
        ("slack", lambda: _plot_slack(results_dir, figures_dir, dpi)),
    ]
    if geometry_path is not None and geometry_path.exists():
        tasks.append(("spatial_maps", lambda: _plot_maps(
            results_dir,
            figures_dir,
            geometry_path,
            dpi,
            max_flow_arcs,
            redirection_month=redirection_map_month,
            basemap_alpha=basemap_alpha,
        )))

    records = []
    for name, task in tasks:
        try:
            files = task()
            records.append({"figure_group": name, "status": "generated", "files": ";".join(files), "message": ""})
            print(f"Figure generated: {name}")
        except (ValueError, FileNotFoundError) as exc:
            records.append({"figure_group": name, "status": "skipped", "files": "", "message": str(exc)})
            print(f"Figure skipped: {name} ({exc})")
        except Exception as exc:
            records.append({"figure_group": name, "status": "failed", "files": "", "message": f"{type(exc).__name__}: {exc}"})
            print(f"WARNING: Figure failed: {name} ({exc})")
            (figures_dir / f"ERROR_{name}.txt").write_text(traceback.format_exc(), encoding="utf-8")
    if geometry_path is None or not geometry_path.exists():
        records.append({"figure_group": "spatial_maps", "status": "skipped", "files": "", "message": "Parking/hex geometry path unavailable"})
    manifest = pd.DataFrame(records)
    manifest.to_csv(figures_dir / "figures_manifest.csv", index=False)
    _write_figures_readme(figures_dir)
    print(f"Figures written to: {figures_dir}")
    return manifest


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate publication-quality figures from an existing optimization run folder.")
    parser.add_argument("--run-dir", required=True)
    parser.add_argument("--project-root", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--dataset", choices=["small", "full"], default=None)
    parser.add_argument("--parking-shapefile", default=None)
    parser.add_argument("--dpi", type=int, default=300)
    parser.add_argument("--max-flow-arcs", type=int, default=150)
    parser.add_argument("--redirection-map-month", choices=MONTHS, default="June")
    parser.add_argument("--basemap-alpha", type=float, default=0.28)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    generate_run_figures(
        run_dir=args.run_dir,
        project_root=args.project_root,
        dataset=args.dataset,
        parking_shapefile=args.parking_shapefile,
        dpi=max(100, int(args.dpi)),
        max_flow_arcs=max(1, int(args.max_flow_arcs)),
        redirection_map_month=args.redirection_map_month,
        basemap_alpha=min(1.0, max(0.0, float(args.basemap_alpha))),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
