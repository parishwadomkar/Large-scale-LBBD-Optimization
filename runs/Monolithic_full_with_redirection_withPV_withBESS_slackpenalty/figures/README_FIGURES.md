# Generated optimization figures

Figures are generated automatically after successful monolithic, Benders, and LBBD result export.
PNG files use the run-level resolution setting (default: 300 dpi). The figure manifest records
which figure groups were generated, skipped, or failed.

## How to read the common result figures

- `01_economic_breakdown.png` separates annual revenue, grid electricity, redirection incentives,
  slack penalty, charger capex, and PV/BESS capex. Positive bars increase profit; negative bars reduce it.
- `02_charger_deployment_and_utilization.png` compares installed slow, medium, and fast chargers
  with the annual utilization of their available capacity.
- `03_monthly_energy_supply_mix.png` shows whether charger energy is supplied directly from the
  grid, directly from PV, or through battery discharge.
- `04_dispatch_<month>.png` gives the representative-day dispatch profile for selected months.
- `05_bess_soc_by_month.png` and `06_bess_operation_<month>.png` describe the linked BESS state of
  charge and charge/discharge operation. They are generated only when BESS output files exist.
- `07_redirection_month_time_heatmap.png` shows when redirected charging is used most strongly.
- `08_redirection_type_matrix.png` shows the origin charger-type to destination charger-type energy
  assignment in the exact exported solution.
- `10_slack_by_month.png` is generated only when positive unmet demand exists. A skipped slack figure
  normally means the optimized solution had zero positive slack.
- `11_map_public_charging_capacity.png` through `15_map_redirection_corridors_<month>.png` are spatial
  maps. CARTO raster tiles require a key in `CARTO_BASEMAP_API_KEY`. With no key, the default
  uses OpenStreetMap tiles if `contextily` supports custom request headers; otherwise vector
  geometry is retained. Source attribution must remain legible on published maps.
- `15_redirection_corridor_distance_audit_<month>.csv` checks every exported corridor in the
  selected month against hex-centroid great-circle distance. Red dashed arrows require spatial
  review; a mismatch does not establish which input is wrong. Web Mercator span is not ground
  distance. Check the model's shortest-path distance table and shapefile ID/CRS before publication.
- `16_demand_supply_balance_annual_average.png` compares home and public charging supply accounting.
- `25_monolithic_runtime_and_memory.png` shows recorded end-to-end monolithic run phases and
  process-tree RSS where available. Generate it again after the run has written its complexity
  metadata; it cannot use LBBD iteration timing for a monolithic solve.
- `26_process_memory_profile.png` shows measured process-tree RSS over time, including
  iteration-end markers and per-interval statistics where LBBD history exists. The monitor's
  faster peak is distinguished from the saved five-second trace peak. It reports solver memory
  settings and the solver calls that logged node-file-directory creation; node-file disk bytes
  were not monitored. The CSV's `process_tree_rss_MB` is bytes divided by 1024 squared, and is
  converted to GiB by dividing by another 1024. `26_memory_interval_summary.csv` contains
  the numerical interval values.
  Regenerate figures after `resource_usage.csv` and run complexity metadata have been exported.

## How to read decomposition figures

- `09_decomposition_convergence.png` is the main certificate plot. The upper-bound line is the valid
  global master bound. The lower-bound line is the best exact feasible incumbent. The dashed gap line
  is `(UB - LB) / max(1, |UB|)` in percent.

- `17_decomposition_cut_generation.png` separates accepted pre-loop cuts (root and LP-bootstrap Hall cuts, plus any static origin cuts) from cuts added in each outer iteration. The cumulative line includes both phases.
  `lbbd_cut_accounting.csv` lists the accepted counts by phase, iteration and family. Hall cuts preserve penalized unmet-demand slack.

- `18_lbbd_cut_families.png` includes all recorded LBBD cut families, including bootstrap Hall cuts, and displays zero-count families explicitly. Accepted inference cuts are distinct from Gurobi's internal cutting planes.

- `19_lbbd_candidate_bounds.png` shows the reported exact-certified iteration outcome, its fixed-infrastructure upper bound, the best certified incumbent, and fixed-infrastructure certification gap. A repair can cause more than one exact MIP call within an iteration; the history stores the final reported outcome. `lbbd_exact_evaluations.csv` separately lists every exact solver call extracted from the archived solver-log statistics, including raw slack-penalized trial objectives and repair objectives where available.

- `20_lbbd_infrastructure_evolution.png` shows the actual charger, photovoltaic-panel, and battery-unit counts of the best certified
  infrastructure across LBBD iterations.

- `21_lbbd_iteration_timing.png` shows pre-loop preparation and LP bootstrap, each outer iteration, and final export/figures as distinct phases. Its cumulative curve covers the complete end-to-end run. The LP-bootstrap solve is attributed to pre-loop rather than counted again as an iteration-1 master MIP.

- `22_lbbd_gap_diagnostics.png` compares the global LBBD gap, achieved master MIP gap where an incumbent and bound came from the same master solve, and exact fixed-layout gaps for newly certified outcomes. Cached or bound-only iterations do not create new fixed-layout gap points.

- `23_lbbd_adaptive_master_control.png` compares requested master MIP tolerance and genuine achieved master MIP gaps with the certified outer gap. The LP bootstrap has no requested MIP solve, while fallback and bound-only iterations have no achieved master MIP gap without a master incumbent.
  
- `24_lbbd_candidate_reuse.png` distinguishes a new exact-certified outcome, a cache hit, and a bound-only termination without a new exact solve. Its cut line counts outer-iteration additions only; the bootstrap cuts appear in figures 17 and 18.

## Regenerating figures

```powershell
python src\visualize_results.py --run-dir "runs\<RUN_FOLDER>" --dataset full --dpi 300 --redirection-map-month June
```
