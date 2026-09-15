#!/usr/bin/env python3
"""Project Montecito Experiment 3BS corrected release runner v1.1.

Re-executes the immutable bounded-study protocol and deterministically generates
all primary and derived result tables. This is an exploratory finite-sample study,
not the deferred full confirmatory Experiment 3.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import resource
import sys
import time
from typing import Any

import numpy as np

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
sys.path.insert(0, str(HERE))

from runtime_src.collision_decomposition import anchored_collision_terms
from runtime_src.cue_cmv import cue_points_cmv
from runtime_src.poisson_control import poisson_circular_points
from runtime_src.sinc_kernel import build_sinc_kernel
from runtime_src.spectral_moments import core_product_rows, moments_from_core_rows, raw_moments
from runtime_src.zeta_inputs import load_point_csv, sha256_file
from aggregate_results_v1_1 import generate_summary_tables

PROTOCOL = BASE / "00_protocol" / "Experiment3_Bounded_Cloud_Closure_Protocol_v1.md"
RESULTS = BASE / "02_results"
FIGURES = BASE / "03_figures"
REPORT = BASE / "04_report"
INTEGRITY = BASE / "05_integrity"
INPUT_DIR = BASE / "00_protocol"

DATASETS = {
    "D0_first_10000": "D0_zeta_first_10000_unfolded.csv",
    "D1_near_1e12": "D1_zeta_near_1e12_unfolded.csv",
    "D2_near_1e21": "D2_zeta_near_1e21_unfolded.csv",
}
WINDOW_STARTS = np.rint(np.linspace(0, 9488, 16)).astype(int)
OUTER_SIZE = 512
CORE = np.arange(192, 320, dtype=np.int64)
N_CONTROLS = 64
METRICS = ["mu2", "mu3", "mu4_raw", "mu4_gt2", "q4_per_core", "pair_part_per_core"]


def protocol_sha() -> str:
    return sha256_file(PROTOCOL)


def seed_for(label: str, index: int = 0) -> int:
    material = f"{protocol_sha()}|{label}|{index:08d}".encode("utf-8")
    digest = hashlib.sha256(material).digest()
    return int.from_bytes(digest[:8], "big", signed=False)


def point_metrics(points: np.ndarray, source: str, index: int) -> dict[str, Any]:
    x = np.asarray(points, dtype=np.float64)
    if x.shape != (OUTER_SIZE,):
        raise ValueError(f"expected {OUTER_SIZE} points, got {x.shape}")
    if not np.all(np.diff(x) > 0):
        raise ValueError("points are not strictly increasing")
    K = build_sinc_kernel(x, row_block=256)
    K_core, K2_core = core_product_rows(K, CORE)
    moments = moments_from_core_rows(K_core, K2_core)
    terms = anchored_collision_terms(K, CORE, precomputed_rows=(K_core, K2_core))
    td = terms.to_dict()
    # Q4 is computed as a residual in the production path. The resulting closure
    # residual is retained only as an algebraic bookkeeping value; it is not an
    # independent validation. Independent explicit-enumeration tests are shipped.
    closure_residual = float(td["algebraic_closure_residual_by_construction"])
    return {
        "source": source,
        "index": int(index),
        "point_count": int(x.size),
        "span": float(x[-1] - x[0]),
        "mean_spacing": float(np.mean(np.diff(x))),
        "mu1": float(moments[1]),
        "mu2": float(moments[2]),
        "mu3": float(moments[3]),
        "mu4_raw": float(moments[4]),
        "mu4_gt2": float(td["mu4_gt2"]),
        "q4_per_core": float(td["q4_per_core"]),
        "pair_part_per_core": float(td["pair_part"] / len(CORE)),
        "three_index_part_per_core": float(td["three_index_part"] / len(CORE)),
        "algebraic_closure_residual_by_construction": closure_residual,
    }


def write_csv(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def summarize(values: np.ndarray) -> dict[str, float]:
    x = np.asarray(values, dtype=np.float64)
    return {
        "n": int(x.size),
        "mean": float(np.mean(x)),
        "sd": float(np.std(x, ddof=1)) if x.size > 1 else 0.0,
        "median": float(np.median(x)),
        "q025": float(np.quantile(x, 0.025)),
        "q975": float(np.quantile(x, 0.975)),
        "min": float(np.min(x)),
        "max": float(np.max(x)),
    }


def bootstrap_cue_mean_comparison(
    zeta_values: np.ndarray,
    cue_values: np.ndarray,
    label: str,
    draws: int = 20000,
) -> dict[str, float]:
    rng = np.random.default_rng(seed_for(f"bootstrap_{label}"))
    zmean = float(np.mean(zeta_values))
    cmean = float(np.mean(cue_values))
    csd = float(np.std(cue_values, ddof=1))
    indices = rng.integers(0, cue_values.size, size=(draws, zeta_values.size))
    boot_means = np.mean(cue_values[indices], axis=1)
    boot_mean_sd = float(np.std(boot_means, ddof=1))
    centered_distance = abs(zmean - cmean)
    tail = float((1 + np.count_nonzero(np.abs(boot_means - cmean) >= centered_distance)) / (draws + 1))
    percentile = float((np.count_nonzero(boot_means <= zmean) + 0.5) / (draws + 1))
    return {
        "zeta_mean": zmean,
        "cue_mean": cmean,
        "difference": zmean - cmean,
        "cue_window_sd": csd,
        "effect_in_cue_window_sd": (zmean - cmean) / csd if csd > 0 else math.nan,
        "cue_16_window_mean_bootstrap_sd": boot_mean_sd,
        "effect_in_cue_16_window_mean_bootstrap_sd": (zmean - cmean) / boot_mean_sd if boot_mean_sd > 0 else math.nan,
        "bootstrap_mean_q025": float(np.quantile(boot_means, 0.025)),
        "bootstrap_mean_q975": float(np.quantile(boot_means, 0.975)),
        "bootstrap_mean_percentile": percentile,
        "bootstrap_two_sided_tail_descriptive": tail,
        "bootstrap_draws": draws,
        "warning": "Exploratory descriptive bootstrap; not a preregistered confirmatory p-value.",
    }


def homometric_control() -> dict[str, Any]:
    A = 0.5 * np.asarray([0, 1, 2, 6, 8, 11], dtype=np.float64)
    B = 0.5 * np.asarray([0, 1, 6, 7, 9, 11], dtype=np.float64)
    def distance_multiset(x: np.ndarray) -> list[float]:
        return sorted(float(x[j] - x[i]) for i in range(len(x)) for j in range(i + 1, len(x)))
    KA = build_sinc_kernel(A)
    KB = build_sinc_kernel(B)
    mA = raw_moments(KA)
    mB = raw_moments(KB)
    return {
        "A": A.tolist(),
        "B": B.tolist(),
        "pair_distance_multisets_identical": distance_multiset(A) == distance_multiset(B),
        "moments_A": {str(k): float(v) for k, v in mA.items()},
        "moments_B": {str(k): float(v) for k, v in mB.items()},
        "differences_A_minus_B": {str(k): float(mA[k] - mB[k]) for k in mA},
    }


def lattice_control() -> dict[str, Any]:
    return point_metrics(np.arange(OUTER_SIZE, dtype=np.float64), "lattice", 0)


def make_figures(all_rows: list[dict[str, Any]], summaries: dict[str, Any]) -> list[str]:
    import matplotlib.pyplot as plt

    FIGURES.mkdir(parents=True, exist_ok=True)
    order = ["D0_first_10000", "D1_near_1e12", "D2_near_1e21", "CUE", "Poisson"]
    labels = ["zeta first 10k", "zeta near 1e12", "zeta near 1e21", "CUE", "Poisson"]
    generated: list[str] = []
    for metric, title, ylabel in [
        ("mu2", "Second sinc-kernel moment", r"$\mu_2$"),
        ("mu4_raw", "Raw fourth sinc-kernel moment", r"$\mu_4$"),
        ("mu4_gt2", "Collision-reduced fourth-moment component", r"$\mu_4^{(>2)}$"),
    ]:
        data = [np.asarray([r[metric] for r in all_rows if r["source"] == group]) for group in order]
        fig, ax = plt.subplots(figsize=(10, 5.5))
        ax.boxplot(data, tick_labels=labels, showmeans=True)
        ax.set_title(title)
        ax.set_ylabel(ylabel)
        ax.tick_params(axis="x", rotation=20)
        ax.grid(axis="y", alpha=0.25)
        fig.tight_layout()
        path = FIGURES / f"{metric}_boxplot.png"
        fig.savefig(path, dpi=180)
        plt.close(fig)
        generated.append(str(path.relative_to(BASE)))

    # Height trajectory relative to CUE mean and empirical 95% window interval.
    for metric, ylabel in [("mu2", r"$\mu_2$"), ("mu4_raw", r"$\mu_4$"), ("mu4_gt2", r"$\mu_4^{(>2)}$")]:
        cue = summaries["CUE"][metric]
        zgroups = ["D0_first_10000", "D1_near_1e12", "D2_near_1e21"]
        zmeans = [summaries[g][metric]["mean"] for g in zgroups]
        zsd = [summaries[g][metric]["sd"] for g in zgroups]
        fig, ax = plt.subplots(figsize=(8, 5))
        x = np.arange(3)
        ax.errorbar(x, zmeans, yerr=zsd, marker="o", capsize=4, label="zeta mean ± block SD")
        ax.axhline(cue["mean"], linestyle="--", label="CUE mean")
        ax.axhspan(cue["q025"], cue["q975"], alpha=0.15, label="CUE 2.5–97.5% window range")
        ax.set_xticks(x, ["first 10k", "near 1e12", "near 1e21"])
        ax.set_ylabel(ylabel)
        ax.set_title(f"Zeta height trajectory for {metric}")
        ax.grid(axis="y", alpha=0.25)
        ax.legend()
        fig.tight_layout()
        path = FIGURES / f"{metric}_height_trajectory.png"
        fig.savefig(path, dpi=180)
        plt.close(fig)
        generated.append(str(path.relative_to(BASE)))
    return generated


def main() -> int:
    for directory in [RESULTS, FIGURES, REPORT, INTEGRITY]:
        directory.mkdir(parents=True, exist_ok=True)
    start = time.perf_counter()
    psha = protocol_sha()
    print(f"protocol_sha256={psha}", flush=True)
    print(f"window_starts={WINDOW_STARTS.tolist()}", flush=True)

    rows: list[dict[str, Any]] = []
    input_hashes: dict[str, str] = {}

    for dataset, filename in DATASETS.items():
        path = INPUT_DIR / filename
        input_hashes[filename] = sha256_file(path)
        points = load_point_csv(path)
        for idx, start_idx in enumerate(WINDOW_STARTS):
            row = point_metrics(points[start_idx : start_idx + OUTER_SIZE], dataset, idx)
            row["window_start"] = int(start_idx)
            rows.append(row)
        print(f"completed {dataset}: 16 windows", flush=True)

    for idx in range(N_CONTROLS):
        rng = np.random.default_rng(seed_for("CUE", idx))
        points = cue_points_cmv(OUTER_SIZE, rng)
        row = point_metrics(points, "CUE", idx)
        row["window_start"] = -1
        rows.append(row)
        if (idx + 1) % 8 == 0:
            print(f"completed CUE {idx + 1}/{N_CONTROLS}", flush=True)

    for idx in range(N_CONTROLS):
        rng = np.random.default_rng(seed_for("Poisson", idx))
        points = poisson_circular_points(OUTER_SIZE, rng)
        row = point_metrics(points, "Poisson", idx)
        row["window_start"] = -1
        rows.append(row)
    print(f"completed Poisson {N_CONTROLS}/{N_CONTROLS}", flush=True)

    lattice = lattice_control()
    homometric = homometric_control()
    write_csv(RESULTS / "all_window_endpoints.csv", rows)

    groups = sorted({row["source"] for row in rows})
    summaries: dict[str, Any] = {}
    for group in groups:
        summaries[group] = {}
        grows = [row for row in rows if row["source"] == group]
        for metric in METRICS:
            summaries[group][metric] = summarize(np.asarray([row[metric] for row in grows]))
        summaries[group]["mean_spacing"] = summarize(np.asarray([row["mean_spacing"] for row in grows]))
        summaries[group]["max_absolute_algebraic_closure_residual_by_construction"] = max(
            abs(float(row["algebraic_closure_residual_by_construction"])) for row in grows
        )

    comparisons: dict[str, Any] = {}
    cue_rows = [row for row in rows if row["source"] == "CUE"]
    for dataset in DATASETS:
        comparisons[dataset] = {}
        zrows = [row for row in rows if row["source"] == dataset]
        for metric in ["mu2", "mu3", "mu4_raw", "mu4_gt2", "q4_per_core"]:
            comparisons[dataset][metric] = bootstrap_cue_mean_comparison(
                np.asarray([r[metric] for r in zrows]),
                np.asarray([r[metric] for r in cue_rows]),
                f"{dataset}_{metric}",
            )

    uncertainty_rows: list[dict[str, Any]] = []
    for dataset in DATASETS:
        for metric in ["mu2", "mu3", "mu4_raw", "mu4_gt2"]:
            comp = comparisons[dataset][metric]
            uncertainty_rows.append(
                {
                    "dataset": dataset,
                    "metric": metric,
                    "difference_vs_CUE": comp["difference"],
                    "cue_individual_window_sd": comp["cue_window_sd"],
                    "effect_in_cue_individual_window_sd": comp["effect_in_cue_window_sd"],
                    "cue_16_window_mean_bootstrap_sd": comp["cue_16_window_mean_bootstrap_sd"],
                    "effect_in_cue_16_window_mean_bootstrap_sd": comp["effect_in_cue_16_window_mean_bootstrap_sd"],
                    "bootstrap_two_sided_tail_descriptive": comp["bootstrap_two_sided_tail_descriptive"],
                }
            )
    write_csv(RESULTS / "uncertainty_scale_comparison.csv", uncertainty_rows)

    derived_table_validation = generate_summary_tables(RESULTS)
    figures = make_figures(rows, summaries)
    elapsed = time.perf_counter() - start
    peak_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    # Linux ru_maxrss is KiB; macOS reports bytes.
    peak_rss_bytes = int(peak_rss * 1024) if platform.system() == "Linux" else int(peak_rss)

    result = {
        "document_id": "Project_Montecito_Experiment3BS_Results_v1_1",
        "classification": "EXPLORATORY_FINITE_SAMPLE_CLOSURE_STUDY",
        "protocol_sha256": psha,
        "scientific_parameters": {
            "zeta_datasets": list(DATASETS),
            "zeta_windows_per_dataset": 16,
            "window_starts": WINDOW_STARTS.tolist(),
            "outer_size": OUTER_SIZE,
            "core_size": int(CORE.size),
            "halo_per_side": 192,
            "cue_realizations": N_CONTROLS,
            "poisson_realizations": N_CONTROLS,
            "D3_accessed": False,
            "pair_matched_surrogates_used": False,
        },
        "input_sha256": input_hashes,
        "summaries": summaries,
        "zeta_vs_cue_descriptive_comparisons": comparisons,
        "lattice_control": lattice,
        "homometric_control": homometric,
        "derived_table_validation": derived_table_validation,
        "uncertainty_scale_table": "02_results/uncertainty_scale_comparison.csv",
        "collision_validation_note": (
            "The production Q4 term is residual-based. Its algebraic closure residual is not "
            "an independent check; independent brute-force validation is shipped in 04_report/"
            "independent_collision_validation_v1_1.json and 01_code/tests/."
        ),
        "figures": figures,
        "runtime": {
            "elapsed_seconds": elapsed,
            "peak_rss_bytes": peak_rss_bytes,
            "peak_rss_gib": peak_rss_bytes / 1024**3,
            "platform": platform.platform(),
            "python": sys.version,
            "numpy": np.__version__,
        },
        "claim_boundary": "No RH claim; no theorem validation; no proof that differences are beyond the complete two-point law; no confirmatory p-values.",
        "terminal_status": "EXPERIMENT3BS_COMPLETE_CORRECTED_RELEASE_V1_1",
    }
    (RESULTS / "bounded_cloud_results.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (RESULTS / "lattice_control.json").write_text(json.dumps(lattice, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (RESULTS / "homometric_control.json").write_text(json.dumps(homometric, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    (RESULTS / "descriptive_comparisons.json").write_text(json.dumps(comparisons, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["terminal_status"], "elapsed_seconds": elapsed, "peak_rss_gib": result["runtime"]["peak_rss_gib"]}, indent=2), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
