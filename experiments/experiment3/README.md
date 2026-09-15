
# Experiment 3 — bounded sinc-kernel moment study

The paper calls this completed study **Experiment 3**. The internal archival
label is **Experiment 3BS (Bounded Study)**.

The corrected v1.1 release is self-contained and includes the pre-result
protocol, three frozen zeta inputs, CUE/Poisson/exact controls, execution code,
aggregation code, tests, validators, results, figures, reports, peer review, and
checksums.

## Full clean reproduction

```bash
make reproduce-exp3
```

The original corrected release remains unchanged under `frozen_release/`. The
top-level runner reproduces it inside `build/experiment3/`.
