from __future__ import annotations

from pathlib import Path
from typing import Iterable

import geopandas as gpd
import pandas as pd

_GPKG_SIGNATURE = b"SQLite format 3\x00"
_LFS_PREFIX = b"version https://git-lfs.github.com/spec/v1"


def _read_head(path: Path, size: int = 256) -> bytes:
    try:
        with path.open("rb") as fh:
            return fh.read(size)
    except OSError:
        return b""


def _describe_invalid_vector_file(path: Path) -> str:
    head = _read_head(path, 512)
    lower = head.lstrip().lower()
    if head.startswith(_LFS_PREFIX):
        return (
            "The file is a Git LFS pointer, not the actual spatial dataset. "
            "Run 'git lfs install' and 'git lfs pull', or restore the real data file."
        )
    if lower.startswith(b"<!doctype html") or lower.startswith(b"<html"):
        return (
            "The file contains HTML rather than spatial data. It was probably downloaded "
            "from a web/GitHub page instead of as the raw binary file."
        )
    if head.startswith(b"PK\x03\x04"):
        return "The file is a ZIP archive despite its current extension. Extract/restore the real spatial file."
    if len(head) == 0:
        return "The file is empty or unreadable."
    return "The file exists, but its binary signature does not match the configured spatial format."


def _is_valid_gpkg_container(path: Path) -> bool:
    return path.is_file() and _read_head(path, len(_GPKG_SIGNATURE)) == _GPKG_SIGNATURE


def _candidate_gpkg_files(configured: Path, role: str) -> list[Path]:
    parent = configured.parent
    if not parent.exists():
        return []

    role_tokens = {
        "demand": ("demand", "hexgrid"),
        "parking": ("charpark", "parking"),
    }.get(role, ())

    candidates: list[Path] = []
    for candidate in sorted(parent.glob("*.gpkg")):
        if candidate.resolve() == configured.resolve():
            continue
        name = candidate.name.lower()
        if role_tokens and not any(token in name for token in role_tokens):
            continue
        if _is_valid_gpkg_container(candidate):
            candidates.append(candidate)
    return candidates


def _resolve_vector_path(path: Path, role: str) -> Path:
    if not path.exists():
        raise FileNotFoundError(f"Configured {role} spatial input does not exist: {path}")

    if path.suffix.lower() == ".gpkg" and not _is_valid_gpkg_container(path):
        candidates = _candidate_gpkg_files(path, role)
        if len(candidates) == 1:
            replacement = candidates[0]
            print(
                f"WARNING: Configured {role} GeoPackage is invalid: {path}\n"
                f"         Using the only matching valid GeoPackage in the same folder: {replacement}"
            )
            return replacement

        detail = _describe_invalid_vector_file(path)
        candidate_text = ""
        if candidates:
            candidate_text = "\nMatching valid GeoPackages found:\n  - " + "\n  - ".join(str(p) for p in candidates)
        raise RuntimeError(
            f"Invalid configured {role} GeoPackage: {path}\n"
            f"{detail}\n"
            "A GeoPackage is an SQLite container and should begin with the binary signature "
            "'SQLite format 3'. Explicitly forcing the GPKG driver will not repair a non-GeoPackage file."
            f"{candidate_text}\n"
            "Update config/paths.json to the correct file if needed."
        )

    return path


def _read_vector(path: Path, role: str) -> tuple[gpd.GeoDataFrame, Path]:
    resolved = _resolve_vector_path(path, role)

    # Pyogrio is GeoPandas' current high-performance engine. Fiona is retained
    # as a compatibility fallback for a genuine vector dataset that Pyogrio
    # cannot open in the local GDAL environment.
    errors: list[str] = []
    for engine in ("pyogrio", "fiona"):
        try:
            return gpd.read_file(resolved, engine=engine), resolved
        except Exception as exc:
            errors.append(f"{engine}: {type(exc).__name__}: {exc}")

    raise RuntimeError(
        f"Could not read {role} spatial input: {resolved}\n"
        + "\n".join(f"  {msg}" for msg in errors)
    )


def _require_files(paths: Iterable[tuple[str, Path]]) -> None:
    missing = [(name, path) for name, path in paths if not path.exists()]
    if missing:
        listing = "\n".join(f"  - {name}: {path}" for name, path in missing)
        raise FileNotFoundError(f"Required optimization input files are missing:\n{listing}")


def load_inputs(paths: dict) -> dict:
    demand_shapefile = Path(paths["demand_shapefile"])
    parking_shapefile = Path(paths["parking_shapefile"])
    distance_csv = Path(paths["distance_csv"])
    spot_price_csv = Path(paths["spot_price_csv"])
    pvgis_excel = Path(paths["pvgis_excel"])

    _require_files(
        [
            ("demand_shapefile", demand_shapefile),
            ("parking_shapefile", parking_shapefile),
            ("distance_csv", distance_csv),
            ("spot_price_csv", spot_price_csv),
            ("pvgis_excel", pvgis_excel),
        ]
    )

    gdf, demand_resolved = _read_vector(demand_shapefile, "demand")
    parking_gdf, parking_resolved = _read_vector(parking_shapefile, "parking")

    resolved_paths = dict(paths)
    resolved_paths["demand_shapefile"] = str(demand_resolved)
    resolved_paths["parking_shapefile"] = str(parking_resolved)

    return {
        "gdf": gdf,
        "parking_gdf": parking_gdf,
        "dist_df": pd.read_csv(distance_csv),
        "spot_df": pd.read_csv(spot_price_csv),
        "pvgis_df": pd.read_excel(pvgis_excel),
        "paths": resolved_paths,
    }


def check_input_paths(paths: dict) -> list[tuple[str, bool]]:
    keys = ["demand_shapefile", "distance_csv", "parking_shapefile", "pvgis_excel", "spot_price_csv"]
    return [(str(Path(paths[k])), Path(paths[k]).exists()) for k in keys]
