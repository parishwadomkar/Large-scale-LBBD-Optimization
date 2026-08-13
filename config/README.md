# Configuration files

`solver_gurobi.json` contains settings shared by all methods. `run_profiles.json` contains calibrated method- and dataset-specific settings. Values supplied on the command line take precedence over both files.

Edit `run_profiles.json` when changing a standard small/full production profile. Reserve command-line overrides for experiments and sensitivities.

Figure generation is enabled by default in all run profiles (`skip_figures: false`). Each runner accepts `--skip-figures` as an explicit override.

`model_config.json` uses `charger_resources` for the relative installation-resource requirement of each public charger type. The numeric resource requirements are unchanged; this is a terminology-only revision.
