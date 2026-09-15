#!/usr/bin/env python3
"""Regenerate all derived Experiment 3BS summary tables from endpoint rows.

This module closes the v1 packaging gap identified by independent peer review:
`group_summary.csv` and `mu4_difference_decomposition_vs_cue.csv` are now
produced deterministically from `all_window_endpoints.csv`.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any

import numpy as np

GROUP_ORDER = [
    "D0_first_10000",
    "D1_near_1e12",
    "D2_near_1e21",
    "CUE",
    "Poisson",
]
ZETA_GROUPS = GROUP_ORDER[:3]


def _read_rows(path: Path) -> list[dict[str, Any]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError(f"no endpoint rows in {path}")
    numeric = {
        "index",
        "point_count",
        "span",
        "mean_spacing",
        "mu1",
        "mu2",
        "mu3",
        "mu4_raw",
        "mu4_gt2",
        "q4_per_core",
        "pair_part_per_core",
        "three_index_part_per_core",
        "algebraic_closure_residual_by_construction",
        "window_start",
    }
    converted: list[dict[str, Any]] = []
    for row in rows:
        out: dict[str, Any] = dict(row)
        for key in numeric:
            if key in out and out[key] != "":
                out[key] = float(out[key])
        converted.append(out)
    return converted


def _mean(rows: list[dict[str, Any]], key: str) -> float:
    return float(np.mean(np.asarray([float(r[key]) for r in rows], dtype=np.float64)))


def _sd(rows: list[dict[str, Any]], key: str) -> float:
    values = np.asarray([float(r[key]) for r in rows], dtype=np.float64)
    return float(np.std(values, ddof=1)) if values.size > 1 else 0.0


def _write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    if not rows:
        raise ValueError("cannot write empty CSV")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def generate_summary_tables(results_dir: Path) -> dict[str, Any]:
    """Generate summary/decomposition tables and return validation metadata."""
    endpoint_path = results_dir / "all_window_endpoints.csv"
    rows = _read_rows(endpoint_path)
    by_group = {group: [row for row in rows if row["source"] == group] for group in GROUP_ORDER}
    missing = [group for group, grows in by_group.items() if not grows]
    if missing:
        raise ValueError(f"missing endpoint groups: {missing}")

    summary_rows: list[dict[str, Any]] = []
    for group in GROUP_ORDER:
        grows = by_group[group]
        summary_rows.append(
            {
                "group": group,
                "n": len(grows),
                "mean_spacing": _mean(grows, "mean_spacing"),
                "mu2_mean": _mean(grows, "mu2"),
                "mu2_sd": _sd(grows, "mu2"),
                "mu3_mean": _mean(grows, "mu3"),
                "mu3_sd": _sd(grows, "mu3"),
                "mu4_raw_mean": _mean(grows, "mu4_raw"),
                "mu4_raw_sd": _sd(grows, "mu4_raw"),
                "pair_part_mean": _mean(grows, "pair_part_per_core"),
                "mu4_gt2_mean": _mean(grows, "mu4_gt2"),
                "mu4_gt2_sd": _sd(grows, "mu4_gt2"),
                "q4_per_core_mean": _mean(grows, "q4_per_core"),
                "q4_per_core_sd": _sd(grows, "q4_per_core"),
            }
        )

    summary_path = results_dir / "group_summary.csv"
    _write_csv(summary_path, summary_rows)
    summary_by_group = {row["group"]: row for row in summary_rows}
    cue = summary_by_group["CUE"]

    decomposition_rows: list[dict[str, Any]] = []
    max_additive_error = 0.0
    for dataset in ZETA_GROUPS:
        row = summary_by_group[dataset]
        raw = float(row["mu4_raw_mean"] - cue["mu4_raw_mean"])
        pair = float(row["pair_part_mean"] - cue["pair_part_mean"])
        gt2 = float(row["mu4_gt2_mean"] - cue["mu4_gt2_mean"])
        max_additive_error = max(max_additive_error, abs(raw - pair - gt2))
        decomposition_rows.append(
            {
                "dataset": dataset,
                "raw_mu4_difference_vs_CUE": raw,
                "pair_part_difference": pair,
                "gt2_difference": gt2,
                "pair_share_of_raw_difference": pair / raw if raw != 0.0 else float("nan"),
                "gt2_share_of_raw_difference": gt2 / raw if raw != 0.0 else float("nan"),
            }
        )

    decomposition_path = results_dir / "mu4_difference_decomposition_vs_cue.csv"
    _write_csv(decomposition_path, decomposition_rows)

    validation = {
        "document_id": "Experiment3BS_Derived_Table_Validation_v1_1",
        "source": "02_results/all_window_endpoints.csv",
        "endpoint_rows": len(rows),
        "group_counts": {group: len(by_group[group]) for group in GROUP_ORDER},
        "generated_files": [summary_path.name, decomposition_path.name],
        "max_group_identity_error_raw_minus_pair_minus_gt2": max_additive_error,
        "tolerance": 1e-12,
        "status": "PASS" if max_additive_error <= 1e-12 else "FAIL",
    }
    (results_dir / "derived_table_validation.json").write_text(
        json.dumps(validation, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    if validation["status"] != "PASS":
        raise RuntimeError(f"derived-table identity failed: {max_additive_error}")
    return validation


if __name__ == "__main__":
    base = Path(__file__).resolve().parents[1]
    print(json.dumps(generate_summary_tables(base / "02_results"), indent=2, sort_keys=True))
