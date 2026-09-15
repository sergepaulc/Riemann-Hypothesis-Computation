"""Fixed-count circular Poisson/binomial controls at unit density."""
from __future__ import annotations

import numpy as np


def poisson_circular_points(n: int, rng: np.random.Generator) -> np.ndarray:
    """Sample n independent circular points on circumference n and unwrap them.

    A seeded circular rotation is applied before sorting, matching the frozen
    control description.  The resulting ordered coordinates have local unit
    density without result-dependent renormalization.
    """
    if n < 2:
        raise ValueError("n must be at least 2")
    circumference = float(n)
    points = rng.uniform(0.0, circumference, size=n)
    points = np.mod(points + rng.uniform(0.0, circumference), circumference)
    points.sort()
    return points


def poisson_points(n: int, rng: np.random.Generator, *, exact_mean_spacing: bool = False) -> np.ndarray:
    """Compatibility entry point.

    ``exact_mean_spacing=False`` is the preregistered fixed-count circular model.
    The legacy conditioned-exponential option is retained only for unit tests and
    must not be used by production gate runners.
    """
    if not exact_mean_spacing:
        return poisson_circular_points(n, rng)
    gaps = rng.exponential(scale=1.0, size=n - 1)
    gaps *= (n - 1) / np.sum(gaps)
    return np.concatenate(([0.0], np.cumsum(gaps)))
