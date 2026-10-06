# Manuscript monolithic reruns

Run one case per HPC allocation with `scripts/run_monolithic_manuscript.ps1`.
The six principal cases are S01 (chargers only), S02 (chargers plus PV), and
S03 (chargers plus PV and BESS), each with `_NR` (no redirection) or `_R`
(redirection). S03_R is also the sensitivity baseline: 30 km/h car travel,
80 SEK/hour value of time, and 1.5 km maximum redirection distance. The
additional sensitivity cases are `S03_speed10`, `S03_speed20`, `S03_speed40`,
`S03_vot50`, `S03_vot100`, `S03_dist1p2`, and `S03_dist2p0`.

The script uses the full dataset, cold monolithic formulation, penalized slack,
10 solver threads, a 200 GB (decimal) Gurobi soft memory limit, 0.5 GB
`NodefileStart`, dual simplex at root and nodes, `PreSparsify=1`, `Cuts=1`,
relative `MIPGap=0.0002`, and 1,684,800 seconds of solver time (19.5 days).
The checked-in solver configuration also supplies `MIPFocus=1`,
`NumericFocus=2`, and `Heuristics=0.1`; record the effective Gurobi log
settings for each run.
The 12-hour difference from a 20-day HPC allocation leaves time for input
loading, model construction, and result export. Run from the same tagged
commit, environment, configuration, and input version. Place node files on a
fast local SSD; the default path is within the repository's `runs/` directory.
Do not launch multiple full jobs simultaneously on a 250 GB node.

Automatic figures are skipped so the optimization's measured end-to-end time
does not depend on basemap downloads. Generate manuscript figures later from
the selected run folders with `src/visualize_results.py`.

For each finished run, preserve the run folder's `README_RUN.txt`,
`logs/gurobi_run.log`, `results/solver_certificate.json`,
`results/model_summary.csv`, `results/slack.csv`,
`results/resource_usage.csv`, and `results/computational_complexity_scalars.csv`.
Record the tag and commit SHA, Gurobi/Pyomo/Python versions, input LFS object
identifiers, requested resource limits, actual termination, total runtime,
peak process-tree RSS, incumbent, global solver bound, and achieved MIP gap.

For maximization, an incumbent is a feasible lower bound L and Gurobi's
reported best bound is an upper bound U. The gap used here is
`max(0,U-L)/max(1,abs(L))`. A memory or time-limit exit with an incumbent is
useful evidence, but it has not met the requested convergence target unless
the reported achieved gap itself meets 0.0002. Verify `annual_slack_kWh` in
`model_summary.csv`, and reconcile any positive slack in `slack.csv` with its
penalty rather than treating slack as infeasibility.

For two scenario profits A and B, the defensible range for `A-B` is
`[L_A-U_B, U_A-L_B]`. If it straddles zero, the sign of their true objective
difference is unresolved. Replace manuscript numerical tables and sensitivity
ratios only after matching each reported value to its archived run and checking
these bound ranges. Do not combine figures from an older LBBD baseline with
these monolithic sensitivity runs.
