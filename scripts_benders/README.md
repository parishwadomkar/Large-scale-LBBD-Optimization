# Benders scenario scripts

These eight scripts cover every cold-start combination of redirection, PV, and BESS.
Calibrated solver and algorithm settings are loaded automatically from:

- `config/solver_gurobi.json`
- `config/run_profiles.json`

Run a script without an argument for the `full` dataset, or pass `small` as the first argument.

Example:

```bat
08_benders_PV_BESS_withRedirection.bat small
```

No previous run folder or external infrastructure solution is read.

Figures are generated automatically after a successful result export. Use `--skip-figures` only when post-processing should be disabled.

Same-method scenario comparisons are generated with the shared `scripts\10_compare_scenario_runs.bat` utility using `benders` as the method argument.
