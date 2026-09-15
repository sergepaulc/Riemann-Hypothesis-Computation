"""Normalized sinc-pi kernel construction with bounded temporary memory."""
from __future__ import annotations

import numpy as np


def validate_points(points: np.ndarray) -> np.ndarray:
    x = np.asarray(points, dtype=np.float64)
    if x.ndim != 1 or x.size < 2:
        raise ValueError("points must be a one-dimensional array with at least two entries")
    if not np.all(np.isfinite(x)):
        raise ValueError("points contain non-finite values")
    if not np.all(np.diff(x) > 0):
        raise ValueError("points must be strictly increasing")
    return x


def sinc_pi(u: np.ndarray | float) -> np.ndarray:
    """Return sin(pi*u)/(pi*u), with the continuous value 1 at u=0."""
    return np.sinc(np.asarray(u, dtype=np.float64))


def build_sinc_cross(
    left_points: np.ndarray,
    right_points: np.ndarray,
    *,
    row_block: int = 256,
) -> np.ndarray:
    left = np.asarray(left_points, dtype=np.float64)
    right = np.asarray(right_points, dtype=np.float64)
    if left.ndim != 1 or right.ndim != 1:
        raise ValueError("point arrays must be one-dimensional")
    if row_block < 1:
        raise ValueError("row_block must be positive")
    out = np.empty((left.size, right.size), dtype=np.float64)
    for start in range(0, left.size, row_block):
        stop = min(start + row_block, left.size)
        delta = left[start:stop, None] - right[None, :]
        out[start:stop] = np.sinc(delta)
    return out


def build_sinc_kernel(
    points: np.ndarray,
    *,
    check: bool = True,
    row_block: int = 256,
) -> np.ndarray:
    """Construct a real symmetric sinc matrix without a full-size delta array."""
    x = validate_points(points) if check else np.asarray(points, dtype=np.float64)
    K = build_sinc_cross(x, x, row_block=row_block)
    np.fill_diagonal(K, 1.0)
    # Average with the transpose once to remove tiny asymmetric rounding effects.
    K += K.T
    K *= 0.5
    np.fill_diagonal(K, 1.0)
    return K
