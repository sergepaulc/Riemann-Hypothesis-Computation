# Project Montecito — Experiment 1 → Experiment 2 Handoff — Version 2

## Readiness decision

**Experiment 1 is scientifically closed and computationally ready to hand off to Experiment 2.**

The final publication-level provenance formality is now closed. The official raw `zeros1.txt` file is stored unchanged with SHA-256 `3436c916a7878261ac183fd7b9448c9a4736b8bbccf1356874a6ce1788541632`. All 10,000 frozen low-height ordinates agree with the official table within its approximately 3e-9 precision, and recomputation produces exactly the same 300-bin pair-count histogram.

## What Experiment 2 must consume

The primary zeta input remains the frozen:

`zeta_unfolded_points.csv`

from the original first-10,000 Experiment 1 sample.

The primary Level-1 diagnostic remains:

`zeta_pair_correlation.csv`.

The authoritative GUE calibration is the dimension-1200 matched ensemble:

`gue_matched_monte_carlo_200.csv`.

## What Experiment 2 must not do

Do not:

- replace the first-10,000 primary point set with a high-height sample after the fact;
- treat the first-10,000 D0.5 distortion as a universal property of zeta zeros;
- interpret a first-10,000 zeta-vs-GUE inertia difference as higher-order structure before propagating the known Level-1 distortion;
- use the preliminary dimension-256 GUE control for inferential statements;
- use zeta-side block bootstrap/permutation inference as if the contiguous height blocks were exchangeable;
- change the frozen Experiment 2 kernel/lambda/block design because of Experiment 1 results unless the change is explicitly versioned as a new specification.

## Dual-reference policy

The three zeta samples have different roles:

**First 10,000:** primary frozen Experiment 2 artifact; contains a known finite-height Level-1 distortion.

**Near 10^12:** secondary high-height control for what GUE-like zeta looks like at current resolution.

**Near 10^21:** secondary high-height control with the source's explicit accuracy caveat.

## Interpretation sequence for Experiment 2 / 3

1. Run the fixed toy apparatus on the frozen first-10,000 point set.
2. Quantify trace, Frobenius/second-moment, inertia, and the positive-inertia bound exactly as specified.
3. Connect measured matrix second moments to the already-measured pair-correlation Level-1 structure.
4. When synthetic GUE or high-height zeta controls are introduced, report Level-1 differences first.
5. Only residual Level-2 differences not explained by Level-1 propagation may be discussed as possible sensitivity beyond two-point structure.

## Status

`SCIENTIFIC_EXPERIMENT1_CLOSED = TRUE`

`COMPUTATIONAL_EXPERIMENT2_READY = TRUE`

`PUBLICATION_RAW_ZEROS1_BYTE_LOCK = CLOSED`

`EXPERIMENT1_ALL_DATA_PROVENANCE_CLOSED = TRUE`
