"""Checksum-verified loading of frozen Project Montecito point-set inputs."""
from __future__ import annotations

import csv
import hashlib
from pathlib import Path
import numpy as np

POINT_COLUMN_PRIORITY = (
    "x_unfolded",
    "theta_unfolded_relative_x",
    "unfolded_x",
    "unfolded",
    "x",
    "value",
)


def sha256_file(path: str | Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_point_csv(path: str | Path, expected_sha256: str | None = None) -> np.ndarray:
    source = Path(path)
    if expected_sha256 and sha256_file(source) != expected_sha256:
        raise ValueError(f"SHA-256 mismatch for {source}")
    with source.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
    if not rows:
        raise ValueError(f"empty point CSV: {source}")
    columns = set(rows[0])
    key = next((name for name in POINT_COLUMN_PRIORITY if name in columns), None)
    if key is None:
        raise ValueError(f"no recognized unfolded-point column in {source}: {sorted(columns)}")
    points = np.asarray([float(row[key]) for row in rows], dtype=np.float64)
    if not np.all(np.isfinite(points)):
        raise ValueError(f"non-finite unfolded values in {source}")
    if not np.all(np.diff(points) > 0):
        raise ValueError(f"loaded points are not strictly increasing: {source}")
    return points
