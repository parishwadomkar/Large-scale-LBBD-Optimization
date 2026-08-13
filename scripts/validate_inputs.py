#!/usr/bin/env python
from __future__ import annotations

import argparse
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC = PROJECT_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from data_loader import load_inputs  # noqa: E402
from run_optimization import load_configs  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate optimization input files without building a model.")
    parser.add_argument("--dataset", choices=["small", "full"], default="small")
    args = parser.parse_args()

    paths, _, _, dataset = load_configs(PROJECT_ROOT, args.dataset)
    print(f"Validating dataset: {dataset}")
    for key in ["demand_shapefile", "parking_shapefile", "distance_csv", "pvgis_excel", "spot_price_csv"]:
        path = Path(paths[key])
        size = path.stat().st_size if path.exists() else 0
        print(f"{key:<20} {path}  [{'OK' if path.exists() else 'MISSING'}; {size:,} bytes]")

    raw = load_inputs(paths)
    print("\nInput validation PASS")
    print(f"Demand rows:  {len(raw['gdf']):,}")
    print(f"Parking rows: {len(raw['parking_gdf']):,}")
    print(f"Distance rows:{len(raw['dist_df']):,}")
    print(f"Resolved demand file:  {raw['paths']['demand_shapefile']}")
    print(f"Resolved parking file: {raw['paths']['parking_shapefile']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
