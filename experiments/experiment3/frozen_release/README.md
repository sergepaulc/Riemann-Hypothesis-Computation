# Project Montecito — Experiment 3BS Corrected Release v1.1

**Experiment 3BS** is the internal name of the bounded study presented as **Experiment 3** in the paper.

This release incorporates the independent peer review of the original bounded cloud package. It corrects package reproducibility and statistical presentation while preserving every scientific result and the immutable v1 protocol.

## Read first

1. `00_protocol/Experiment3BS_Release_v1_1_Change_Record.md`
2. `04_report/Experiment3BS_Corrected_Release_Report_v1.1.md`
3. `04_report/Experiment3BS_Peer_Review_Response_v1.md`
4. `04_report/Experiment3BS_Closure_Decision_v1.1.md`
5. `06_paper/Project_Montecito_Paper_Simple_Draft_v0.3.2.md`
6. `07_peer_review/16-experiment3-bounded-study-review.md`

## Reproduce from a clean copy

The original bounded protocol remains the seed authority. From the package root:

```bash
export PYTHONPATH=01_code
export OPENBLAS_NUM_THREADS=2
export OMP_NUM_THREADS=2

python 01_code/run_experiment3bs_v1_1.py
python 01_code/make_paper_figures_v1.py
python 01_code/validate_collision_decomposition_v1_1.py
python 01_code/validate_moments_v1_1.py
pytest -q 01_code/tests/test_experiment3bs_v1_1.py
```

The main runner now regenerates:

- `02_results/all_window_endpoints.csv`
- `02_results/group_summary.csv`
- `02_results/mu4_difference_decomposition_vs_cue.csv`
- `02_results/uncertainty_scale_comparison.csv`
- all machine-readable summary and control JSON files

The figure script uses only regenerated result files. The complete unit-test source and independent brute-force collision validator are included.

## Principal validation records

- `04_report/independent_collision_validation_v1_1.json`
- `04_report/independent_moment_validation_v1_1.json`
- `04_report/Experiment3BS_v1_to_v1_1_Scientific_Equivalence_Check.json`
- `02_results/derived_table_validation.json`
- `04_report/unit_test_log_v1_1.txt`

## Claim boundary

This release reports a finite exploratory study. It does not complete the deferred full Experiment 3, establish a residual beyond the complete two-point law, access D3, validate a 2026 zeta-zero proof, or make a claim for or against the Riemann Hypothesis.
