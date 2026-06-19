from __future__ import annotations

import math
from pyomo.environ import (
    Any,
    Binary,
    ConcreteModel,
    Constraint,
    ConstraintList,
    NonNegativeIntegers,
    NonNegativeReals,
    Objective,
    Param,
    Set,
    Var,
    maximize,
    quicksum,
    value,
)

from .lbbd_master_stage1 import compute_theta_upper_bounds


def _safe_value(obj, default: float = 0.0) -> float:
    try:
        v = value(obj, exception=False)
        return default if v is None else float(v)
    except Exception:
        return default


def build_stage4_master(data: dict, cfg: dict, scenario: str):
    """Stage 4 master: charger infrastructure + PV + BESS operation + local service
    + redirection interface. Redirection remains decomposed by month-time slot.

    BESS is kept in the master to preserve the 12-month linked representative-day SoC
    structure. The redirection subproblem remains a slot-wise type-aware recourse model.
    Redirected energy is conservatively costed as grid-supplied in the redirection
    subproblem; local non-redirected charging can use grid, direct PV, and BESS discharge.
    """
    if scenario not in {"with_redirection", "no_redirection"}:
        raise ValueError(f"Unsupported scenario: {scenario}")

    m = ConcreteModel()
    I = data["hex_ids"]
    M = data["MONTHS"]
    H = data["INTERVALS"]
    Hsoc = data["HSOC"]
    C = data["PUB_TYPES"]
    B = data["DEMAND_CLASSES"]

    m.I = Set(initialize=I)
    m.M = Set(initialize=M)
    m.H = Set(initialize=H)
    m.Hsoc = Set(initialize=Hsoc)
    m.C_pub = Set(initialize=C)
    m.B = Set(initialize=B)

    m.Price = Param(m.C_pub, initialize=data["charger_price"])
    m.Demand = Param(m.I, m.M, m.H, m.B, initialize=data["demand_event_annual"], within=NonNegativeReals)
    m.K = Param(m.C_pub, initialize=data["charger_capacity_pub"])
    m.Footprint = Param(m.C_pub, initialize=data["charger_footprint"])
    m.PVF_cost = Param(m.C_pub, initialize=lambda mm, c: data["daily_cost"][c])
    m.PVF_PV = Param(initialize=data["daily_cost"]["PV"])
    m.PVF_Batt = Param(initialize=data["daily_cost"]["Batt"])
    m.CL = Param(m.I, initialize=data["cl"])
    m.tou = Param(m.M, m.H, initialize=lambda mm, mon, t: data["tou"][mon][t], mutable=False)
    m.Ndays = Param(m.M, initialize=lambda mm, mon: data["N_MONTH"][mon])
    m.PV_panel_cap = Param(initialize=data["pv_kwh_per_panel_slot_at_cf1"])
    m.p_pv = Param(m.M, m.H, initialize=lambda mm, mon, t: data["pv_cf"][mon][t], mutable=False)
    m.PV_upper = Param(m.I, initialize=data["pv_upper"])

    m.Batt_cell_cap = Param(initialize=float(cfg["battery_cell_cap_kwh"]))
    m.eta_ch = Param(initialize=float(cfg["eta_charge"]))
    m.eta_dis = Param(initialize=float(cfg["eta_discharge"]))
    m.alpha_soc = Param(initialize=float(cfg["initial_soc_fraction"]))
    m.beta_min_soc = Param(initialize=float(cfg["soc_min_fraction"]))
    m.beta_max_soc = Param(initialize=float(cfg["soc_max_fraction"]))
    m.K_batt = Param(initialize=data["K_BATT"])
    m.M_batt = Param(m.I, initialize=lambda mm, i: data["M_BATT"][int(i)], within=NonNegativeReals)
    m.prev_mon = Param(m.M, initialize=data["prev_month"], within=Any)

    theta_ub = compute_theta_upper_bounds(data, cfg)

    def x_bounds(mm, i, c):
        return (0, int(math.floor(float(data["cl"][int(i)]) / float(data["charger_footprint"][c]))))

    def pv_bounds(mm, i):
        return (0, int(math.floor(float(data["pv_upper"].get(int(i), 0)))))

    def batt_bounds(mm, i):
        return (0, int(cfg["battery_max_units_per_hex"]))

    def theta_bounds(mm, mon, t):
        return (0.0, theta_ub[(mon, int(t))])

    m.x = Var(m.I, m.C_pub, domain=NonNegativeIntegers, bounds=x_bounds)
    m.PV = Var(m.I, domain=NonNegativeIntegers, bounds=pv_bounds)
    m.Batt = Var(m.I, domain=NonNegativeIntegers, bounds=batt_bounds)
    m.e_home = Var(m.I, m.M, m.H, m.C_pub, domain=NonNegativeReals)
    m.q = Var(m.I, m.M, m.H, m.C_pub, domain=NonNegativeReals)
    m.R = Var(m.I, m.M, m.H, m.C_pub, domain=NonNegativeReals)
    m.S = Var(m.I, m.M, m.H, m.C_pub, domain=NonNegativeReals)
    m.grid_dir = Var(m.I, m.M, m.H, domain=NonNegativeReals)
    m.grid_batt = Var(m.I, m.M, m.H, domain=NonNegativeReals)
    m.pv_dir = Var(m.I, m.M, m.H, domain=NonNegativeReals)
    m.pv_batt = Var(m.I, m.M, m.H, domain=NonNegativeReals)
    m.batt_discharge = Var(m.I, m.M, m.H, domain=NonNegativeReals)
    m.soc = Var(m.I, m.M, m.Hsoc, domain=NonNegativeReals)
    m.delta = Var(m.I, m.M, m.H, domain=Binary)
    m.slack = Var(m.I, m.M, m.H, m.B, domain=NonNegativeReals)
    m.ThetaRedir = Var(m.M, m.H, domain=NonNegativeReals, bounds=theta_bounds)
    m.BendersCuts = ConstraintList()

    def public_limit(mm, i):
        return quicksum(mm.Footprint[c] * mm.x[i, c] for c in mm.C_pub) <= mm.CL[i]

    m.PublicLimit = Constraint(m.I, rule=public_limit)

    def pv_upper_bound(mm, i):
        return mm.PV[i] <= mm.PV_upper[i]

    m.PVUpperBound = Constraint(m.I, rule=pv_upper_bound)

    def batt_cap_rule(mm, i):
        return mm.Batt[i] <= int(cfg["battery_max_units_per_hex"])

    m.BattCap = Constraint(m.I, rule=batt_cap_rule)

    def home_cover(mm, i, mon, t):
        return quicksum(mm.e_home[i, mon, t, c] for c in mm.C_pub) + mm.slack[i, mon, t, "home"] == mm.Demand[i, mon, t, "home"]

    m.HomeDemandCover = Constraint(m.I, m.M, m.H, rule=home_cover)

    def public_origin_allocation(mm, i, mon, t):
        return quicksum(mm.q[i, mon, t, c] for c in mm.C_pub) + mm.slack[i, mon, t, "public"] == mm.Demand[i, mon, t, "public"]

    m.PublicOriginAllocation = Constraint(m.I, m.M, m.H, rule=public_origin_allocation)

    def redirectable_bound(mm, i, mon, t, c):
        return mm.R[i, mon, t, c] <= mm.q[i, mon, t, c]

    m.RedirectableBound = Constraint(m.I, m.M, m.H, m.C_pub, rule=redirectable_bound)

    def type_capacity_interface(mm, i, mon, t, c):
        local_public = mm.q[i, mon, t, c] - mm.R[i, mon, t, c]
        return mm.e_home[i, mon, t, c] + local_public + mm.S[i, mon, t, c] <= mm.K[c] * mm.x[i, c]

    m.TypeCapacityInterface = Constraint(m.I, m.M, m.H, m.C_pub, rule=type_capacity_interface)

    def energy_balance(mm, i, mon, t):
        local_energy = quicksum(mm.e_home[i, mon, t, c] + mm.q[i, mon, t, c] - mm.R[i, mon, t, c] for c in mm.C_pub)
        return mm.grid_dir[i, mon, t] + mm.pv_dir[i, mon, t] + mm.batt_discharge[i, mon, t] == local_energy

    m.EnergyBalance = Constraint(m.I, m.M, m.H, rule=energy_balance)

    def pv_generation(mm, i, mon, t):
        return mm.pv_dir[i, mon, t] + mm.pv_batt[i, mon, t] <= mm.PV_panel_cap * mm.PV[i] * mm.p_pv[mon, t]

    m.PVGeneration = Constraint(m.I, m.M, m.H, rule=pv_generation)

    last_h = max(data["INTERVALS"])

    def battery_initial_january(mm, i):
        return mm.soc[i, "January", 0] == mm.alpha_soc * mm.Batt_cell_cap * mm.Batt[i]

    m.BatteryInitialJanuary = Constraint(m.I, rule=battery_initial_january)

    def battery_month_link(mm, i, mon):
        if mon == "January":
            return Constraint.Skip
        return mm.soc[i, mon, 0] == mm.soc[i, mm.prev_mon[mon], last_h]

    m.BatteryMonthLink = Constraint(m.I, m.M, rule=battery_month_link)

    def battery_dynamics(mm, i, mon, t):
        charge = mm.eta_ch * (mm.grid_batt[i, mon, t] + mm.pv_batt[i, mon, t])
        discharge = (1.0 / mm.eta_dis) * mm.batt_discharge[i, mon, t]
        return mm.soc[i, mon, t] == mm.soc[i, mon, t - 1] + charge - discharge

    m.BatteryDynamics = Constraint(m.I, m.M, m.H, rule=battery_dynamics)

    def batt_charge_throughput(mm, i, mon, t):
        return mm.grid_batt[i, mon, t] + mm.pv_batt[i, mon, t] <= mm.K_batt * mm.Batt[i]

    m.BattChargeThroughput = Constraint(m.I, m.M, m.H, rule=batt_charge_throughput)

    def batt_discharge_throughput(mm, i, mon, t):
        return mm.batt_discharge[i, mon, t] <= mm.K_batt * mm.Batt[i]

    m.BattDischargeThroughput = Constraint(m.I, m.M, m.H, rule=batt_discharge_throughput)

    def charge_only(mm, i, mon, t):
        return mm.grid_batt[i, mon, t] + mm.pv_batt[i, mon, t] <= mm.M_batt[i] * mm.delta[i, mon, t]

    m.ChargeOnly = Constraint(m.I, m.M, m.H, rule=charge_only)

    def discharge_only(mm, i, mon, t):
        return mm.batt_discharge[i, mon, t] <= mm.M_batt[i] * (1 - mm.delta[i, mon, t])

    m.DischargeOnly = Constraint(m.I, m.M, m.H, rule=discharge_only)

    def battery_capacity_upper(mm, i, mon, ell):
        return mm.soc[i, mon, ell] <= mm.beta_max_soc * mm.Batt_cell_cap * mm.Batt[i]

    m.BatteryCapacityUpper = Constraint(m.I, m.M, m.Hsoc, rule=battery_capacity_upper)

    def battery_capacity_lower(mm, i, mon, ell):
        return mm.soc[i, mon, ell] >= mm.beta_min_soc * mm.Batt_cell_cap * mm.Batt[i]

    m.BatteryCapacityLower = Constraint(m.I, m.M, m.Hsoc, rule=battery_capacity_lower)

    if data.get("disable_pv", False):
        for idx in m.PV:
            m.PV[idx].fix(0)
        for idx in m.pv_dir:
            m.pv_dir[idx].fix(0.0)
        for idx in m.pv_batt:
            m.pv_batt[idx].fix(0.0)

    if scenario == "no_redirection":
        for idx in m.R:
            m.R[idx].fix(0.0)
        for idx in m.S:
            m.S[idx].fix(0.0)
        for idx in m.ThetaRedir:
            m.ThetaRedir[idx].fix(0.0)

    days = data["DAYS"]
    penalty = float(cfg["penalty_per_kwh_slack"])

    def annual_profit(mm):
        local_revenue = quicksum(
            mm.Ndays[mon] * mm.Price[c] * (mm.e_home[i, mon, t, c] + mm.q[i, mon, t, c] - mm.R[i, mon, t, c])
            for i in mm.I for mon in mm.M for t in mm.H for c in mm.C_pub
        )
        grid_cost = quicksum(
            mm.Ndays[mon] * mm.tou[mon, t] * (mm.grid_dir[i, mon, t] + mm.grid_batt[i, mon, t])
            for i in mm.I for mon in mm.M for t in mm.H
        )
        slack_cost = penalty * quicksum(
            mm.Ndays[mon] * mm.slack[i, mon, t, b]
            for i in mm.I for mon in mm.M for t in mm.H for b in mm.B
        )
        capex_chargers = days * quicksum(mm.PVF_cost[c] * mm.x[i, c] for i in mm.I for c in mm.C_pub)
        capex_pv = days * quicksum(mm.PVF_PV * mm.PV[i] for i in mm.I)
        capex_batt = days * quicksum(mm.PVF_Batt * mm.Batt[i] for i in mm.I)
        redirection_proxy = quicksum(mm.ThetaRedir[mon, t] for mon in mm.M for t in mm.H)
        return local_revenue - grid_cost - slack_cost - capex_chargers - capex_pv - capex_batt + redirection_proxy

    m.obj = Objective(rule=annual_profit, sense=maximize)
    m._stage4_data = data
    m._stage4_cfg = cfg
    m._stage4_theta_ub = theta_ub
    return m


