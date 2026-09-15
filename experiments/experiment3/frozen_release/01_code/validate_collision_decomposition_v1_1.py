#!/usr/bin/env python3
"""Independent brute-force validation of the Experiment 3BS collision decomposition.

This script deliberately does not recover Q4 as a residual.  It enumerates every
ordered index tuple for small matrices and computes each collision class directly.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from runtime_src.collision_decomposition import anchored_collision_terms
from runtime_src.sinc_kernel import build_sinc_kernel


def brute_force_terms(K: np.ndarray, core: np.ndarray) -> dict[str, float]:
    n = K.shape[0]
    cset = [int(i) for i in core]
    direct = 0.0
    one = 0.0
    two = 0.0
    three = 0.0
    four = 0.0
    q4 = 0.0

    for i in cset:
        for j in range(n):
            for k in range(n):
                for ell in range(n):
                    value = float(K[i, j] * K[j, k] * K[k, ell] * K[ell, i])
                    direct += value
                    distinct = len({i, j, k, ell})
                    if distinct == 1:
                        one += value
                    elif distinct == 2:
                        two += value
                    elif distinct == 3:
                        three += value
                    elif distinct == 4:
                        four += value
                        q4 += value
                    else:  # pragma: no cover
                        raise AssertionError("invalid distinct-index count")

    s2 = 0.0
    s4 = 0.0
    t3 = 0.0
    w30 = 0.0
    w31 = 0.0
    for i in cset:
        for j in range(n):
            if j != i:
                s2 += float(K[i, j] ** 2)
                s4 += float(K[i, j] ** 4)
        for j in range(n):
            for k in range(n):
                if len({i, j, k}) == 3:
                    t3 += float(K[i, j] * K[j, k] * K[k, i])
                    w31 += float((K[i, j] ** 2) * (K[j, k] ** 2))
        for j in range(n):
            for ell in range(n):
                if len({i, j, ell}) == 3:
                    w30 += float((K[i, j] ** 2) * (K[i, ell] ** 2))

    return {
        "core_size": float(len(cset)),
        "s2": s2,
        "s4": s4,
        "t3": t3,
        "w30": w30,
        "w31": w31,
        "q4": q4,
        "direct_numerator": direct,
        "one_distinct_direct": one,
        "two_distinct_direct": two,
        "three_distinct_direct": three,
        "four_distinct_direct": four,
        "pair_part": 6.0 * s2 + s4,
        "three_index_part": 4.0 * t3 + w30 + w31,
    }


def validate() -> dict[str, Any]:
    cases: list[dict[str, Any]] = []
    maximum_error = 0.0
    maximum_class_error = 0.0
    for n in (5, 6, 7):
        for seed in (11, 29, 47):
            rng = np.random.default_rng(seed + 100 * n)
            points = np.cumsum(rng.uniform(0.31, 1.47, size=n))
            sinc_matrix = build_sinc_kernel(points)
            raw = rng.uniform(-0.75, 0.75, size=(n, n))
            generic_matrix = 0.5 * (raw + raw.T)
            np.fill_diagonal(generic_matrix, 1.0)
            matrices = [("sinc", sinc_matrix), ("generic_symmetric_unit_diagonal", generic_matrix)]
            core_sets = [
                np.arange(n, dtype=np.int64),
                np.arange(0, n, 2, dtype=np.int64),
                np.arange(1, n - 1, dtype=np.int64),
            ]
            for matrix_type, K in matrices:
                for core in core_sets:
                    if core.size == 0:
                        continue
                    optimized = anchored_collision_terms(K, core).to_dict()
                    brute = brute_force_terms(K, core)
                    keys = ("s2", "s4", "t3", "w30", "w31", "q4", "direct_numerator")
                    errors = {key: abs(float(optimized[key]) - float(brute[key])) for key in keys}
                    class_errors = {
                        "one": abs(float(core.size) - brute["one_distinct_direct"]),
                        "two": abs(float(optimized["pair_part"]) - brute["two_distinct_direct"]),
                        "three": abs(float(optimized["three_index_part"]) - brute["three_distinct_direct"]),
                        "four": abs(float(optimized["q4"]) - brute["four_distinct_direct"]),
                    }
                    maximum_error = max(maximum_error, *errors.values())
                    maximum_class_error = max(maximum_class_error, *class_errors.values())
                    cases.append(
                        {
                            "n": n,
                            "seed": seed,
                            "matrix_type": matrix_type,
                            "core_indices": core.tolist(),
                            "term_absolute_errors": errors,
                            "index_class_absolute_errors": class_errors,
                        }
                    )

    tolerance = 2e-12
    status = "PASS" if max(maximum_error, maximum_class_error) <= tolerance else "FAIL"
    result = {
        "document_id": "Experiment3BS_Independent_Collision_Validation_v1_1",
        "method": "explicit ordered quadruple enumeration; Q4 computed directly over all-distinct tuples",
        "cases_tested": len(cases),
        "matrix_sizes": [5, 6, 7],
        "matrix_types": ["sinc", "generic_symmetric_unit_diagonal"],
        "maximum_term_absolute_error": maximum_error,
        "maximum_index_class_absolute_error": maximum_class_error,
        "tolerance": tolerance,
        "status": status,
        "cases": cases,
    }
    if status != "PASS":
        raise RuntimeError(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    result = validate()
    out = HERE.parent / "04_report" / "independent_collision_validation_v1_1.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in result if k != "cases"}, indent=2, sort_keys=True))
