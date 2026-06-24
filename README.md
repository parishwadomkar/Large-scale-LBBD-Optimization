# Large-Scale EV Charging Infrastructure Optimization

## PV- and BESS-enabled public EV charging with user redirection

This repository implements a Pyomo/Gurobi optimization framework for planning public EV charging infrastructure with co-located photovoltaic (PV) generation, battery energy storage systems (BESS), and incentive-based short-range user redirection. The model is designed from the perspective of a charging point operator (CPO) and maximizes annual net profit while satisfying spatiotemporal charging demand.

The full-scale type-aware redirection problem is solved with a **Logic-Based Benders Decomposition (LBBD)** workflow. A monolithic formulation is also retained for small-scale validation and benchmark comparisons.

Charging demand is generated externally using the MATSim-based simulation framework [`UrbanEV-v2`](https://github.com/parishwadomkar/UrbanEV-v2) and aggregated to spatial planning cells, representative monthly days, and half-hour intervals.

<p align="center">
  <img src="./assets/Considerations.png" alt="Integrated EV charging, PV, BESS, and redirection planning scope" width="85%">
</p>

<p align="center"><em>Conceptual scope of the integrated charger–PV–BESS–redirection planning problem.</em></p>

---

## Model scope

The framework jointly represents:

- public charger deployment by charger type;
- PV and BESS sizing at candidate spatial cells;
- grid procurement, PV self-consumption, BESS charging/discharging, and linked monthly SoC dynamics;
- residual home demand served locally by public chargers;
- type-aware public charging redirection across eligible short-distance cell pairs;
- redirection incentive costs and tariff-compensation accounting;
- annualized charger, PV, and BESS investment costs.

The model is intended for strategic city-scale planning. It does not model private home-charger investment, upstream grid reinforcement, parcel-level permitting, or real-time user acceptance behavior.

<p align="center">
  <img src="./assets/LBBD.png" alt="Logic-Based Benders Decomposition workflow" width="70%">
</p>

<p align="center"><em>LBBD workflow used for the city-scale optimization problem.</em></p>

---

## Implemented workflows

| Workflow | Location | Intended use |
|---|---|---|
| Monolithic MILP | `src/` | Full/Small-instance validation, scenario checks, and comparison against LBBD outputs. |
| LBBD | `src_lbbd/` | Full/small-scale optimization with type-aware redirection. Recommended for city-scale runs. |

In the LBBD workflow, charger, PV, BESS, local energy dispatch, and SoC-linking constraints are retained in the master problem. Redirection is evaluated through slot-wise LP/MIP recourse models, and violated Benders cuts are added iteratively.

Available cut strategies are:

| Strategy | Description | Typical use |
|---|---|---|
| `standard` | Standard slot-wise LP-dual cuts. | Baseline and debugging. |
| `corepoint` | Core-point / Pareto-style dual cut selection. | Recommended for full-scale runs. |
| `mw`, `pareto` | Compatibility aliases mapped to the core-point strategy. | Legacy experiment names. |

---

## Input data

A typical `config/paths.json` points to files under `data/raw/small/` and `data/raw/full/`:

```text
demandHexGrid_optimization*.gpkg
CharPark*.shp
shortestpath*.csv
spot_prices*.csv
pvgis*.csv
```

The demand file provides aggregated charging demand by cell, month, half-hour interval, and charging context. Parking and land-use files define installation bounds. Shortest-path distances define eligible redirection arcs. Spot-price and PVGIS files provide time-varying electricity and solar-generation inputs.

---

## Installation

Create and activate a Python environment:

```powershell
conda create -n opti python=3.12
conda activate opti
```

Install the Python packages:

```powershell
conda install -c conda-forge geopandas pyogrio shapely pyproj fiona
python -m pip install -r requirements_opti.txt
```

Gurobi must be installed and licensed locally. Verify that Pyomo can access Gurobi before running large cases:

```powershell
python -c "import pyomo.environ as pyo; print(pyo.SolverFactory('gurobi').available())"
```

---

## Optimization runs

Run all commands from the project root.

Small LBBD validation:

```powershell
python src_lbbd\run_lbbd.py --dataset small --scenario with_redirection --preset small_validation --threads 10 --cut-strategy corepoint --mip-reconstruction-frequency 2
```

Small monolithic validation:

```powershell
python src\run_optimization.py --dataset small --scenario with_redirection --threads 10 --mip-gap 0.001
```

Full LBBD run:

```powershell
python src_lbbd\run_lbbd.py --dataset full --scenario with_redirection --preset full_strict --threads 16 --cut-strategy corepoint --mip-reconstruction-frequency 2
```

### Scenario and technology switches

| Option | Values / usage | Effect |
|---|---|---|
| `--dataset` | `small`, `full` | Selects input data from `config/paths.json`. |
| `--scenario` | `no_redirection`, `with_redirection` | Enables or disables redirection. |
| `--disable-pv` | flag | Removes PV investment and dispatch. |
| `--disable-bess` | flag | Removes BESS investment, dispatch, and SoC dynamics. |
| `--hard-no-slack` | flag | Enforces zero slack where supported; mainly for validated feasible cases. |

Common scenario modifiers:

| Scenario | Command modifier |
|---|---|
| No PV, no BESS, no redirection | `--scenario no_redirection --disable-pv --disable-bess` |
| No PV, no BESS, with redirection | `--scenario with_redirection --disable-pv --disable-bess` |
| PV only, no redirection | `--scenario no_redirection --disable-bess` |
| PV only, with redirection | `--scenario with_redirection --disable-bess` |
| BESS only, no redirection | `--scenario no_redirection --disable-pv` |
| BESS only, with redirection | `--scenario with_redirection --disable-pv` |
| PV + BESS, no redirection | `--scenario no_redirection` |
| PV + BESS, with redirection | `--scenario with_redirection` |

### Presets and solver controls

| Option | Values / usage | Effect |
|---|---|---|
| `--preset` | `small_validation`, `full_default`, `full_strict` | Applies predefined validation or full-scale run settings. |
| `--threads` | integer | Number of Gurobi threads. |
| `--time-limit` | seconds | Solver time limit. |
| `--master-gap` | float | Relative MIP gap for the LBBD master. |
| `--subproblem-gap` | float | Relative MIP gap for integer redirection reconstruction. |
| `--lbbd-gap` | float | LBBD convergence tolerance. |
| `--max-iterations` | integer | Maximum LBBD iterations. |
| `--mip-gap` | float | Monolithic MIP gap; also retained as a compatibility alias where supported. |

Preset guidance:

| Preset | Intended use |
|---|---|
| `small_validation` | Debugging, validation against monolithic results, and export checks. |
| `full_default` | Standard full-data LBBD runs. |
| `full_strict` | Tighter full-data runs after data and model validation. |

### LBBD acceleration options

| Option | Values / usage | Effect |
|---|---|---|
| `--cut-strategy` | `standard`, `corepoint`, `mw`, `pareto` | Selects the redirection cut-generation strategy. |
| `--max-cuts-per-iteration` | integer | Limits each iteration to the most violated cuts. |
| `--min-cut-violation` | float | Filters weakly violated cuts. |
| `--mip-reconstruction-frequency` | integer | Solves integer redirection reconstruction every `K` iterations. |
| `--core-weight` | float | Moving-average weight for the core/reference point. |
| `--core-floor-kwh` | float | Positive floor for core-point supply and spare-capacity values. |
| `--pareto-tolerance` | float | Tolerance for the auxiliary Pareto/core-point dual-face restriction. |

Ablation run without PV or BESS:

```powershell
python src_lbbd\run_lbbd.py --dataset full --scenario with_redirection --preset full_default --threads 16 --disable-pv --disable-bess --cut-strategy corepoint
```

Example no-redirection PV+BESS baseline:

```powershell
python src_lbbd\run_lbbd.py --dataset full --scenario no_redirection --preset full_default --threads 16
```

---

## Outputs

Main result files (in runs folder):

| File | Contents |
|---|---|
| `results/run_summary.csv` | Run-level objective, gap, technology, and status summary. |
| `results/quality_checks.csv` | Automated feasibility and consistency checks. |
| `results/model_summary.csv` | Economic, energy, infrastructure, and capacity metrics. |
| `results/infrastructure_by_hex.csv` | Cell-level charger, PV, BESS, footprint, and capacity outputs. |
| `results/energy_by_charger_type.csv` | Annual served energy and utilization by charger type. |
| `results/redirections.csv` | Redirected energy by origin, destination, month, and slot. |
| `results/redirections_by_type.csv` | Type-aware origin/destination charger-type redirection flows. |
| `results/origin_type_allocation_or_benchmark_tariff.csv` | Origin-type tariff accounting data. |
| `results/hourly_energy.csv` | Cell-month-slot energy, PV, grid, BESS, and redirection values. |
| `results/slack.csv` | Nonzero slack values, if present. |
| `results/lbbd_iteration_history.csv` | LBBD upper/lower bound and cut progress. |
| `results/lbbd_subproblem_summary.csv` | Slot-wise LP/MIP recourse summaries. |
| `results/lbbd_cuts.csv` | Generated cut metadata. |
| `results/combined_results.xlsx` | Convenience workbook. CSV files remain authoritative for very large tables. |

---

## Reproducibility notes

The full type-aware redirection model is difficult to solve monolithically because redirection variables scale with active arc-slots and origin/destination charger-type pairs. The LBBD implementation avoids constructing all redirection variables in one model by solving compact slot-wise redirection subproblems and adding cuts to the master.

For this maximization model, the reported LBBD gap is computed from the master upper bound and the best feasible MIP reconstruction lower bound. Small nonzero gaps are expected unless both bounds coincide within the requested tolerance.

---

## Contact / support

**Omkar Parishwad**  
Urban Mobility Research Group  
Chalmers University of Technology  
Email: [omkarp@chalmers.se](mailto:omkarp@chalmers.se)

For issues, feature requests, or reproducibility questions, please open a GitHub issue in this repository.

---

## Associated articles and data sources

### Charging infrastructure optimization

**Parishwad, Omkar; Najafi, Arsalan; Gao, Kun** — *Joint optimization of charging infrastructure and renewable energies with battery storage considering user redirection incentives.*  
[SSRN preprint](https://doi.org/10.2139/ssrn.5395539)

### Demand simulation source

Charging-demand inputs are based on the MATSim-driven simulation framework [`UrbanEV-v2`](https://github.com/parishwadomkar/UrbanEV-v2).

Published demand-modeling article:

**Parishwad, Omkar; Gao, Kun; Najafi, Arsalan** — *Integrated and Agent-Based Charging Demand Prediction Considering Cost-Aware and Adaptive Charging Behavior*. **Transportation Research Part D: Transport and Environment**, 154 (2026), 105285.  
DOI: <https://doi.org/10.1016/j.trd.2026.105285>
