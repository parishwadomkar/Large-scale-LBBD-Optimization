Monolithic optimization run folder
==================================

This folder is produced by src/run_optimization.py. It contains the outputs from the full monolithic Pyomo/Gurobi formulation.

Core files:
- README_RUN.txt: complete terminal transcript from this run.
- results/model_summary.csv: detailed economic, energy, and infrastructure metrics.
- results/infrastructure_by_hex.csv: charger/PV/BESS deployment by cell.
- results/redirections.csv and redirections_by_type.csv: optimized redirected flows.
- results/hourly_energy.csv: slot-level energy dispatch.
- logs/gurobi_run.log: Gurobi solver log.
- logs/pyomo_solve.log: Pyomo solve log.

Scenario: with_redirection
Dataset: small
Technology: PV enabled, BESS enabled
Sensitivity overrides: None
