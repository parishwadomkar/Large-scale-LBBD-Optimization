LBBD optimization
=================
Project root: C:\Users\omkarp\Downloads\Opti
Dataset: small
Run profile: lbbd.small
Scenario: with_redirection
Technology: withPV_withBESS
Method: embedded continuous recourse relaxation with LP cuts and exact annual MIP certification
Run directory: C:\Users\omkarp\Downloads\Opti\runs\2026-08-12_184349_small_with_redirection_LBBD_withPV_withBESS
Master solver memory mode: threads=32, root_method=auto, node_method=auto, nodefile_start=0.5 GB, soft_mem_limit=none GB
Hex cells: 57
Active redirection arc-slots: 57,600
Slot components: 11,640
Global redirection components: 12
Static origin-neighbourhood profit cuts: 0
Initial master size: 466,011 variables; 452,492 constraints
Adaptive master-gap control: initial 0.200000% -> tight 0.005000%
Internal master MIP start: slack-only feasible point loaded (Eta -539,435,277,458.976; setup 1.2s).
Iteration 01 | UB 127,037,382.560 | LB 126,832,594.926 | gap 0.161203% | candidate 126,832,594.926 | fixed gap 0.000049% | master optimal 0.1616% (requested 0.2000%) | cuts +0 Hall +0 comp-LP +0 annual-LP +0 config-MIP +0 partial-MIP | slow 93 medium 389 fast 41 PV 15059 BESS 326
Iteration 02 | UB 127,004,430.505 | LB 126,962,240.768 | gap 0.033219% | candidate 126,962,240.768 | fixed gap 0.000071% | master optimal 0.0331% (requested 0.0500%) | cuts +0 Hall +0 comp-LP +0 annual-LP +1 config-MIP +0 partial-MIP | slow 47 medium 419 fast 40 PV 15048 BESS 320
Iteration 03 | UB 126,993,953.763 | LB 126,987,822.329 | gap 0.004828% | candidate 126,987,822.329 | fixed gap 0.000001% | master optimal 0.0048% (requested 0.0125%) | cuts +0 Hall +0 comp-LP +0 annual-LP +1 config-MIP +0 partial-MIP | slow 67 medium 403 fast 41 PV 15114 BESS 320

Best certified incumbent
------------------------
Objective: 126,987,822.329 SEK/year
Best fixed-investment upper bound: 126,987,823.141 SEK/year
Global master upper bound: 126,993,953.763 SEK/year
Certified gap: 0.004828%
Termination: certified_gap
Output: C:\Users\omkarp\Downloads\Opti\runs\2026-08-12_184349_small_with_redirection_LBBD_withPV_withBESS
Combined XLSX written to: C:\Users\omkarp\Downloads\Opti\runs\2026-08-12_184349_small_with_redirection_LBBD_withPV_withBESS\results\combined_results.xlsx
Output files written to: C:\Users\omkarp\Downloads\Opti\runs\2026-08-12_184349_small_with_redirection_LBBD_withPV_withBESS\results
Generating result figures...
Figure generated: economic_breakdown
Figure generated: charger_deployment
Figure generated: monthly_energy
Figure generated: dispatch_January
Figure generated: dispatch_April
Figure generated: dispatch_July
Figure generated: dispatch_October
Figure generated: bess_soc
Figure generated: bess_operation_January
Figure generated: bess_operation_July
Figure generated: demand_supply_balance
Figure generated: redirection_heatmap
Figure generated: redirection_type_matrix
Figure generated: decomposition_convergence
Figure generated: decomposition_cut_generation
Figure generated: lbbd_cut_families
Figure generated: lbbd_candidate_bounds
Figure generated: lbbd_infrastructure_evolution
Figure generated: lbbd_iteration_timing
Figure generated: lbbd_gap_diagnostics
Figure generated: lbbd_adaptive_master_control
Figure generated: lbbd_candidate_reuse
Figure skipped: slack (No positive slack)
Figure generated: spatial_maps
Figures written to: C:\Users\omkarp\Downloads\Opti\runs\2026-08-12_184349_small_with_redirection_LBBD_withPV_withBESS\figures
