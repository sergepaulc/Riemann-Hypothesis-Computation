# Project Montecito - Experiment 2 Execution Log - Version 1

## Scope

Execution follows Project Montecito Specification v0.6. The first 10,000 unfolded zeta zeros remain the primary input. The near-10^12 and near-10^21 zeta samples are secondary controls only.

## Stage A - Pre-registration

Before any Experiment 2 spectra were computed:

1. Copied the frozen v0.6 specification and Experiment 1 handoff documents into `00_preregistration/`.
2. Copied the six frozen Experiment 1 input artifacts into `01_inputs/`.
3. Recorded SHA-256 hashes of all six inputs.
4. Froze the primary Gaussian kernel `sigma=1` and lambda grid `0.10,0.15,...,0.95`.
5. Froze 16 common locations by evenly spacing the 512-point block starts from 1 through 9489.
6. Nested the 256-point and 128-point blocks concentrically inside each 512-point block.
7. Froze the spectrum-first sign protocol, screening rule, direct-H verification subset, and pair-correlation/Frobenius finite-window formula.
8. Wrote the immutable configuration to `experiment2_config_v1_frozen.json` and exact indices to `block_manifest_v1.csv`.

## Stage B - Baseline computation

For each of the three zeta datasets, 16 locations, and three block sizes:

1. Constructed the full untruncated Gaussian Gram matrix.
2. Checked symmetry and unit diagonal.
3. Computed the complete eigenvalue spectrum of C once.
4. Verified C is PSD to the numerical tolerance.
5. Computed every crossing threshold `1/mu_j(C)`.
6. Derived the full H_lambda spectrum for all 18 lambda values using `1-lambda*mu_j(C)`.
7. Recorded resolved positive, negative, and unresolved counts.
8. Verified trace and Frobenius formulas against the spectrum.
9. Evaluated the generic positive-inertia lower bound.
10. Computed the direct points-in Gram Frobenius moment.
11. Predicted that moment from the frozen empirical pair-correlation curve using the translation-edge finite-window formula.

Selected H_lambda matrices were also directly diagonalized at locations 1, 8, and 16, for m=128,256,512 and lambda=0.10,0.50,0.95.

## Stage C - Numerical resolution and finite-window audit

1. Checked all 2,592 block/lambda sign assignments against the screening rule.
2. No eigenvalue entered the high-precision escalation band; no unresolved sign remained.
3. Compared positive-inertia profiles across the 16 fixed locations.
4. Compared nested m=128,256,512 blocks at every common location.
5. Evaluated the exact Gaussian tail budget beyond u=30.
6. Recomputed one primary 512-point Gram spectrum independently with a different SciPy symmetric eigensolver driver.
7. Recomputed the theoretical Gaussian-weighted GUE benchmark independently.
8. Ran 19 independent verification checks; all passed.

## Output status

`SCIENTIFIC_EXPERIMENT2_COMPLETE = TRUE`

`COMPUTATIONAL_EXPERIMENT3_READY = TRUE`

No Experiment 3 synthetic input was generated or analyzed in this execution.
