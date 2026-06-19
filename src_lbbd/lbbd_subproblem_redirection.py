from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pyomo.environ as pyo


@dataclass
class SlotDualResult:
    month: str
    time_index: int
    objective: float
    alpha: dict[tuple[int, str], float]
    beta: dict[tuple[int, str], float]
    n_positive_type_arcs: int
    status: str
    termination: str


@dataclass
class SlotPrimalResult:
    month: str
    time_index: int
    objective: float
    flows: list[dict[str, Any]]
    status: str
    termination: str


def _solver_factory(solver_cfg: dict, log_file: Path | None = None, tee: bool = False):
    solver = pyo.SolverFactory("gurobi")
    opts = solver.options
    if solver_cfg.get("threads") is not None:
        opts["Threads"] = int(solver_cfg["threads"])
    if solver_cfg.get("mip_gap") is not None:
        opts["MIPGap"] = float(solver_cfg["mip_gap"])
    if solver_cfg.get("time_limit_seconds") is not None:
        opts["TimeLimit"] = int(solver_cfg["time_limit_seconds"])
    opts["OutputFlag"] = 1 if tee else 0
    if log_file is not None:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        opts["LogFile"] = str(log_file).replace("\\", "/")
    return solver


def _positive_type_arcs(data: dict, cfg: dict, mon: str, t: int) -> list[tuple[int, int, str, str, float]]:
    prices = data["charger_price"]
    delta = data["delta_price"]
    tou = float(data["tou"][mon][int(t)])
    x_kwh = float(cfg["x_kwh_per_trip"])
    ndays = float(data["N_MONTH"][mon])
    arcs = []
    for (i, j, m2, t2) in data["allowed_st"]:
        if m2 != mon or int(t2) != int(t):
            continue
        dist_cost_per_kwh = float(data["T_dict"].get((int(i), int(j)), 0.0)) / x_kwh
        for co in data["PUB_TYPES"]:
            for cd in data["PUB_TYPES"]:
                margin = float(prices[cd]) - tou - float(delta[(co, cd)]) - dist_cost_per_kwh
                coeff = ndays * margin
                if coeff > 1e-9:
                    arcs.append((int(i), int(j), str(co), str(cd), float(coeff)))
    return arcs


