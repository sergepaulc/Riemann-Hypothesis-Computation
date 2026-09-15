"""Killip--Nenciu CMV sampler for the circular beta ensemble at beta=2.

The CMV matrix is assembled from sparse 1x1/2x2 blocks and converted to a
single dense Fortran-ordered work array only for the all-eigenvalue solve.  This
avoids the frozen baseline's two dense block-diagonal matrices and dense L@M
product, while leaving the mathematical generator unchanged.
"""
from __future__ import annotations

import numpy as np
from scipy import linalg
from scipy.sparse import block_diag, csr_matrix


def _theta(alpha: complex) -> np.ndarray:
    rho = float(np.sqrt(max(0.0, 1.0 - abs(alpha) ** 2)))
    return np.asarray([[np.conjugate(alpha), rho], [rho, -alpha]], dtype=np.complex128)


def sample_verblunsky_cue(n: int, rng: np.random.Generator) -> np.ndarray:
    if n < 1:
        raise ValueError("n must be positive")
    alpha = np.empty(n, dtype=np.complex128)
    for k in range(n - 1):
        # beta=2: |alpha_k|^2 ~ Beta(1, n-k-1), angle uniform.
        radius_squared = rng.beta(1.0, float(n - k - 1))
        angle = rng.uniform(0.0, 2.0 * np.pi)
        alpha[k] = np.sqrt(radius_squared) * np.exp(1j * angle)
    alpha[n - 1] = np.exp(1j * rng.uniform(0.0, 2.0 * np.pi))
    return alpha


def _cmv_factors_sparse(alpha: np.ndarray) -> tuple[csr_matrix, csr_matrix]:
    a = np.asarray(alpha, dtype=np.complex128)
    n = a.size
    if n < 1:
        raise ValueError("at least one Verblunsky coefficient is required")
    if np.any(np.abs(a[:-1]) >= 1.0 + 1e-14) or not np.isclose(abs(a[-1]), 1.0, atol=1e-12):
        raise ValueError("invalid Verblunsky coefficients")

    l_blocks: list[np.ndarray] = []
    k = 0
    while k + 1 < n:
        l_blocks.append(_theta(a[k]))
        k += 2
    if k < n:
        l_blocks.append(np.asarray([[np.conjugate(a[-1])]], dtype=np.complex128))

    m_blocks: list[np.ndarray] = [np.asarray([[1.0 + 0.0j]], dtype=np.complex128)]
    k = 1
    while k + 1 < n:
        m_blocks.append(_theta(a[k]))
        k += 2
    if k < n:
        m_blocks.append(np.asarray([[np.conjugate(a[-1])]], dtype=np.complex128))

    L = block_diag(l_blocks, format="csr", dtype=np.complex128)
    M = block_diag(m_blocks, format="csr", dtype=np.complex128)
    if L.shape != (n, n) or M.shape != (n, n):
        raise RuntimeError(f"internal CMV factor shape error: L={L.shape}, M={M.shape}, n={n}")
    return L, M


def cmv_matrix(alpha: np.ndarray) -> np.ndarray:
    """Return the dense CMV matrix, assembled through sparse factors."""
    L, M = _cmv_factors_sparse(alpha)
    return np.asarray((L @ M).toarray(order="F"), dtype=np.complex128, order="F")


def cmv_matrix_dense_reference(alpha: np.ndarray) -> np.ndarray:
    """Frozen-baseline dense construction, retained only for small cross-checks."""
    a = np.asarray(alpha, dtype=np.complex128)
    n = a.size
    L = np.eye(n, dtype=np.complex128)
    M = np.eye(n, dtype=np.complex128)
    for k in range(0, n - 1, 2):
        L[k : k + 2, k : k + 2] = _theta(a[k])
    if n % 2 == 1:
        L[-1, -1] = np.conjugate(a[-1])
    for k in range(1, n - 1, 2):
        M[k : k + 2, k : k + 2] = _theta(a[k])
    if n % 2 == 0:
        M[-1, -1] = np.conjugate(a[-1])
    return L @ M


def cue_eigenangles_cmv(n: int, rng: np.random.Generator) -> np.ndarray:
    matrix = cmv_matrix(sample_verblunsky_cue(n, rng))
    eigenvalues = linalg.eigvals(matrix, overwrite_a=True, check_finite=False)
    return np.sort(np.mod(np.angle(eigenvalues), 2.0 * np.pi))


def eigenangles_to_unit_density_points(
    angles: np.ndarray,
    rng: np.random.Generator,
) -> np.ndarray:
    """Apply a seeded rotation, unwrap, and scale a circular point set to density 1."""
    theta = np.asarray(angles, dtype=np.float64)
    if theta.ndim != 1 or theta.size < 2:
        raise ValueError("angles must be one-dimensional")
    rotated = np.mod(theta + rng.uniform(0.0, 2.0 * np.pi), 2.0 * np.pi)
    rotated.sort()
    return rotated * (theta.size / (2.0 * np.pi))


def cue_points_cmv(n: int, rng: np.random.Generator) -> np.ndarray:
    # Keep generator and rotation draws in one deterministic stream, as preregistered.
    return eigenangles_to_unit_density_points(cue_eigenangles_cmv(n, rng), rng)
