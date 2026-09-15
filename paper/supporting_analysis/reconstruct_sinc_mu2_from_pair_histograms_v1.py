#!/usr/bin/env python3
"""Reconstruct Experiment 3's core-anchored sinc mu2 from Experiment 1 pair histograms.

This is a paper-review diagnostic. It uses the fixed Experiment 3 bounded-study
geometry: 512-point outer window, 128-point central core, and 192-point halos.
The Experiment 1 empirical R2 histogram is used on 0<u<=30; beyond 30 we set
R2=1. The tail completion differs from the sine-process tail by <1e-7 in mu2.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import quad

REPO = Path(__file__).resolve().parents[2]
EXP1 = REPO / 'experiments' / 'experiment1' / 'frozen_release'
EXP3_RESULTS = REPO / 'experiments' / 'experiment3' / 'frozen_release' / '02_results'
OUTDIR = Path(__file__).resolve().parent / 'generated'

CORE_LENGTH = 128.0
HALO = 192.0
MAX_U = HALO + CORE_LENGTH
HIST_MAX_U = 30.0
CUE_N = 512

DATASETS = {
    'Z0': (EXP1 / '02_primary_low_height' / 'zeta_pair_correlation.csv', 'empirical_full'),
    'Z12': (EXP1 / '04_high_height_controls' / 'near_1e12_pair_correlation.csv', 'empirical_pair_correlation'),
    'Z21': (EXP1 / '04_high_height_controls' / 'near_1e21_pair_correlation.csv', 'empirical_pair_correlation'),
}


def sinc2(u: float) -> float:
    return float(np.sinc(u) ** 2)


def overlap_weight(u: float) -> float:
    """Spatial core/outer overlap for a centered core and symmetric halos."""
    u = abs(float(u))
    if u <= HALO:
        return CORE_LENGTH
    if u <= MAX_U:
        return MAX_U - u
    return 0.0


def integrate_segmented(fn, a: float, b: float, step: float = 1.0) -> float:
    total = 0.0
    x = float(a)
    while x < b - 1e-14:
        y = min(x + step, b)
        total += quad(fn, x, y, epsabs=1e-13, epsrel=1e-12, limit=200)[0]
        x = y
    return total


def weighted_sinc2_integral(a: float, b: float) -> float:
    return quad(
        lambda u: overlap_weight(u) * sinc2(u),
        a,
        b,
        epsabs=1e-13,
        epsrel=1e-12,
        limit=200,
    )[0]


def sine_r2(u: float) -> float:
    return 1.0 - sinc2(u)


def cue_r2_finite(u: float, n: int = CUE_N) -> float:
    if abs(u) < 1e-14:
        return 0.0
    denominator = n * np.sin(np.pi * u / n)
    return float(1.0 - (np.sin(np.pi * u) / denominator) ** 2)


def expected_mu2(r2_fn) -> float:
    integral = integrate_segmented(
        lambda u: overlap_weight(u) * sinc2(u) * r2_fn(u),
        0.0,
        MAX_U,
        step=0.5,
    )
    return float(1.0 + 2.0 * integral / CORE_LENGTH)


def empirical_hist_mu2(path: Path, column: str) -> float:
    frame = pd.read_csv(path)
    integral = 0.0
    for row in frame.itertuples(index=False):
        center = float(getattr(row, 'u_center'))
        a = max(0.0, center - 0.05)
        b = center + 0.05
        integral += float(getattr(row, column)) * weighted_sinc2_integral(a, b)
    # Complete the very small long-range tail with R2=1.
    integral += integrate_segmented(
        lambda u: overlap_weight(u) * sinc2(u),
        HIST_MAX_U,
        MAX_U,
        step=1.0,
    )
    return float(1.0 + 2.0 * integral / CORE_LENGTH)


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    sine_mu2 = expected_mu2(sine_r2)
    finite_cue_theory_mu2 = expected_mu2(cue_r2_finite)

    summary = pd.read_csv(EXP3_RESULTS / 'group_summary.csv')
    cue = summary.loc[summary['group'] == 'CUE'].iloc[0]
    cue_mean = float(cue['mu2_mean'])
    cue_sd = float(cue['mu2_sd'])
    cue_se = cue_sd / np.sqrt(int(cue['n']))

    rows = []
    mapping = {
        'Z0': 'D0_first_10000',
        'Z12': 'D1_near_1e12',
        'Z21': 'D2_near_1e21',
    }
    for label, (path, col) in DATASETS.items():
        reconstructed = empirical_hist_mu2(path, col)
        direct = float(summary.loc[summary['group'] == mapping[label], 'mu2_mean'].iloc[0])
        rows.append({
            'dataset': label,
            'mu2_histogram_reconstruction': reconstructed,
            'difference_from_truncated_sine': reconstructed - sine_mu2,
            'experiment3_16_window_mu2_mean': direct,
            'window_mean_minus_histogram_reconstruction': direct - reconstructed,
        })

    df = pd.DataFrame(rows)
    df.to_csv(OUTDIR / 'sinc_mu2_histogram_reconstruction_v1.csv', index=False)

    # Existing Experiment 3 standardized effects, corrected for uncertainty in the 64-window CUE mean.
    uncertainty = pd.read_csv(EXP3_RESULTS / 'uncertainty_scale_comparison.csv')
    uncertainty['cue_reference_mean_se_64'] = uncertainty['cue_individual_window_sd'] / np.sqrt(64.0)
    uncertainty['two_sample_reference_sd'] = np.sqrt(
        uncertainty['cue_16_window_mean_bootstrap_sd'] ** 2
        + uncertainty['cue_reference_mean_se_64'] ** 2
    )
    uncertainty['effect_in_two_sample_reference_sd'] = (
        uncertainty['difference_vs_CUE'] / uncertainty['two_sample_reference_sd']
    )
    uncertainty.to_csv(OUTDIR / 'experiment3_corrected_uncertainty_scales_v1.csv', index=False)

    tail_poisson = integrate_segmented(
        lambda u: overlap_weight(u) * sinc2(u), HIST_MAX_U, MAX_U, step=1.0
    )
    tail_sine = integrate_segmented(
        lambda u: overlap_weight(u) * sinc2(u) * sine_r2(u),
        HIST_MAX_U,
        MAX_U,
        step=1.0,
    )

    result = {
        'geometry': {
            'outer_points': 512,
            'core_points': 128,
            'halo_points_each_side': 192,
            'continuous_core_length': CORE_LENGTH,
            'continuous_halo_length': HALO,
        },
        'truncated_sine_mu2': sine_mu2,
        'finite_CUE_N512_pair_density_mu2': finite_cue_theory_mu2,
        'finite_N_correction': finite_cue_theory_mu2 - sine_mu2,
        'observed_CUE_mu2_mean_64': cue_mean,
        'observed_CUE_window_sd': cue_sd,
        'observed_CUE_mean_se_64': cue_se,
        'observed_CUE_minus_truncated_sine': cue_mean - sine_mu2,
        'observed_CUE_minus_truncated_sine_in_SE': (cue_mean - sine_mu2) / cue_se,
        'histogram_tail_completion_mu2_using_R2_equal_1': 2.0 * tail_poisson / CORE_LENGTH,
        'exact_sine_tail_mu2': 2.0 * tail_sine / CORE_LENGTH,
        'tail_completion_difference': 2.0 * (tail_poisson - tail_sine) / CORE_LENGTH,
        'dataset_rows': rows,
        'interpretation': (
            'The full-sample pair-histogram reconstruction agrees in sign with Experiment 1: '
            'Z0 and Z12 are below the truncated-sine mu2 benchmark, while Z21 is above it. '
            'The direct 16-window Experiment 3 means reverse the ordering of Z12 and Z21, '
            'showing that the earlier marginal-Z12 wording is not robust to benchmark and sampling geometry.'
        ),
    }
    (OUTDIR / 'sinc_mu2_histogram_reconstruction_v1.json').write_text(
        json.dumps(result, indent=2) + '\n', encoding='utf-8'
    )
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
