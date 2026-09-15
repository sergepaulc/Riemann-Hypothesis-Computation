"""Fourth-moment collision decomposition with core-row memory scaling.

The production all-distinct term ``Q4`` is computed as the residual after the
one-, two-, and three-distinct-index terms are evaluated.  Consequently, adding
those terms back is only an algebraic closure identity, not an independent
validation.  Independent brute-force validation for small matrices is shipped
under ``01_code/tests`` and recorded in the release report.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np

from .spectral_moments import core_product_rows


@dataclass(frozen=True)
class AnchoredCollisionTerms:
    core_size: int
    s2: float
    s4: float
    t3: float
    w30: float
    w31: float
    q4: float
    direct_numerator: float

    @property
    def pair_part(self) -> float:
        return 6.0 * self.s2 + self.s4

    @property
    def three_index_part(self) -> float:
        return 4.0 * self.t3 + self.w30 + self.w31

    @property
    def higher_distinct_part(self) -> float:
        return self.three_index_part + self.q4

    @property
    def reconstructed_numerator(self) -> float:
        return float(self.core_size) + self.pair_part + self.higher_distinct_part

    @property
    def algebraic_closure_residual_by_construction(self) -> float:
        """Residual of the defining identity; not an independent check."""
        return self.direct_numerator - self.reconstructed_numerator

    @property
    def mu4_raw(self) -> float:
        return self.direct_numerator / self.core_size

    @property
    def mu4_gt2(self) -> float:
        return self.higher_distinct_part / self.core_size

    @property
    def q4_per_core(self) -> float:
        return self.q4 / self.core_size

    def to_dict(self) -> dict:
        data = asdict(self)
        data.update(
            {
                "pair_part": self.pair_part,
                "three_index_part": self.three_index_part,
                "higher_distinct_part": self.higher_distinct_part,
                "reconstructed_numerator": self.reconstructed_numerator,
                "algebraic_closure_residual_by_construction": self.algebraic_closure_residual_by_construction,
                "mu4_raw": self.mu4_raw,
                "mu4_gt2": self.mu4_gt2,
                "q4_per_core": self.q4_per_core,
                "q4_computation_note": (
                    "Q4 is the residual after independently computing the one-, two-, "
                    "and three-distinct-index classes. Validate Q4 with the shipped "
                    "brute-force small-matrix tests, not with this closure residual."
                ),
            }
        )
        return data


def _validate(K: np.ndarray, core_indices: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    A = np.asarray(K, dtype=np.float64)
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("K must be square")
    if not np.allclose(A, A.T, atol=1e-12, rtol=0):
        raise ValueError("K must be symmetric")
    if not np.allclose(np.diag(A), 1.0, atol=1e-12, rtol=0):
        raise ValueError("K must have unit diagonal")
    core = np.asarray(core_indices, dtype=np.int64)
    if core.ndim != 1 or core.size == 0 or np.any(core < 0) or np.any(core >= A.shape[0]):
        raise ValueError("invalid core indices")
    if np.unique(core).size != core.size:
        raise ValueError("core indices must be unique")
    return A, core


def anchored_collision_terms(
    K: np.ndarray,
    core_indices: np.ndarray,
    *,
    precomputed_rows: tuple[np.ndarray, np.ndarray] | None = None,
) -> AnchoredCollisionTerms:
    """Compute the anchored decomposition with bounded temporary memory.

    For a core of size ``c`` inside an ``n``-point halo, the dominant product is
    ``K[core,:] @ K`` and therefore stores only ``c x n`` rows of K².  The all-
    distinct Q4 contribution is recovered as the residual after computing the
    one-, two-, and three-distinct-index classes.  That production shortcut is
    independently tested by explicit enumeration on small matrices.
    """
    A, core = _validate(K, core_indices)
    K_core, K2_core = precomputed_rows or core_product_rows(A, core)
    if K_core.shape != (core.size, A.shape[0]) or K2_core.shape != K_core.shape:
        raise ValueError("precomputed core rows have incompatible shapes")

    squared_core = K_core * K_core
    s2_by_core = np.sum(squared_core, axis=1, dtype=np.float64) - 1.0
    s4_by_core = np.sum(squared_core * squared_core, axis=1, dtype=np.float64) - 1.0

    # (K^3)_ii = 1 + 3*S2_i + T3_i.
    k3_diag_core = np.sum(K2_core * K_core, axis=1, dtype=np.float64)
    t3_by_core = k3_diag_core - 1.0 - 3.0 * s2_by_core

    # Two variants of the three-distinct repeated-index contribution.
    w30_by_core = s2_by_core * s2_by_core - s4_by_core
    row_s2_all = np.sum(A * A, axis=1, dtype=np.float64) - 1.0
    w31_by_core = squared_core @ row_s2_all - s2_by_core - s4_by_core

    direct_by_core = np.sum(K2_core * K2_core, axis=1, dtype=np.float64)

    s2 = float(np.sum(s2_by_core, dtype=np.float64))
    s4 = float(np.sum(s4_by_core, dtype=np.float64))
    t3 = float(np.sum(t3_by_core, dtype=np.float64))
    w30 = float(np.sum(w30_by_core, dtype=np.float64))
    w31 = float(np.sum(w31_by_core, dtype=np.float64))
    direct = float(np.sum(direct_by_core, dtype=np.float64))
    q4 = direct - float(core.size) - 6.0 * s2 - s4 - 4.0 * t3 - w30 - w31

    return AnchoredCollisionTerms(int(core.size), s2, s4, t3, w30, w31, q4, direct)
