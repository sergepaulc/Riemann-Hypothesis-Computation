#!/usr/bin/env python3
"""Independent moment checks for the Experiment 3BS corrected release."""
from __future__ import annotations

import json
from pathlib import Path
import sys

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
sys.path.insert(0, str(HERE))

from runtime_src.sinc_kernel import build_sinc_kernel
from runtime_src.spectral_moments import core_diagonal_moments, eigenvalue_moments, raw_moments
from runtime_src.zeta_inputs import load_point_csv


def high_precision_homometric() -> dict:
    mp.mp.dps = 90
    sets = {
        "A": [mp.mpf(v) / 2 for v in (0, 1, 2, 6, 8, 11)],
        "B": [mp.mpf(v) / 2 for v in (0, 1, 6, 7, 9, 11)],
    }

    def sinc(x: mp.mpf) -> mp.mpf:
        return mp.mpf(1) if x == 0 else mp.sin(mp.pi * x) / (mp.pi * x)

    def moments(points: list[mp.mpf]) -> dict[str, str]:
        K = mp.matrix([[sinc(a - b) for b in points] for a in points])
        out = {}
        power = mp.eye(len(points))
        for k in range(1, 5):
            power = power * K
            out[str(k)] = mp.nstr(sum(power[i, i] for i in range(len(points))) / len(points), 85)
        return out

    ma = moments(sets["A"])
    mb = moments(sets["B"])
    diff = mp.mpf(ma["4"]) - mp.mpf(mb["4"])
    return {
        "decimal_precision": mp.mp.dps,
        "moments_A": ma,
        "moments_B": mb,
        "mu4_A_minus_B": mp.nstr(diff, 85),
    }


def dense_crosschecks() -> list[dict]:
    cases = [
        ("D0_first_window", "D0_zeta_first_10000_unfolded.csv", 0),
        ("D1_middle_window", "D1_zeta_near_1e12_unfolded.csv", 4428),
        ("D2_last_window", "D2_zeta_near_1e21_unfolded.csv", 9488),
    ]
    core = np.arange(192, 320, dtype=np.int64)
    records = []
    for label, filename, start in cases:
        points = load_point_csv(BASE / "00_protocol" / filename)[start : start + 512]
        K = build_sinc_kernel(points)
        optimized = core_diagonal_moments(K, core)
        # Independent dense powers: form K^2, K^3, K^4 explicitly and read core diagonals.
        K2 = K @ K
        K3 = K2 @ K
        K4 = K2 @ K2
        dense = {
            1: 1.0,
            2: float(np.mean(np.diag(K2)[core])),
            3: float(np.mean(np.diag(K3)[core])),
            4: float(np.mean(np.diag(K4)[core])),
        }
        errors = {str(k): abs(optimized[k] - dense[k]) for k in (1, 2, 3, 4)}
        records.append({"case": label, "optimized": optimized, "dense_power": dense, "absolute_errors": errors})
    return records


def main() -> int:
    dense = dense_crosschecks()
    max_error = max(err for case in dense for err in case["absolute_errors"].values())
    result = {
        "document_id": "Experiment3BS_Independent_Moment_Validation_v1_1",
        "dense_core_moment_crosschecks": dense,
        "maximum_dense_crosscheck_absolute_error": max_error,
        "dense_crosscheck_tolerance": 2e-12,
        "homometric_high_precision": high_precision_homometric(),
        "status": "PASS" if max_error <= 2e-12 else "FAIL",
    }
    if result["status"] != "PASS":
        raise RuntimeError(json.dumps(result, indent=2, default=str))
    out = BASE / "04_report" / "independent_moment_validation_v1_1.json"
    out.write_text(json.dumps(result, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": result["status"],
        "maximum_dense_crosscheck_absolute_error": max_error,
        "homometric_mu4_A_minus_B": result["homometric_high_precision"]["mu4_A_minus_B"],
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
