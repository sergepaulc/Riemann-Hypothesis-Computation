# Paper-to-computation map

All paths below are relative to the repository root. The numeric directory prefixes and implementation filenames are retained to minimize changes to working code.

| Paper content | Code or command | Data and reference results |
|---|---|---|
| Section 4; pair correlation at three heights; Figures 1–2 | `python scripts/reproduce.py --experiment 1` | `experiments/experiment1/frozen_release/02_primary_low_height/` and `04_high_height_controls/` |
| Section 4; finite-GUE calibration | Reference outputs; not resimulated by the main runner | `experiments/experiment1/frozen_release/03_validation/gue_matched_monte_carlo_200.csv` and its configuration |
| Section 5; Gaussian spectra, inertia and bridge; Figure 3 | `python scripts/reproduce.py --experiment 2` | `experiments/experiment2/frozen_release/02_results/` |
| Section 5; supplementary kernel-width sensitivity | `python scripts/reproduce.py --experiment 2-validation` | `experiments/experiment2/validation_release/01_results/` |
| Section 6; homometric control; Figure 4 | Experiment 3 runner, moment validator and unit tests | `experiments/experiment3/frozen_release/02_results/homometric_control.json` |
| Section 6; zeta/CUE/Poisson moments; Figure 5 | Experiment 3 runner and aggregation script | `all_window_endpoints.csv` and `group_summary.csv` in Experiment 3 `02_results/` |
| Section 6; pair-histogram reconstruction; Figure 6 | Formula in Section 2.7; stored histograms and reference paper figure | Experiment 1 pair histograms and Experiment 3 second-moment outputs; no dedicated full-panel reconstruction script is claimed |
| Section 6; uncertainty comparison; Figure 7 | Formulas in Section 2.8; endpoint means and sample deviations | Experiment 3 endpoint rows; note that its stored bootstrap comparison is distinct from the paper's finite-reference mean scale |
| Section 6; fourth-moment decomposition; Figure 8 | Experiment 3 collision and aggregation scripts | `mu4_difference_decomposition_vs_cue.csv` in Experiment 3 `02_results/` |

The exact eight publication panels are in `paper/figures/`. The paper explains the interpretation and limitations; this file identifies the computational material rather than adding research claims.
