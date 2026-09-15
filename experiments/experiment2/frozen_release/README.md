# Project Montecito — Experiment 2 — Version 1

## Status

- **Specification:** Project Montecito v0.6
- **Experiment 2 scientific status:** COMPLETE
- **Independent reproducibility checks:** 19 / 19 PASS
- **Experiment 3 computational readiness:** READY
- **Experiment 3 execution:** NOT STARTED

Experiment 2 implements the frozen toy Hermitian apparatus

\[
C_{ij}=\exp\!\left[-\frac{(x_i-x_j)^2}{2}\right],
\qquad
H_\lambda=I-\lambda C,
\]

on the frozen Experiment-1 zeta point configurations. The primary input is the unfolded first 10,000 zeros; the near-\(10^{12}\) and near-\(10^{21}\) samples are secondary controls only.

## Main findings

1. **The Experiment 1 -> Experiment 2 pair-correlation bridge works quantitatively.** For the full primary 10,000-point sample, the direct normalized off-diagonal Gram energy is \(D_C=0.9201665\), while the prediction from the frozen empirical pair-correlation curve is \(0.9209746\). The relative Frobenius discrepancy is about **0.0421%**.
2. **The finite-height effect propagates into a second weighted two-point observable.** The direct \(D_C\) moves from 0.920167 at low height to 0.945814 near zero number \(10^{12}\) and 0.951435 near \(10^{21}\). The asymptotic GUE Gaussian-weighted benchmark is 0.952041.
3. **The toy family has a stable nontrivial inertia profile.** For primary \(m=512\) blocks, negative directions first appear on the frozen grid at \(\lambda=0.35\). Mean positive fractions are approximately 0.777 at \(\lambda=0.50\), 0.653 at \(\lambda=0.75\), and 0.597 at \(\lambda=0.95\).
4. **The generic trace/Frobenius positive-inertia lower bound is valid but becomes very loose.** At \(m=512\), it falls from about 0.521 at \(\lambda=0.50\) to about 0.003 at \(\lambda=0.95\), while the measured positive fraction remains near 0.60.
5. **Numerical sign resolution is unambiguous on the frozen grid.** No unresolved eigenvalue assignments occurred; the closest grid eigenvalue to zero was approximately \(2.516\times10^{-6}\), about \(1.49\times10^4\) screening thresholds away from zero.

These are computational results for the toy model. They do not validate the Alpöge-Furman theorem, do not identify the toy matrix with Weil's Hermitian form, and do not constitute evidence for the Riemann Hypothesis.

## Where to start

- `04_report/Project_Montecito_Experiment2_Report_v1.pdf` — typeset final report
- `04_report/Project_Montecito_Experiment2_Report_v1.docx` — editable typeset report
- `04_report/Experiment2_Report_v1.md` — source report
- `04_report/Experiment2_Execution_Log_v1.md` — chronological execution record
- `00_preregistration/experiment2_config_v1_frozen.json` — frozen parameters and input hashes
- `00_preregistration/block_manifest_v1.csv` — exact nested block geometry
- `02_results/` — machine-readable numerical outputs
- `03_figures/` — final figures
- `src/experiment2_run.py` — primary computation
- `src/verify_experiment2.py` — independent verification checks
- `05_reproducibility/verification_summary.json` — verification status
- `05_reproducibility/Experiment2_Artifact_Manifest_v1.csv` — artifact sizes and hashes
- `05_reproducibility/SHA256SUMS_Experiment2_v1.json` — SHA-256 map
