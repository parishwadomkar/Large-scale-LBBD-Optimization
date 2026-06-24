from __future__ import annotations

from pathlib import Path
from typing import Any


def configure_project_imports(project_root: Path) -> None:
    import sys

    src_path = str(project_root / "src")
    root_path = str(project_root)
    for p in [src_path, root_path]:
        if p not in sys.path:
            sys.path.insert(0, p)


def load_project_data(project_root: Path, dataset_arg: str | None) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], str]:
    configure_project_imports(project_root)
    from utils import load_json, resolve_project_path

    raw_paths = load_json(project_root / "config" / "paths.json")
    model_cfg = load_json(project_root / "config" / "model_config.json")
    solver_cfg = load_json(project_root / "config" / "solver_gurobi.json")

    dataset = dataset_arg or raw_paths.get("default_dataset", "small")
    if "datasets" not in raw_paths or dataset not in raw_paths["datasets"]:
        available = list(raw_paths.get("datasets", {}).keys())
        raise KeyError(f"Dataset '{dataset}' not found in config/paths.json. Available datasets: {available}")

    paths = dict(raw_paths["datasets"][dataset])
    paths["dataset"] = dataset
    paths["pvgis_excel"] = raw_paths["pvgis_excel"]
    paths["spot_price_csv"] = raw_paths["spot_price_csv"]
    paths["runs_root"] = raw_paths["runs_root"]

    for key in [
        "demand_shapefile",
        "distance_csv",
        "parking_shapefile",
        "pvgis_excel",
        "spot_price_csv",
        "runs_root",
    ]:
        paths[key] = str(resolve_project_path(project_root, paths[key]))

    return paths, model_cfg, solver_cfg, dataset


def load_and_preprocess(project_root: Path, dataset_arg: str | None) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any], str]:
    configure_project_imports(project_root)
    from data_loader import load_inputs
    from preprocessing import preprocess

    paths, model_cfg, solver_cfg, dataset = load_project_data(project_root, dataset_arg)
    raw = load_inputs(paths)
    data = preprocess(raw, model_cfg)
    data["dataset"] = dataset
    return paths, model_cfg, solver_cfg, data, dataset

