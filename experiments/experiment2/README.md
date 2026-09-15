
# Experiment 2 — the First Hermitian Instrument

Experiment 2 applies the frozen Gaussian Gram matrix and shifted Hermitian family

\[
C_{ij}=\exp[-(x_i-x_j)^2/2],\qquad H_\lambda=I-\lambda C
\]

to the three Experiment 1 point configurations.

The computation is valid and independently reproduced. Its controlling final
interpretation is in `final_record/Experiment2_Report_v2.md`: the trace is
data-free, the Frobenius moment and elementary positive-inertia bound are
controlled by one weighted two-point scalar, and the completed inertia
comparisons did not isolate a residual beyond the measured pair evolution.

## Verify the frozen release

```bash
cd frozen_release
python src/verify_experiment2.py
```

## Full clean reproduction

From the repository root:

```bash
make reproduce-exp2
```

The top-level runner copies the frozen release into `build/` before executing it,
so committed results are never overwritten.
