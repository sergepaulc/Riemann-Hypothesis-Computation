# Project Montecito — Experiment 1 Closure Report — Version 2

## Purpose

This document formally closes the Experiment 1 phase before Experiment 2.

Experiment 1 evolved through four disciplined stages:

1. **Initial Experiment 1** — pair correlation from the first 10,000 zeta zeros.
2. **Peer review / Experiment 1 Version 2** — corrected the overly strong short-range GUE wording and identified a real low-height D0.5 shape distortion.
3. **Validation Extension** — established the matched GUE calibration, promoted the mass-conserved/shape-shifted interpretation, and removed estimator/unfolding-choice concerns.
4. **High-Height Replication** — showed the low-height distortion is strongly suppressed below the current ~5% D0.5 detection scale at much greater height and closed the nonlinear-unfolding confound.

The result is a frozen Level-1 baseline suitable for the toy Hermitian work in Experiment 2.

## Final scientific state

For the first-10,000 frozen point set:

- strong non-Poisson short-range repulsion;
- qualitative sine-kernel/GUE structure;
- single-window D0.5 approximately 0.224;
- local correlation-hole shape redistributed relative to asymptotic GUE;
- integrated correlation-hole mass approximately conserved;
- effect is not an estimator artifact;
- effect is not a smooth-unfolding-choice artifact;
- effect is not a nonlinear-unfolding artifact;
- high-height controls show suppression below the experiment's ~5% D0.5 resolution.

## Provenance state

### First 10,000

The numerical sequence is independently validated and considered numerically closed.

The authoritative public Odlyzko `zeros1` web source is plain text with 100,000 rows. Its first row and row 10,000 agree with the frozen Experiment 1 endpoints at the source precision.

The exact official raw file is now archived in this package. Its SHA-256 is `3436c916a7878261ac183fd7b9448c9a4736b8bbccf1356874a6ce1788541632`. All 100,000 rows parse correctly and are strictly increasing; all first 10,000 values agree with the frozen Experiment 1 sequence within the official table's approximately 3e-9 precision.

### High-height controls

Raw `zeros3.txt` and `zeros4.txt` are included unchanged and checksum-locked.

## Freeze decision

No further scientific extension is required before Experiment 2.

Intermediate-height convergence-law work, deeper finite-T formulas, larger Monte Carlo tail enumeration, and manuscript-specific raw-file provenance can be pursued later without changing the Experiment 2 baseline.

## Readiness

**Experiment 1 scientific status: CLOSED.**

**Experiment 2 computational readiness: READY.**

**Publication-level official zeros1 raw-byte checksum: CLOSED.**


## Final raw-byte closure addendum

The official `zeros1.txt` file was received and checksum-locked:

`3436c916a7878261ac183fd7b9448c9a4736b8bbccf1356874a6ce1788541632`

A full 10,000-row comparison found maximum absolute difference `2.912202035077e-09` from the frozen numerically regenerated sequence, with **0 / 10,000** rows outside the approximately 3e-9 source precision.

Re-running the original Experiment 1 pair-count computation from the official values changed **0 / 300 bins**. The low-height pair count below 0.5 remains exactly **878**.

There is therefore no remaining data-provenance qualification for Experiment 1.
