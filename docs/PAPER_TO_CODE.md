
# Paper-to-code map

| Manuscript section | Computation | Primary code | Frozen outputs |
|---|---|---|---|
| §4, Experiment 1 | unfolding, edge-corrected pair correlation, `D_0.5`, high-height comparison | `experiments/experiment1/code/reproduce_experiment1.py`; original fragments in `experiments/experiment1/frozen_release/02_primary_low_height/` and `04_high_height_controls/` | `experiments/experiment1/frozen_release/02_primary_low_height/`, `03_validation/`, `04_high_height_controls/` |
| §5, Experiment 2 | Gaussian Gram matrices, spectra, inertia, bridge, sensitivity | `experiments/experiment2/frozen_release/src/experiment2_run.py` | `experiments/experiment2/frozen_release/02_results/` |
| §5 independent verification | checksums, identities, spectra, sign resolution | `experiments/experiment2/frozen_release/src/verify_experiment2.py` | `experiments/experiment2/frozen_release/05_reproducibility/` |
| §5 robustness | independent kernel-width and spectral diagnostics | `experiments/experiment2/validation_release/src/independent_validate.py` | `experiments/experiment2/validation_release/01_results/` |
| §6, Experiment 3 | sinc moments, collision decomposition, CUE/Poisson/lattice/homometric controls | `experiments/experiment3/frozen_release/01_code/run_experiment3bs_v1_1.py` | `experiments/experiment3/frozen_release/02_results/` |
| §6 exact validation | brute-force collision classes, independent moment paths, unit tests | `validate_collision_decomposition_v1_1.py`, `validate_moments_v1_1.py`, `tests/test_experiment3bs_v1_1.py` | `experiments/experiment3/frozen_release/04_report/` |

The repository preserves the historical frozen releases and provides top-level
runners that reproduce them in `build/` without modifying committed evidence.