def solve_redirection_dual_lp(
    data: dict,
    cfg: dict,
    solver_cfg: dict,
    mon: str,
    t: int,
    R_values: dict[tuple[int, str, int, str], float],
    S_values: dict[tuple[int, str, int, str], float],
    log_dir: Path | None = None,
    pareto_core_R_values: dict[tuple[int, str, int, str], float] | None = None,
    pareto_core_S_values: dict[tuple[int, str, int, str], float] | None = None,
    pareto_tolerance: float = 1e-7,
) -> SlotDualResult:
    arcs = _positive_type_arcs(data, cfg, mon, int(t))
    if not arcs:
        return SlotDualResult(mon, int(t), 0.0, {}, {}, 0, "ok", "empty")

    origin_keys = sorted({(i, co) for (i, _j, co, _cd, _coef) in arcs})
    dest_keys = sorted({(j, cd) for (_i, j, _co, cd, _coef) in arcs})

    m = pyo.ConcreteModel()
    m.O = pyo.Set(dimen=2, initialize=origin_keys)
    m.D = pyo.Set(dimen=2, initialize=dest_keys)
    m.A = pyo.Set(dimen=4, initialize=[(i, j, co, cd) for (i, j, co, cd, _coef) in arcs])
    coeff = {(i, j, co, cd): coef for (i, j, co, cd, coef) in arcs}

    m.alpha = pyo.Var(m.O, domain=pyo.NonNegativeReals)
    m.beta = pyo.Var(m.D, domain=pyo.NonNegativeReals)

    def dual_feas(mm, i, j, co, cd):
        return mm.alpha[i, co] + mm.beta[j, cd] >= coeff[(int(i), int(j), str(co), str(cd))]

    m.DualFeas = pyo.Constraint(m.A, rule=dual_feas)

    def obj_rule(mm):
        return sum(R_values.get((int(i), mon, int(t), str(co)), 0.0) * mm.alpha[i, co] for (i, co) in mm.O) + sum(
            S_values.get((int(j), mon, int(t), str(cd)), 0.0) * mm.beta[j, cd] for (j, cd) in mm.D
        )

    m.obj = pyo.Objective(rule=obj_rule, sense=pyo.minimize)

    log_file = None
    if log_dir is not None:
        log_file = log_dir / f"dual_{mon}_{int(t):02d}.log"
    solver = _solver_factory(solver_cfg, log_file=log_file, tee=False)
    res = solver.solve(m, tee=False)
    term = str(res.solver.termination_condition).lower()
    status = str(res.solver.status).lower()
    if "optimal" not in term:
        raise RuntimeError(f"Redirection dual LP failed for {mon}, t={t}. status={status}, termination={term}")

    obj = float(pyo.value(m.obj, exception=False) or 0.0)

    # Optional Magnanti-Wong/core-point cut selection.  The first dual solve
    # obtains the exact LP recourse value at the current master interface.
    # If a core/reference point is supplied, solve a second dual LP over the
    # near-optimal dual face at the current point and choose the dual vector
    # that gives the smallest upper bound at the core point.  The resulting
    # cut remains valid because all dual-feasible multipliers define valid
    # upper cuts for the continuous redirection LP.
    if pareto_core_R_values is not None and pareto_core_S_values is not None and obj > 1e-9:
        current_expr = sum(R_values.get((int(i), mon, int(t), str(co)), 0.0) * m.alpha[i, co] for (i, co) in m.O) + sum(
            S_values.get((int(j), mon, int(t), str(cd)), 0.0) * m.beta[j, cd] for (j, cd) in m.D
        )
        core_expr = sum(pareto_core_R_values.get((int(i), mon, int(t), str(co)), 0.0) * m.alpha[i, co] for (i, co) in m.O) + sum(
            pareto_core_S_values.get((int(j), mon, int(t), str(cd)), 0.0) * m.beta[j, cd] for (j, cd) in m.D
        )
        try:
            m.CurrentPointNearOptimal = pyo.Constraint(expr=current_expr <= obj + max(1e-6, pareto_tolerance * max(1.0, abs(obj))))
            m.obj.deactivate()
            m.ParetoObj = pyo.Objective(expr=core_expr, sense=pyo.minimize)
            res2 = solver.solve(m, tee=False)
            term2 = str(res2.solver.termination_condition).lower()
            if "optimal" in term2:
                term = term + "+pareto"
            else:
                # Revert silently to the first dual solution if the auxiliary LP is numerically troublesome.
                m.ParetoObj.deactivate()
                m.obj.activate()
        except Exception:
            pass

    alpha = {(int(i), str(co)): max(0.0, float(pyo.value(m.alpha[i, co], exception=False) or 0.0)) for (i, co) in m.O}
    beta = {(int(j), str(cd)): max(0.0, float(pyo.value(m.beta[j, cd], exception=False) or 0.0)) for (j, cd) in m.D}
    obj_current = sum(R_values.get((int(i), mon, int(t), str(co)), 0.0) * alpha[(int(i), str(co))] for (i, co) in m.O) + sum(
        S_values.get((int(j), mon, int(t), str(cd)), 0.0) * beta[(int(j), str(cd))] for (j, cd) in m.D
    )
    return SlotDualResult(mon, int(t), float(obj_current), alpha, beta, len(arcs), status, term)


