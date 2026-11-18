from __future__ import annotations

import csv
from pathlib import Path
import sys

import numpy as np

CODE = Path(__file__).resolve().parents[1]
BASE = CODE.parent
sys.path.insert(0, str(CODE))

from aggregate_results_v1_1 import generate_summary_tables
from runtime_src.collision_decomposition import anchored_collision_terms
from runtime_src.cue_cmv import cue_points_cmv
from runtime_src.poisson_control import poisson_circular_points
from runtime_src.sinc_kernel import build_sinc_kernel, sinc_pi
from runtime_src.spectral_moments import core_diagonal_moments, eigenvalue_moments, raw_moments
from validate_collision_decomposition_v1_1 import brute_force_terms


def test_sinc_convention_and_symmetry() -> None:
    u = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
    expected = np.array([0.0, 2.0 / np.pi, 1.0, 2.0 / np.pi, 0.0])
    assert np.allclose(sinc_pi(u), expected, atol=1e-15, rtol=0)
    K = build_sinc_kernel(np.array([0.0, 0.4, 1.3, 2.2]))
    assert np.allclose(K, K.T, atol=1e-15, rtol=0)
    assert np.array_equal(np.diag(K), np.ones(4))


def test_integer_lattice_is_identity() -> None:
    K = build_sinc_kernel(np.arange(32, dtype=np.float64))
    assert np.allclose(K, np.eye(32), atol=2e-15, rtol=0)
    moments = raw_moments(K)
    assert moments == {1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0}


def test_homometric_fourth_moment_separation() -> None:
    A = 0.5 * np.array([0, 1, 2, 6, 8, 11], dtype=np.float64)
    B = 0.5 * np.array([0, 1, 6, 7, 9, 11], dtype=np.float64)
    distances = lambda x: sorted(x[j] - x[i] for i in range(len(x)) for j in range(i + 1, len(x)))
    assert distances(A) == distances(B)
    ma = raw_moments(build_sinc_kernel(A))
    mb = raw_moments(build_sinc_kernel(B))
    for order in (1, 2, 3):
        assert abs(ma[order] - mb[order]) <= 2e-15
    assert abs((ma[4] - mb[4]) - 0.09830970477875489) <= 2e-15


def test_collision_terms_against_direct_enumeration() -> None:
    for n in (5, 6, 7):
        rng = np.random.default_rng(700 + n)
        points = np.cumsum(rng.uniform(0.25, 1.55, size=n))
        K = build_sinc_kernel(points)
        for core in (np.arange(n), np.arange(0, n, 2), np.arange(1, n - 1)):
            optimized = anchored_collision_terms(K, core).to_dict()
            brute = brute_force_terms(K, core)
            for key in ("s2", "s4", "t3", "w30", "w31", "q4", "direct_numerator"):
                assert abs(float(optimized[key]) - float(brute[key])) <= 2e-12
            assert abs(float(optimized["pair_part"]) - brute["two_distinct_direct"]) <= 2e-12
            assert abs(float(optimized["three_index_part"]) - brute["three_distinct_direct"]) <= 2e-12
            assert abs(float(optimized["q4"]) - brute["four_distinct_direct"]) <= 2e-12

    # The identity is algebraic, not specific to sinc or positive-semidefinite matrices.
    rng = np.random.default_rng(4422)
    raw = rng.uniform(-0.7, 0.7, size=(6, 6))
    generic = 0.5 * (raw + raw.T)
    np.fill_diagonal(generic, 1.0)
    core = np.array([0, 2, 5])
    optimized = anchored_collision_terms(generic, core).to_dict()
    brute = brute_force_terms(generic, core)
    for key in ("s2", "s4", "t3", "w30", "w31", "q4", "direct_numerator"):
        assert abs(float(optimized[key]) - float(brute[key])) <= 2e-12


def test_moment_implementations_agree() -> None:
    rng = np.random.default_rng(8181)
    points = np.cumsum(rng.uniform(0.4, 1.4, size=12))
    K = build_sinc_kernel(points)
    direct = raw_moments(K)
    eigen = eigenvalue_moments(K)
    core = core_diagonal_moments(K, np.arange(K.shape[0]))
    for order in (1, 2, 3, 4):
        assert abs(direct[order] - eigen[order]) <= 2e-12
        assert abs(direct[order] - core[order]) <= 2e-12


def test_cue_generator_is_deterministic_and_unit_density() -> None:
    first = cue_points_cmv(64, np.random.default_rng(123456))
    second = cue_points_cmv(64, np.random.default_rng(123456))
    assert np.array_equal(first, second)
    assert np.all(np.diff(first) > 0)
    assert abs(float(np.mean(np.diff(first))) - 1.0) < 0.15


def test_poisson_generator_is_deterministic_and_ordered() -> None:
    first = poisson_circular_points(128, np.random.default_rng(7890))
    second = poisson_circular_points(128, np.random.default_rng(7890))
    assert np.array_equal(first, second)
    assert np.all(np.diff(first) > 0)
    assert 0.75 < float(np.mean(np.diff(first))) < 1.25


def test_derived_tables_regenerate_from_endpoint_rows(tmp_path: Path) -> None:
    target = tmp_path / "results"
    target.mkdir()
    source = BASE / "02_results" / "all_window_endpoints.csv"
    (target / source.name).write_bytes(source.read_bytes())
    validation = generate_summary_tables(target)
    assert validation["status"] == "PASS"
    assert validation["endpoint_rows"] == 176
    assert (target / "group_summary.csv").exists()
    assert (target / "mu4_difference_decomposition_vs_cue.csv").exists()
    with (target / "group_summary.csv").open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    assert [row["group"] for row in rows] == [
        "D0_first_10000",
        "D1_near_1e12",
        "D2_near_1e21",
        "CUE",
        "Poisson",
    ]
