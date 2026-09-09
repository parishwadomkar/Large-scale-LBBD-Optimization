# Generated optimization figures

Figures are generated automatically after successful monolithic and LBBD result export.
PNG files use the run-level resolution setting (default: 300 dpi).

Spatial maps are projected to EPSG:3857 and use a faint CartoDB Positron basemap when
`contextily` and internet access are available. If tile retrieval is unavailable, the maps
are still generated from the model hex-grid geometry.

The demand/supply figure uses `results/supply_by_demand_class.csv`. Private-home service
is exact. Because grid, direct PV, and BESS discharge are pooled in the optimization energy
balance, their split between residual-home and public service is an ex-post proportional
accounting allocation within each cell-month-slot; it does not add constraints or alter the
optimized solution.

`09_lbbd_convergence.png` labels the certified gap at every iteration, while
`17_lbbd_cut_generation.png` reports violated cut candidates, cuts added, and the
cumulative master cut pool.

`figures_manifest.csv` records generated, skipped, and failed figure groups.

To regenerate figures for an existing run:

```powershell
python src\visualize_results.py --run-dir "runs\<RUN_FOLDER>" --dataset small --dpi 300 --redirection-map-month June
```