def solve_redirection_primal_lp(
    data: dict,
    cfg: dict,
    solver_cfg: dict,
    mon: str,
    t: int,
    R_values: dict[tuple[int, str, int, str], float],
    S_values: dict[tuple[int, str, int, str], float],
    log_dir: Path | None = None,
    flow_tol: float = 1e-7,
) -> SlotPrimalResult:
    arcs = _positive_type_arcs(data, cfg, mon, int(t))
    if not arcs:
        return SlotPrimalResult(mon, int(t), 0.0, [], "ok", "empty")

    origin_keys = sorted({(i, co) for (i, _j, co, _cd, _coef) in arcs})
    dest_keys = sorted({(j, cd) for (_i, j, _co, cd, _coef) in arcs})
    arc_keys = [(i, j, co, cd) for (i, j, co, cd, _coef) in arcs]
    coeff = {(i, j, co, cd): coef for (i, j, co, cd, coef) in arcs}

    m = pyo.ConcreteModel()
    m.O = pyo.Set(dimen=2, initialize=origin_keys)
    m.D = pyo.Set(dimen=2, initialize=dest_keys)
    m.A = pyo.Set(dimen=4, initialize=arc_keys)
    m.z = pyo.Var(m.A, domain=pyo.NonNegativeReals)

    by_origin: dict[tuple[int, str], list[tuple[int, int, str, str]]] = {k: [] for k in origin_keys}
    by_dest: dict[tuple[int, str], list[tuple[int, int, str, str]]] = {k: [] for k in dest_keys}
    for key in arc_keys:
        i, j, co, cd = key
        by_origin[(i, co)].append(key)
        by_dest[(j, cd)].append(key)

    def origin_cap(mm, i, co):
        return sum(mm.z[key] for key in by_origin[(int(i), str(co))]) <= R_values.get((int(i), mon, int(t), str(co)), 0.0)

    def dest_cap(mm, j, cd):
        return sum(mm.z[key] for key in by_dest[(int(j), str(cd))]) <= S_values.get((int(j), mon, int(t), str(cd)), 0.0)

    m.OriginCap = pyo.Constraint(m.O, rule=origin_cap)
    m.DestCap = pyo.Constraint(m.D, rule=dest_cap)
    m.obj = pyo.Objective(expr=sum(coeff[key] * m.z[key] for key in arc_keys), sense=pyo.maximize)

    log_file = None
    if log_dir is not None:
        log_file = log_dir / f"primal_{mon}_{int(t):02d}.log"
    solver = _solver_factory(solver_cfg, log_file=log_file, tee=False)
    res = solver.solve(m, tee=False)
    term = str(res.solver.termination_condition).lower()
    status = str(res.solver.status).lower()
    if "optimal" not in term:
        raise RuntimeError(f"Redirection primal LP failed for {mon}, t={t}. status={status}, termination={term}")

    ndays = float(data["N_MONTH"][mon])
    rows = []
    for key in arc_keys:
        val = float(pyo.value(m.z[key], exception=False) or 0.0)
        if val <= flow_tol:
            continue
        i, j, co, cd = key
        annual_value = coeff[key] * val
        rows.append({
            "from_HexID": int(i),
            "to_HexID": int(j),
            "Month": mon,
            "TimeIndex": int(t),
            "OriginType": str(co),
            "DestinationType": str(cd),
            "Energy_kWh_day": val,
            "Energy_kWh_annual": ndays * val,
            "AnnualNetValue_SEK": annual_value,
            "Coeff_SEK_per_kWh_annualized": coeff[key],
        })
    obj = float(pyo.value(m.obj, exception=False) or 0.0)
    return SlotPrimalResult(mon, int(t), obj, rows, status, term)


