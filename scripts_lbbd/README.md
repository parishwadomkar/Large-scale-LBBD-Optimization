# LBBD scenario scripts

Scripts `01`–`08` cover the cold-start combinations of redirection, PV, and BESS. Calibrated defaults are read from `config/solver_gurobi.json` and `config/run_profiles.json`.

Run a scenario script without an argument for the `full` dataset, or pass `small` as the first argument. Example:

```bat
08_lbbd_PV_BESS_withRedirection.bat small
```

`09_lbbd_full_HPC_withRedirection_PV_BESS.bat` is the production full-data cold-start command. It does not read a previous run, external investment layout, or saved bootstrap checkpoint. Its internal LP/bootstrap and MIP-start information is generated from the current data and current LBBD iterates only.

For the full profile, the outer target is `0.00025` (0.025%). The production script allows up to 12 LBBD iterations and 20 days as a safety ceiling. The solver initially prioritizes incumbent improvement; once the certified outer gap is within 0.1%, adaptive bound polishing switches the master to best-bound focus and activates the objective-bound stopping criterion.

Figures are generated automatically after a successful certified result export. Use `--skip-figures` only when post-processing should be disabled.

Same-method scenario comparisons are generated with the shared `scripts\10_compare_scenario_runs.bat` utility using `lbbd` as the method argument.


Diagnostic note: bootstrap and LP-fallback candidates are not master-MIP incumbents. Their bound-to-candidate differences are therefore not reported as achieved master MIP gaps. The adaptive-control figures plot genuine MIP gaps only and mark non-MIP candidate-generation iterations separately.
