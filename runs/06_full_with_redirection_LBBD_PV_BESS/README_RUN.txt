(omkarp) PS C:\Users\omkarp\Downloads\Opti> python src_lbbd\run_lbbd_final.py --dataset full --scenario with_redirection --preset full_trial --threads 16 --master-gap 0.002 --subproblem-gap 0.002 --lbbd-gap 0.00025 --max-iterations 25 --time-limit 64800 --cut-strategy corepoint --mip-reconstruction-frequency 2
========== FINAL LBBD PRODUCTION RUN ==========
Project root   : C:\Users\omkarp\Downloads\Opti
Dataset        : full
Scenario       : with_redirection
Technology     : PV enabled, BESS enabled
Preset         : full_trial
Master gap     : 0.002
Subproblem gap : 0.002
LBBD gap       : 0.00025
Max iterations : 25
Output logic   : one clean LBBD run folder
Cut strategy   : corepoint
MIP rec freq   : every 2 iterations
===============================================
Run folder     : C:\Users\omkarp\Downloads\Opti\runs\2026-06-22_224533_full_with_redirection_LBBD_PV_BESS
Hex cells      : 638
Arc-slots      : 472,800
Building LBBD master model...
Acceleration       : core-point/Pareto dual cut selection enabled
MIP reconstruction : every 2 iterations, plus the first iteration and near-convergence iterations

========== LBBD ITERATION 1 ==========
Iteration 1: UB=962,948,284.713, MIP-LB=502,356,303.082, gap=91.686315%, LP_rec=0.000, MIP_rec=0.000, PV=78,938, Batt=2,472, cuts_added=576/576, max_violation=2,486,504.966713, strategy=corepoint

========== LBBD ITERATION 2 ==========
Iteration 2: UB=952,361,460.804, MIP-LB=502,356,303.082, gap=89.578882%, LP_rec=983,034.340, MIP_rec=982,600.035, PV=78,737, Batt=2,447, cuts_added=576/576, max_violation=2,469,185.931500, strategy=corepoint

========== LBBD ITERATION 3 ==========
Iteration 3: UB=519,883,446.546, MIP-LB=502,356,303.082, gap=3.488986%, LP_rec=5,178,599.827, MIP_rec=skipped, PV=78,479, Batt=2,446, cuts_added=576/576, max_violation=206,469.336583, strategy=corepoint

========== LBBD ITERATION 4 ==========
Iteration 4: UB=513,408,498.423, MIP-LB=502,356,303.082, gap=2.200071%, LP_rec=4,035,133.244, MIP_rec=4,033,678.994, PV=78,704, Batt=2,462, cuts_added=576/576, max_violation=123,794.551927, strategy=corepoint

========== LBBD ITERATION 5 ==========
Iteration 5: UB=505,337,937.066, MIP-LB=502,356,303.082, gap=0.593530%, LP_rec=5,154,715.442, MIP_rec=skipped, PV=78,703, Batt=2,455, cuts_added=564/564, max_violation=30,995.745201, strategy=corepoint

========== LBBD ITERATION 6 ==========
Iteration 6: UB=502,989,912.448, MIP-LB=502,356,303.082, gap=0.126127%, LP_rec=3,782,225.912, MIP_rec=3,780,627.289, PV=78,724, Batt=2,451, cuts_added=559/559, max_violation=24,658.877426, strategy=corepoint

========== LBBD ITERATION 7 ==========
Iteration 7: UB=503,141,626.379, MIP-LB=502,501,630.751, gap=0.127362%, LP_rec=3,475,134.520, MIP_rec=3,473,598.070, PV=78,733, Batt=2,454, cuts_added=533/533, max_violation=13,710.411175, strategy=corepoint

========== LBBD ITERATION 8 ==========
Iteration 8: UB=502,682,966.359, MIP-LB=502,501,630.751, gap=0.036087%, LP_rec=4,461,508.289, MIP_rec=4,460,247.144, PV=78,608, Batt=2,434, cuts_added=491/491, max_violation=16,802.506811, strategy=corepoint

========== LBBD ITERATION 9 ==========
Iteration 9: UB=502,927,484.520, MIP-LB=502,772,318.719, gap=0.030862%, LP_rec=3,161,196.304, MIP_rec=3,160,126.474, PV=78,712, Batt=2,450, cuts_added=404/404, max_violation=8,424.357289, strategy=corepoint

========== LBBD ITERATION 10 ==========
Iteration 10: UB=502,866,923.674, MIP-LB=502,772,318.719, gap=0.018817%, LP_rec=4,177,741.013, MIP_rec=4,176,735.169, PV=78,506, Batt=2,438, cuts_added=369/369, max_violation=4,858.562661, strategy=corepoint
Combined XLSX written to: C:\Users\omkarp\Downloads\Opti\runs\2026-06-22_224533_full_with_redirection_LBBD_PV_BESS\results\combined_results.xlsx

========== LBBD SOLUTION SUMMARY ==========
Status                : converged
Iterations            : 10
Best MIP-LB SEK       : 502,772,318.719
LP upper bound SEK   : 502,866,923.674
LBBD gap            : 0.018817%
Cuts generated        : 5224
Cut strategy          : corepoint
MIP redirection rows  : 6245
PV panels installed   : 78,506
BESS units installed  : 2,438
Run folder            : C:\Users\omkarp\Downloads\Opti\runs\2026-06-22_224533_full_with_redirection_LBBD_PV_BESS
==========================================

========== FINAL LBBD SUMMARY ==========
Status              : completed
Run folder          : C:\Users\omkarp\Downloads\Opti\runs\2026-06-22_224533_full_with_redirection_LBBD_PV_BESS
Annual profit SEK   : 501662323.9793718
LBBD gap pct        : 0.018816659595842444
PV panels installed : 78506.0
BESS units installed: 2438.0
Slow/Medium/Fast    : 225.0 / 2171.0 / 182.0
Redirected energy   : 1044181.5558624635 kWh/yr
Failed checks       : 0
Summary file        : results/final_run_summary.csv
Quality checks      : results/final_quality_checks.csv
========================================
Run finished successfully. Run directory: C:\Users\omkarp\Downloads\Opti\runs\2026-06-22_224533_full_with_redirection_LBBD_PV_BESS
=====================

This folder is produced by src_lbbd/run_lbbd_final.py. It uses the validated final LBBD formulation:
charger siting and sizing with optional PV and/or BESS switches in the master, with type-aware redirection handled through slot-wise LP/MIP recourse.

Core files:
- results/final_run_summary.csv: one-row thesis-facing summary.
- results/final_quality_checks.csv: automatic checks for LBBD gap, slack, and SoC linkage.
- results/model_summary.csv: detailed economic/energy/infrastructure metrics.
- results/infrastructure_by_hex.csv: charger/PV/BESS deployment by cell.
- results/redirections.csv and redirections_by_type.csv: reconstructed redirected flows.
- results/lbbd_iteration_history.csv: bound and cut progress per iteration.
- master/master_iter_*.log: Gurobi logs for each master solve.
- logs/final_manifest.json: run configuration and solver settings.

Scenario: with_redirection
Dataset: full
