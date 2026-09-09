LBBD optimization
=================
Project root: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization
Dataset: small
Run profile: lbbd.small
Scenario: with_redirection
Technology: withPV_withBESS
Method: embedded continuous recourse relaxation with LP cuts and exact annual MIP certification
Run directory: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-08_061951_small_with_redirection_LBBD_withPV_withBESS
Master solver memory mode: threads=16, root_method=auto, node_method=auto, nodefile_start=0.5 GB, soft_mem_limit=none GB
Hex cells: 57
Active redirection arc-slots: 57,600
Slot components: 11,640
Global redirection components: 12
Static origin-neighbourhood profit cuts: 0
Initial master size: 466,011 variables; 452,492 constraints
Adaptive master-gap control: initial 0.001000% -> tight 0.001000%
Internal master MIP start: slack-only feasible point loaded (Eta -539,435,277,458.976; setup 0.6s).
Iteration 01 | UB 126,993,465.291 | LB 126,991,733.460 | gap 0.001364% | candidate 126,991,733.460 | fixed gap 0.000028% | master maxtimelimit MIP gap 0.0013% (requested 0.0010%) | cuts +0 Hall +0 comp-LP +0 annual-LP +1 config-MIP +0 partial-MIP | slow 71 medium 402 fast 41 PV 15080 BESS 319
Iteration 02 | UB 126,993,152.897 | LB 126,991,930.890 | gap 0.000962% | candidate 126,991,930.890 | fixed gap 0.000008% | master optimal MIP gap 0.0010% (requested 0.0010%) | cuts +0 Hall +0 comp-LP +0 annual-LP +0 config-MIP +0 partial-MIP | slow 72 medium 402 fast 41 PV 15089 BESS 320

Best certified incumbent
------------------------
Objective: 126,991,930.890 SEK/year
Best fixed-investment upper bound: 126,991,941.278 SEK/year
Global master upper bound: 126,993,152.897 SEK/year
Certified gap: 0.000962%
Termination: certified_gap
Output: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-08_061951_small_with_redirection_LBBD_withPV_withBESS
Combined XLSX written to: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-08_061951_small_with_redirection_LBBD_withPV_withBESS\results\combined_results.xlsx
Output files written to: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-08_061951_small_with_redirection_LBBD_withPV_withBESS\results
Certified resume checkpoint written to: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-08_061951_small_with_redirection_LBBD_withPV_withBESS\results\lbbd_certified_resume.json
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
Figures written to: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-08_061951_small_with_redirection_LBBD_withPV_withBESS\figures
