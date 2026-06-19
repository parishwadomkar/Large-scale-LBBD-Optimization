from __future__ import annotations

import math
from pyomo.environ import (
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


def _safe_value(obj, default: float = 0.0) -> float:
    try:
        v = value(obj, exception=False)
        return default if v is None else float(v)
    except Exception:
        return default


def compute_theta_upper_bounds(data: dict, cfg: dict) -> dict[tuple[str, int], float]:
    out: dict[tuple[str, int], float] = {}
    prices = data["charger_price"]
    delta = data["delta_price"]
    x_kwh = float(cfg["x_kwh_per_trip"])
    for mon in data["MONTHS"]:
        for t in data["INTERVALS"]:
            max_margin = 0.0
            for (i, j, m2, t2) in data["allowed_st"]:
                if m2 != mon or t2 != t:
                    continue
                dist_cost = data["T_dict"].get((int(i), int(j)), 0.0) / x_kwh
                for co in data["PUB_TYPES"]:
                    for cd in data["PUB_TYPES"]:
                        margin = prices[cd] - data["tou"][mon][t] - delta[(co, cd)] - dist_cost
                        if margin > max_margin:
                            max_margin = float(margin)
            public_demand = sum(float(data["demand_event_annual"][(i, mon, t, "public")]) for i in data["hex_ids"])
            out[(mon, t)] = max(0.0, data["N_MONTH"][mon] * max_margin * public_demand)
    return out


def build_stage1_master(data: dict, cfg: dict, scenario: str):
    """Build Stage 1 master: no-PV/no-BESS infrastructure + local energy + LP redirection interface.

    This master preserves charger-type-specific capacity, local home demand, public origin-type
    accounting, grid procurement, slack penalties, and charger CapEx. It removes explicit
    redirection variables and replaces them with R/S interface variables and ThetaRedir cuts.
    """
    if scenario not in {"with_redirection", "no_redirection"}:
        raise ValueError(f"Unsupported scenario: {scenario}")

    m = ConcreteModel()
    I = data["hex_ids"]
    M = data["MONTHS"]
    H = data["INTERVALS"]
    C = data["PUB_TYPES"]
    B = data["DEMAND_CLASSES"]

    m.I = Set(initialize=I)
    m.M = Set(initialize=M)
    m.H = Set(initialize=H)
    m.C_pub = Set(initialize=C)
    m.B = Set(initialize=B)

    m.Price = Param(m.C_pub, initialize=data["charger_price"])
    m.Demand = Param(m.I, m.M, m.H, m.B, initialize=data["demand_event_annual"], within=NonNegativeReals)
    m.K = Param(m.C_pub, initialize=data["charger_capacity_pub"])
    m.Footprint = Param(m.C_pub, initialize=data["charger_footprint"])
    m.PVF_cost = Param(m.C_pub, initialize=lambda mm, c: data["daily_cost"][c])
    m.CL = Param(m.I, initialize=data["cl"])
    m.tou = Param(m.M, m.H, initialize=lambda mm, mon, t: data["tou"][mon][t], mutable=False)
    m.Ndays = Param(m.M, initialize=lambda mm, mon: data["N_MONTH"][mon])

    theta_ub = compute_theta_upper_bounds(data, cfg)

    def x_bounds(mm, i, c):
        return (0, int(math.floor(float(data["cl"][int(i)]) / float(data["charger_footprint"][c]))))

    def theta_bounds(mm, mon, t):
        return (0.0, theta_ub[(mon, int(t))])

    m.x = Var(m.I, m.C_pub, domain=NonNegativeIntegers, bounds=x_bounds)
    m.e_home = Var(m.I, m.M, m.H, m.C_pub, domain=NonNegativeReals)
    m.q = Var(m.I, m.M, m.H, m.C_pub, domain=NonNegativeReals)
    m.R = Var(m.I, m.M, m.H, m.C_pub, domain=NonNegativeReals)
    m.S = Var(m.I, m.M, m.H, m.C_pub, domain=NonNegativeReals)
    m.grid_dir = Var(m.I, m.M, m.H, domain=NonNegativeReals)
    m.slack = Var(m.I, m.M, m.H, m.B, domain=NonNegativeReals)
    m.ThetaRedir = Var(m.M, m.H, domain=NonNegativeReals, bounds=theta_bounds)
    m.BendersCuts = ConstraintList()

    def public_limit(mm, i):
        return quicksum(mm.Footprint[c] * mm.x[i, c] for c in mm.C_pub) <= mm.CL[i]

    m.PublicLimit = Constraint(m.I, rule=public_limit)

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

    def grid_balance(mm, i, mon, t):
        return mm.grid_dir[i, mon, t] == quicksum(mm.e_home[i, mon, t, c] + mm.q[i, mon, t, c] - mm.R[i, mon, t, c] for c in mm.C_pub)

    m.GridBalance = Constraint(m.I, m.M, m.H, rule=grid_balance)

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
            mm.Ndays[mon] * mm.tou[mon, t] * mm.grid_dir[i, mon, t]
            for i in mm.I for mon in mm.M for t in mm.H
        )
        slack_cost = penalty * quicksum(
            mm.Ndays[mon] * mm.slack[i, mon, t, b]
            for i in mm.I for mon in mm.M for t in mm.H for b in mm.B
        )
        capex_chargers = days * quicksum(mm.PVF_cost[c] * mm.x[i, c] for i in mm.I for c in mm.C_pub)
        redirection_proxy = quicksum(mm.ThetaRedir[mon, t] for mon in mm.M for t in mm.H)
        return local_revenue - grid_cost - slack_cost - capex_chargers + redirection_proxy

    m.obj = Objective(rule=annual_profit, sense=maximize)
    m._stage1_data = data
    m._stage1_cfg = cfg
    m._stage1_theta_ub = theta_ub
    return m


def extract_stage1_interface(model) -> dict[str, dict]:
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


def evaluate_stage1_base_objective(model) -> float:
    theta_total = sum(_safe_value(model.ThetaRedir[mon, t]) for mon in model.M for t in model.H)
    return _safe_value(model.obj) - theta_total


def add_stage1_dual_cut(model, mon: str, t: int, alpha: dict[tuple[int, str], float], beta: dict[tuple[int, str], float]) -> int:
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
