========== FINAL LBBD PRODUCTION RUN ==========
Project root   : C:\Users\omkarp\Downloads\Opti
Dataset        : full
Scenario       : with_redirection
Technology     : PV enabled, BESS disabled
Preset         : full_trial
Master gap     : 0.002
Subproblem gap : 0.002
LBBD gap       : 0.00025
Max iterations : 25
Output logic   : one clean LBBD run folder
Cut strategy   : corepoint
MIP rec freq   : every 20 iterations
===============================================
Run folder     : C:\Users\omkarp\Downloads\Opti\runs\2026-06-23_172045_full_with_redirection_LBBD_PV_noBESS
Terminal log   : README_RUN.txt
Hex cells      : 638
Arc-slots      : 472,800
Building LBBD master model...
Acceleration       : core-point/Pareto dual cut selection enabled
MIP reconstruction : every 20 iterations, plus the first iteration and near-convergence iterations

========== LBBD ITERATION 1 ==========
Iteration 1: UB=958,543,027.589, MIP-LB=497,951,045.958, gap=92.497442%, LP_rec=0.000, MIP_rec=0.000, PV=65,471, Batt=0, cuts_added=576/576, max_violation=2,486,504.966713, strategy=corepoint

========== LBBD ITERATION 2 ==========
Iteration 2: UB=948,465,393.783, MIP-LB=497,951,045.958, gap=90.473622%, LP_rec=598,124.126, MIP_rec=skipped, PV=65,426, Batt=0, cuts_added=576/576, max_violation=2,481,404.889827, strategy=corepoint

========== LBBD ITERATION 3 ==========
Iteration 3: UB=517,377,624.220, MIP-LB=497,951,045.958, gap=3.901303%, LP_rec=5,497,233.242, MIP_rec=skipped, PV=65,287, Batt=0, cuts_added=576/576, max_violation=226,103.763059, strategy=corepoint

========== LBBD ITERATION 4 ==========
Iteration 4: UB=509,920,391.522, MIP-LB=497,951,045.958, gap=2.403719%, LP_rec=5,292,594.156, MIP_rec=skipped, PV=65,335, Batt=0, cuts_added=576/576, max_violation=143,654.706361, strategy=corepoint

========== LBBD ITERATION 5 ==========
Iteration 5: UB=501,172,575.658, MIP-LB=497,951,045.958, gap=0.646957%, LP_rec=4,315,600.037, MIP_rec=skipped, PV=65,330, Batt=0, cuts_added=564/564, max_violation=22,245.014893, strategy=corepoint

========== LBBD ITERATION 6 ==========
Iteration 6: UB=498,798,531.292, MIP-LB=497,951,045.958, gap=0.170195%, LP_rec=4,215,452.124, MIP_rec=4,214,116.340, PV=65,413, Batt=0, cuts_added=546/546, max_violation=13,044.238968, strategy=corepoint

========== LBBD ITERATION 7 ==========
Iteration 7: UB=498,634,310.332, MIP-LB=497,951,045.958, gap=0.137215%, LP_rec=4,463,029.379, MIP_rec=4,461,747.373, PV=65,355, Batt=0, cuts_added=531/531, max_violation=7,115.685564, strategy=corepoint

========== LBBD ITERATION 8 ==========
Iteration 8: UB=498,455,095.837, MIP-LB=498,145,333.264, gap=0.062183%, LP_rec=4,552,691.432, MIP_rec=4,551,215.185, PV=65,425, Batt=0, cuts_added=509/509, max_violation=8,839.807874, strategy=corepoint

========== LBBD ITERATION 9 ==========
Iteration 9: UB=498,655,557.212, MIP-LB=498,502,370.767, gap=0.030729%, LP_rec=3,704,315.768, MIP_rec=3,703,058.310, PV=65,467, Batt=0, cuts_added=465/465, max_violation=4,237.758579, strategy=corepoint

========== LBBD ITERATION 10 ==========
Iteration 10: UB=498,633,718.699, MIP-LB=498,551,746.682, gap=0.016442%, LP_rec=3,463,142.111, MIP_rec=3,461,952.684, PV=65,467, Batt=0, cuts_added=295/295, max_violation=2,554.288896, strategy=corepoint
Combined XLSX written to: C:\Users\omkarp\Downloads\Opti\runs\2026-06-23_172045_full_with_redirection_LBBD_PV_noBESS\results\combined_results.xlsx

========== LBBD SOLUTION SUMMARY ==========
Status                : converged
Iterations            : 10
Best MIP-LB SEK       : 498,551,746.682
LP upper bound SEK   : 498,633,718.699
LBBD gap            : 0.016442%
Cuts generated        : 5214
Cut strategy          : corepoint
MIP redirection rows  : 6296
PV panels installed   : 65,467
BESS units installed  : 0
Run folder            : C:\Users\omkarp\Downloads\Opti\runs\2026-06-23_172045_full_with_redirection_LBBD_PV_noBESS
==========================================

========== FINAL LBBD SUMMARY ==========
Status              : completed
Run folder          : C:\Users\omkarp\Downloads\Opti\runs\2026-06-23_172045_full_with_redirection_LBBD_PV_noBESS
Annual profit SEK   : 498551746.682475
LBBD gap pct        : 0.016442027709798853
PV panels installed : 65467.0
BESS units installed: 0.0
Slow/Medium/Fast    : 216.0 / 2216.0000000776226 / 173.000000511778
Redirected energy   : 1107640.288135255 kWh/yr
Failed checks       : 0
Summary file        : results/final_run_summary.csv
Quality checks      : results/final_quality_checks.csv
Terminal log        : README_RUN.txt
========================================
Run finished successfully. Run directory: C:\Users\omkarp\Downloads\Opti\runs\2026-06-23_172045_full_with_redirection_LBBD_PV_noBESS
