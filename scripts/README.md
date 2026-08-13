# Monolithic scenario scripts

These eight scripts cover every cold-start combination of redirection, PV, and BESS.
Calibrated solver and algorithm settings are loaded automatically from:

- `config/solver_gurobi.json`
- `config/run_profiles.json`

Run a script without an argument for the `full` dataset, or pass `small` as the first argument.

Example:

```bat
08_monolithic_PV_BESS_withRedirection.bat small
```

No previous run folder or external infrastructure solution is read.

Figures are generated automatically after a successful result export. Use `--skip-figures` only when post-processing should be disabled.

## Same-method multi-scenario comparison

Use `10_compare_scenario_runs.bat` to compare two or more completed runs produced by the same method. The utility supports `monolithic`, `benders`, and `lbbd` and is independent of `09_compare_monolithic_benders_lbbd.bat`.

```bat
10_compare_scenario_runs.bat monolithic "runs\RUN_1" "runs\RUN_2" "runs\RUN_3"
```

The first run is the baseline by default. For custom labels or another baseline, call `src\compare_scenarios.py` directly with repeated `--run` / `--label` arguments and `--baseline-index`.
