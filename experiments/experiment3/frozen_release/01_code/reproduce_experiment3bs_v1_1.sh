#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

export PYTHONPATH=01_code
export OPENBLAS_NUM_THREADS="${OPENBLAS_NUM_THREADS:-2}"
export OMP_NUM_THREADS="${OMP_NUM_THREADS:-2}"
export MKL_NUM_THREADS="${MKL_NUM_THREADS:-2}"
export VECLIB_MAXIMUM_THREADS="${VECLIB_MAXIMUM_THREADS:-2}"

if [[ "${1:-}" == "--clean-generated" ]]; then
  rm -f 02_results/* 03_figures/*
fi

python 01_code/run_experiment3bs_v1_1.py \
  > 04_report/execution_log_v1_1.txt \
  2> 04_report/execution_stderr_v1_1.txt
printf '0\n' > 04_report/exit_code_v1_1.txt

python 01_code/make_paper_figures_v1.py \
  > 04_report/figure_generation_log_v1_1.txt \
  2>&1
python 01_code/validate_collision_decomposition_v1_1.py \
  > 04_report/collision_validation_log_v1_1.txt \
  2>&1
python 01_code/validate_moments_v1_1.py \
  > 04_report/moment_validation_log_v1_1.txt \
  2>&1
pytest -q 01_code/tests/test_experiment3bs_v1_1.py \
  > 04_report/unit_test_log_v1_1.txt \
  2>&1
python 01_code/compare_v1_scientific_outputs_v1_1.py \
  > 04_report/scientific_equivalence_log_v1_1.txt \
  2>&1
python 01_code/validate_release_v1_1.py

echo "Experiment 3BS v1.1 reproduction complete."
