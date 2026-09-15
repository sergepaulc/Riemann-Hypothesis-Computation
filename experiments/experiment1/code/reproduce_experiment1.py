
#!/usr/bin/env python3
"""Reproduce the principal Experiment 1 pair-correlation outputs.

This public runner uses the frozen unfolded point files shipped in the final
Experiment 1 archive. It recomputes the edge-corrected histograms and the two
headline integrated diagnostics without modifying the archived artifacts.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import quad

HERE = Path(__file__).resolve().parent
EXP = HERE.parent
FROZEN = EXP / "frozen_release"

DATASETS = {
    "first_10000": (
        FROZEN / "02_primary_low_height" / "zeta_unfolded_points.csv",
        "x_unfolded",
    ),
    "near_1e12": (
        FROZEN / "04_high_height_controls" / "near_1e12_unfolded_points.csv",
        "theta_unfolded_relative_x",
    ),
    "near_1e21": (
        FROZEN / "04_high_height_controls" / "near_1e21_unfolded_points.csv",
        "theta_unfolded_relative_x",
    ),
}


def positive_differences(points: np.ndarray, umax: float) -> np.ndarray:
    pts = np.sort(np.asarray(points, dtype=np.float64))
    pieces: list[np.ndarray] = []
    for i in range(len(pts) - 1):
        stop = np.searchsorted(pts, pts[i] + umax, side="right")
        if stop > i + 1:
            pieces.append(pts[i + 1 : stop] - pts[i])
    return np.concatenate(pieces) if pieces else np.empty(0, dtype=np.float64)


def gue_r2(u: float | np.ndarray) -> float | np.ndarray:
    return 1.0 - np.sinc(u) ** 2


def analyze(points: np.ndarray, umax: float = 30.0, bin_width: float = 0.1) -> tuple[dict, pd.DataFrame]:
    pts = np.sort(np.asarray(points, dtype=np.float64))
    if len(pts) != 10_000 or not np.all(np.isfinite(pts)) or not np.all(np.diff(pts) > 0):
        raise ValueError("expected 10,000 finite, strictly increasing unfolded points")
    n = len(pts)
    span = float(pts[-1] - pts[0])
    rho2 = n * (n - 1) / span**2
    diffs = positive_differences(pts, umax)
    edges = np.arange(0.0, umax + 0.5 * bin_width, bin_width)
    counts, edges = np.histogram(diffs, bins=edges)
    centers = 0.5 * (edges[:-1] + edges[1:])
    empirical = counts / (rho2 * (span - centers) * bin_width)

    expected_below_half = rho2 * quad(
        lambda u: float(gue_r2(u)) * (span - u),
        0.0,
        0.5,
        epsabs=1e-12,
        epsrel=1e-12,
        limit=200,
    )[0]
    observed_below_half = int(np.count_nonzero((diffs > 0) & (diffs < 0.5)))
    d05 = 1.0 - observed_below_half / expected_below_half
    s30 = float(np.sum((empirical - 1.0) * bin_width))

    table = pd.DataFrame(
        {
            "u_center": centers,
            "empirical_pair_correlation": empirical,
            "gue_at_bin_center": gue_r2(centers),
            "pair_count": counts,
        }
    )
    summary = {
        "n_points": n,
        "span": span,
        "mean_spacing": float(np.mean(np.diff(pts))),
        "observed_pairs_u_lt_0_5": observed_below_half,
        "gue_expected_pairs_u_lt_0_5": float(expected_below_half),
        "D0_5": float(d05),
        "S30_histogram": s30,
    }
    return summary, table


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=EXP / "reproduced")
    parser.add_argument("--no-validate", action="store_true")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    frozen = pd.read_csv(FROZEN / "04_high_height_controls" / "high_height_replication_summary.csv")
    frozen_map = {
        "first_10000": frozen.iloc[0],
        "near_1e12": frozen.iloc[1],
        "near_1e21": frozen.iloc[2],
    }

    all_summary: dict[str, dict] = {}
    checks: list[dict] = []
    for name, (path, column) in DATASETS.items():
        points = pd.read_csv(path)[column].to_numpy(dtype=np.float64)
        summary, table = analyze(points)
        all_summary[name] = summary
        table.to_csv(args.output_dir / f"{name}_pair_correlation_reproduced.csv", index=False)

        ref = frozen_map[name]
        d05_error = abs(summary["D0_5"] - float(ref["D05_full_block"]))
        s30_error = abs(summary["S30_histogram"] - float(ref["S30_full_block"]))
        observed_match = summary["observed_pairs_u_lt_0_5"] == int(ref["observed_pairs_u_lt_0_5"])
        passed = observed_match and d05_error <= 1e-6 and s30_error <= 5e-6
        checks.append(
            {
                "dataset": name,
                "observed_pair_count_match": observed_match,
                "D0_5_abs_error": d05_error,
                "S30_abs_error": s30_error,
                "passed": passed,
            }
        )

    result = {
        "experiment": "Project Montecito Experiment 1",
        "status": "PASS" if all(c["passed"] for c in checks) else "FAIL",
        "summaries": all_summary,
        "validation_checks": checks,
        "note": "Recomputed from frozen unfolded coordinates; raw third-party tables are not required.",
    }
    (args.output_dir / "experiment1_reproduction_summary.json").write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if args.no_validate or result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
