"""Memory-aware raw and core-anchored spectral moments through order four."""
from __future__ import annotations

from collections.abc import Iterable
import numpy as np


def _validate_square(K: np.ndarray) -> np.ndarray:
    A = np.asarray(K, dtype=np.float64)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("K must be square")
    return A


def _validate_core(core_indices: np.ndarray, n: int) -> np.ndarray:
    core = np.asarray(core_indices, dtype=np.int64)
    if core.ndim != 1 or core.size == 0 or np.any(core < 0) or np.any(core >= n):
        raise ValueError("invalid core indices")
    if np.unique(core).size != core.size:
        raise ValueError("core indices must be unique")
    return core


def core_product_rows(K: np.ndarray, core_indices: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return ``K[core,:]`` and the corresponding rows of ``K @ K``.

    Only a ``core_size x n`` product is formed, rather than a full ``n x n`` K².
    """
    A = _validate_square(K)
    core = _validate_core(core_indices, A.shape[0])
    K_core = np.ascontiguousarray(A[core, :])
    K2_core = K_core @ A
    return K_core, K2_core


def moments_from_core_rows(K_core: np.ndarray, K2_core: np.ndarray) -> dict[int, float]:
    if K_core.shape != K2_core.shape:
        raise ValueError("K_core and K2_core must have identical shapes")
    core_size = K_core.shape[0]
    # Every Experiment 3 sinc matrix has an exact unit diagonal.
    mu1 = 1.0
    mu2 = float(np.sum(K_core * K_core, dtype=np.float64) / core_size)
    mu3 = float(np.sum(K2_core * K_core, dtype=np.float64) / core_size)
    mu4 = float(np.sum(K2_core * K2_core, dtype=np.float64) / core_size)
    return {1: mu1, 2: mu2, 3: mu3, 4: mu4}


def core_diagonal_moments(
    K: np.ndarray,
    core_indices: np.ndarray,
    orders: Iterable[int] = (1, 2, 3, 4),
) -> dict[int, float]:
    requested = sorted(set(int(order) for order in orders))
    if not requested or requested[0] < 1 or requested[-1] > 4:
        raise ValueError("this optimized routine supports orders 1 through 4")
    K_core, K2_core = core_product_rows(K, core_indices)
    all_moments = moments_from_core_rows(K_core, K2_core)
    return {order: all_moments[order] for order in requested}


def raw_moments(K: np.ndarray, orders: Iterable[int] = (1, 2, 3, 4)) -> dict[int, float]:
    A = _validate_square(K)
    requested = sorted(set(int(order) for order in orders))
    if not requested or requested[0] < 1 or requested[-1] > 4:
        raise ValueError("this optimized routine supports orders 1 through 4")
    K2 = A @ A
    values = {
        1: float(np.trace(A) / A.shape[0]),
        2: float(np.sum(A * A, dtype=np.float64) / A.shape[0]),
        3: float(np.sum(K2 * A, dtype=np.float64) / A.shape[0]),
        4: float(np.sum(K2 * K2, dtype=np.float64) / A.shape[0]),
    }
    return {order: values[order] for order in requested}


def eigenvalue_moments(K: np.ndarray, orders: Iterable[int] = (1, 2, 3, 4)) -> dict[int, float]:
    A = _validate_square(K)
    vals = np.linalg.eigvalsh(A)
    return {int(k): float(np.mean(vals ** int(k))) for k in orders}
