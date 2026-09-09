LBBD optimization
=================
Project root: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization
Dataset: small
Run profile: lbbd.small
Scenario: with_redirection
Technology: withPV_withBESS
Method: embedded continuous recourse relaxation with LP cuts and exact annual MIP certification
Run directory: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-07_173810_small_with_redirection_LBBD_withPV_withBESS
Master solver memory mode: threads=16, root_method=auto, node_method=auto, nodefile_start=0.5 GB, soft_mem_limit=none GB
Hex cells: 57
Active redirection arc-slots: 57,600
Slot components: 11,640
Global redirection components: 12
Static origin-neighbourhood profit cuts: 0
Initial master size: 466,011 variables; 452,492 constraints
Adaptive master-gap control: initial 0.010000% -> tight 0.002000%
Internal master MIP start: slack-only feasible point loaded (Eta -539,435,277,458.976; setup 0.7s).
Iteration 01 | UB 127,001,258.784 | LB 126,989,765.270 | gap 0.009050% | candidate 126,989,765.270 | fixed gap 0.000006% | master optimal MIP gap 0.0090% (requested 0.0100%) | cuts +0 Hall +0 comp-LP +0 annual-LP +1 config-MIP +0 partial-MIP | slow 68 medium 404 fast 41 PV 15088 BESS 322
Iteration 02 | UB 126,994,013.482 | LB 126,990,418.176 | gap 0.002831% | candidate 126,990,418.176 | fixed gap 0.001017% | master optimal MIP gap 0.0018% (requested 0.0025%) | cuts +0 Hall +0 comp-LP +0 annual-LP +1 config-MIP +0 partial-MIP | slow 72 medium 402 fast 41 PV 15072 BESS 321
Iteration 03 | UB 126,993,520.357 | LB 126,990,418.176 | gap 0.002443% | candidate 126,990,418.176 cached | fixed gap 0.001017% | master optimal MIP gap 0.0014% (requested 0.0020%) | cuts +0 Hall +0 comp-LP +0 annual-LP +0 config-MIP +0 partial-MIP | slow 72 medium 402 fast 41 PV 15072 BESS 321
Iteration 04 | UB 126,993,520.357 | LB 126,990,631.159 | gap 0.002275% | candidate 126,990,631.159 | fixed gap 0.000888% | master optimal MIP gap 0.0017% (requested 0.0020%) | cuts +0 Hall +0 comp-LP +0 annual-LP +0 config-MIP +0 partial-MIP | slow 72 medium 402 fast 41 PV 15072 BESS 320
Iteration 05 | UB 126,993,520.357 | LB 126,990,631.159 | gap 0.002275% | candidate 126,990,631.159 cached | fixed gap 0.000888% | master optimal MIP gap 0.0017% (requested 0.0020%) | cuts +0 Hall +0 comp-LP +0 annual-LP +0 config-MIP +0 partial-MIP | slow 72 medium 402 fast 41 PV 15072 BESS 320
Iteration 06 | UB 126,993,394.607 | LB 126,990,631.159 | gap 0.002176% | candidate 126,990,631.159 cached | fixed gap 0.000888% | master optimal MIP gap 0.0013% (requested 0.0020%) | cuts +0 Hall +0 comp-LP +0 annual-LP +0 config-MIP +0 partial-MIP | slow 72 medium 402 fast 41 PV 15072 BESS 320
Iteration 07 | UB 126,993,394.607 | LB 126,990,631.159 | gap 0.002176% | candidate 126,990,631.159 cached | fixed gap 0.000888% | master optimal MIP gap 0.0013% (requested 0.0020%) | cuts +0 Hall +0 comp-LP +0 annual-LP +0 config-MIP +0 partial-MIP | slow 72 medium 402 fast 41 PV 15072 BESS 320
Iteration 08 | UB 126,993,394.607 | LB 126,990,631.159 | gap 0.002176% | candidate 126,990,631.159 cached | fixed gap 0.000888% | master optimal MIP gap 0.0013% (requested 0.0020%) | cuts +0 Hall +0 comp-LP +0 annual-LP +0 config-MIP +0 partial-MIP | slow 72 medium 402 fast 41 PV 15072 BESS 320
Stopping after repeated identical candidates with no separating cuts at the tight master gap 0.002000%.

Best certified incumbent
------------------------
Objective: 126,990,631.159 SEK/year
Best fixed-investment upper bound: 126,991,759.104 SEK/year
Global master upper bound: 126,993,394.607 SEK/year
Certified gap: 0.002176%
Termination: stagnation_no_new_cuts_at_tight_master_gap
Output: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-07_173810_small_with_redirection_LBBD_withPV_withBESS
Combined XLSX written to: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-07_173810_small_with_redirection_LBBD_withPV_withBESS\results\combined_results.xlsx
Output files written to: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-07_173810_small_with_redirection_LBBD_withPV_withBESS\results
Certified resume checkpoint written to: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-07_173810_small_with_redirection_LBBD_withPV_withBESS\results\lbbd_certified_resume.json
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
Figures written to: C:\Users\omkarp\IdeaProjects\VSCode\Large-scale-LBBD-Optimization\runs\2026-09-07_173810_small_with_redirection_LBBD_withPV_withBESS\figures
