from __future__ import annotations

from pathlib import Path
import pandas as pd
import geopandas as gpd


def load_inputs(paths: dict) -> dict:
    demand_shapefile = Path(paths["demand_shapefile"])
    parking_shapefile = Path(paths["parking_shapefile"])
    distance_csv = Path(paths["distance_csv"])
    spot_price_csv = Path(paths["spot_price_csv"])
    pvgis_excel = Path(paths["pvgis_excel"])

    return {
        "gdf": gpd.read_file(demand_shapefile),
        "parking_gdf": gpd.read_file(parking_shapefile),
        "dist_df": pd.read_csv(distance_csv),
        "spot_df": pd.read_csv(spot_price_csv),
        "pvgis_df": pd.read_excel(pvgis_excel),
        "paths": paths,
    }


def check_input_paths(paths: dict) -> list[tuple[str, bool]]:
    keys = ["demand_shapefile", "distance_csv", "parking_shapefile", "pvgis_excel", "spot_price_csv"]
    return [(str(Path(paths[k])), Path(paths[k]).exists()) for k in keys]