def extract_stage4_interface(model) -> dict[str, dict]:
    R: dict[tuple[int, str, int, str], float] = {}
    S: dict[tuple[int, str, int, str], float] = {}
    theta: dict[tuple[str, int], float] = {}
    for i in model.I:
        for mon in model.M:
            for t in model.H:
                for c in model.C_pub:
                    R[(int(i), str(mon), int(t), str(c))] = max(0.0, _safe_value(model.R[i, mon, t, c]))
                    S[(int(i), str(mon), int(t), str(c))] = max(0.0, _safe_value(model.S[i, mon, t, c]))
    for mon in model.M:
        for t in model.H:
            theta[(str(mon), int(t))] = max(0.0, _safe_value(model.ThetaRedir[mon, t]))
    return {"R": R, "S": S, "theta": theta}


def evaluate_stage4_base_objective(model) -> float:
    theta_total = sum(_safe_value(model.ThetaRedir[mon, t]) for mon in model.M for t in model.H)
    return _safe_value(model.obj) - theta_total


def add_stage4_dual_cut(model, mon: str, t: int, alpha: dict[tuple[int, str], float], beta: dict[tuple[int, str], float]) -> int:
    expr = 0.0
    nz = 0
    for (i, co), val in alpha.items():
        if abs(val) > 1e-9:
            expr += float(val) * model.R[int(i), mon, int(t), str(co)]
            nz += 1
    for (j, cd), val in beta.items():
        if abs(val) > 1e-9:
            expr += float(val) * model.S[int(j), mon, int(t), str(cd)]
            nz += 1
    model.BendersCuts.add(model.ThetaRedir[mon, int(t)] <= expr)
    return nz
