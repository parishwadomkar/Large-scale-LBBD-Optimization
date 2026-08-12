# Configuration files

`solver_gurobi.json` contains settings shared by all methods. `run_profiles.json` contains calibrated method- and dataset-specific settings. Values supplied on the command line take precedence over both files.

Edit `run_profiles.json` when changing a standard small/full production profile. Reserve command-line overrides for experiments and sensitivities.

Figure generation is enabled by default in all run profiles (`skip_figures: false`). Each runner accepts `--skip-figures` as an explicit override.