def solve_redirection_primal_mip(
    data: dict,
    cfg: dict,
    solver_cfg: dict,
    mon: str,
    t: int,
    R_values: dict[tuple[int, str, int, str], float],
    S_values: dict[tuple[int, str, int, str], float],
    log_dir: Path | None = None,
    flow_tol: float = 1e-7,
) -> SlotPrimalResult:
    """Solve the slot-wise type-aware redirection MIP with the monolithic trip-bundle
    structure: z = kappa*n_trip + tail, tail < kappa, Yarc activation, and a
    minimum positive redirected quantity when Yarc=1.
    """
    arcs_type = _positive_type_arcs(data, cfg, mon, int(t))
    if not arcs_type:
        return SlotPrimalResult(mon, int(t), 0.0, [], "ok", "empty")

    arc_keys = sorted({(i, j) for (i, j, _co, _cd, _coef) in arcs_type})
    atype_keys = [(i, j, co, cd) for (i, j, co, cd, _coef) in arcs_type]
    prices = data["charger_price"]
    delta = data["delta_price"]
    tou = float(data["tou"][mon][int(t)])
    ndays = float(data["N_MONTH"][mon])
    kappa = float(cfg["x_kwh_per_trip"])
    redir_min = float(cfg.get("redir_min_kwh", 0.0))

    # Annualized revenue/grid/price-compensation coefficient. Distance is represented
    # separately through n_trip and tail to preserve the monolithic formulation.
    coeff_no_dist = {(i, j, co, cd): ndays * (float(prices[cd]) - tou - float(delta[(co, cd)])) for (i, j, co, cd) in atype_keys}
    dist_cost = {(i, j): float(data["T_dict"].get((int(i), int(j)), 0.0)) for (i, j) in arc_keys}

    by_origin: dict[tuple[int, str], list[tuple[int, int, str, str]]] = {}
    by_dest: dict[tuple[int, str], list[tuple[int, int, str, str]]] = {}
    by_arc: dict[tuple[int, int], list[tuple[int, int, str, str]]] = {a: [] for a in arc_keys}
    for key in atype_keys:
        i, j, co, cd = key
        by_origin.setdefault((i, co), []).append(key)
        by_dest.setdefault((j, cd), []).append(key)
        by_arc[(i, j)].append(key)

    origin_keys = sorted(by_origin)
    dest_keys = sorted(by_dest)

    m = pyo.ConcreteModel()
    m.Arc = pyo.Set(dimen=2, initialize=arc_keys)
    m.AType = pyo.Set(dimen=4, initialize=atype_keys)
    m.O = pyo.Set(dimen=2, initialize=origin_keys)
    m.D = pyo.Set(dimen=2, initialize=dest_keys)

    m.zod = pyo.Var(m.AType, domain=pyo.NonNegativeReals)
    m.z = pyo.Var(m.Arc, domain=pyo.NonNegativeReals)
    m.Yarc = pyo.Var(m.Arc, domain=pyo.Binary)
    m.n_trip = pyo.Var(m.Arc, domain=pyo.NonNegativeIntegers)
    m.r_tail = pyo.Var(m.Arc, domain=pyo.NonNegativeReals)

    def origin_cap(mm, i, co):
        return sum(mm.zod[key] for key in by_origin[(int(i), str(co))]) <= R_values.get((int(i), mon, int(t), str(co)), 0.0)

    def dest_cap(mm, j, cd):
        return sum(mm.zod[key] for key in by_dest[(int(j), str(cd))]) <= S_values.get((int(j), mon, int(t), str(cd)), 0.0)

    def aggregate(mm, i, j):
        return mm.z[i, j] == sum(mm.zod[key] for key in by_arc[(int(i), int(j))])

    def min_activation(mm, i, j):
        return mm.z[i, j] >= redir_min * mm.Yarc[i, j]

    def cap_activation(mm, i, j):
        origin_cap_val = sum(R_values.get((int(i), mon, int(t), str(co)), 0.0) for co in data["PUB_TYPES"])
        dest_cap_val = sum(S_values.get((int(j), mon, int(t), str(cd)), 0.0) for cd in data["PUB_TYPES"])
        static_cap = float(data.get("M_REDIR", {}).get(int(j), max(origin_cap_val, dest_cap_val, redir_min)))
        cap = max(0.0, min(static_cap, origin_cap_val, dest_cap_val))
        return mm.z[i, j] <= cap * mm.Yarc[i, j]

    def trip_decomp(mm, i, j):
        return mm.z[i, j] == kappa * mm.n_trip[i, j] + mm.r_tail[i, j]

    def tail_upper(mm, i, j):
        return mm.r_tail[i, j] <= (kappa - 1e-6) * mm.Yarc[i, j]

    m.OriginCap = pyo.Constraint(m.O, rule=origin_cap)
    m.DestCap = pyo.Constraint(m.D, rule=dest_cap)
    m.Aggregate = pyo.Constraint(m.Arc, rule=aggregate)
    m.RedirMin = pyo.Constraint(m.Arc, rule=min_activation)
    m.RedirCap = pyo.Constraint(m.Arc, rule=cap_activation)
    m.TripDecomp = pyo.Constraint(m.Arc, rule=trip_decomp)
    m.TailUpper = pyo.Constraint(m.Arc, rule=tail_upper)

    m.obj = pyo.Objective(
        expr=sum(coeff_no_dist[key] * m.zod[key] for key in atype_keys)
        - sum(ndays * (dist_cost[(i, j)] * m.n_trip[i, j] + (dist_cost[(i, j)] / kappa) * m.r_tail[i, j]) for (i, j) in arc_keys),
        sense=pyo.maximize,
    )

    log_file = None
    if log_dir is not None:
        log_file = log_dir / f"mip_{mon}_{int(t):02d}.log"
    solver = _solver_factory(solver_cfg, log_file=log_file, tee=False)
    res = solver.solve(m, tee=False)
    term = str(res.solver.termination_condition).lower()
    status = str(res.solver.status).lower()
    if not ("optimal" in term or "feasible" in term or "time" in term):
        raise RuntimeError(f"Redirection MIP failed for {mon}, t={t}. status={status}, termination={term}")

    arc_stats: dict[tuple[int, int], dict[str, float]] = {}
    for (i, j) in arc_keys:
        zval = float(pyo.value(m.z[i, j], exception=False) or 0.0)
        yval = float(pyo.value(m.Yarc[i, j], exception=False) or 0.0)
        nval = float(pyo.value(m.n_trip[i, j], exception=False) or 0.0)
        rval = float(pyo.value(m.r_tail[i, j], exception=False) or 0.0)
        arc_stats[(i, j)] = {"z": zval, "Yarc": yval, "Trips_day": nval, "Tail_kWh_day": rval}

    rows = []
    for key in atype_keys:
        val = float(pyo.value(m.zod[key], exception=False) or 0.0)
        if val <= flow_tol:
            continue
        i, j, co, cd = key
        stats = arc_stats[(i, j)]
        ztot = max(stats["z"], 1e-12)
        share = val / ztot
        annual_gross = coeff_no_dist[key] * val
        annual_dist = ndays * (dist_cost[(i, j)] * stats["Trips_day"] + (dist_cost[(i, j)] / kappa) * stats["Tail_kWh_day"]) * share
        rows.append({
            "from_HexID": int(i),
            "to_HexID": int(j),
            "Month": mon,
            "TimeIndex": int(t),
            "OriginType": str(co),
            "DestinationType": str(cd),
            "Energy_kWh_day": val,
            "Energy_kWh_annual": ndays * val,
            "AnnualNetValue_SEK": annual_gross - annual_dist,
            "Coeff_SEK_per_kWh_annualized_excl_distance": coeff_no_dist[key],
            "Yarc": stats["Yarc"],
            "Trips_day": stats["Trips_day"] * share,
            "Tail_kWh_day": stats["Tail_kWh_day"] * share,
        })
    obj = float(pyo.value(m.obj, exception=False) or 0.0)
    return SlotPrimalResult(mon, int(t), obj, rows, status, term)
