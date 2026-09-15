# Review — Experiment 1 (pair correlation from 10,000 zeta zeros)

Reviewer pass over `experiment_1_results/`. Everything below was recomputed
independently from the two exported CSVs; nothing is taken from the report.

**Verdict: the experiment is sound, fully reproducible, and passes all four v0.4
success criteria. One substantive correction is needed — the report's central
qualitative claim about short-range agreement with GUE is contradicted by its own
data, at high significance.**

---

## 1. Reproduction audit

Recomputed from `zeta_unfolded_points.csv` alone, using the estimator exactly as
specified in §4 of the report:


| quantity                  | report      | recomputed  | agreement            |
| ------------------------- | ----------- | ----------- | -------------------- |
| pairs with `0 < d ≤ 30`   | 294,472     | 294,472     | exact                |
| per-bin counts (300 bins) | —           | —           | max diff **0**       |
| `R̂₂` per bin             | —           | —           | max diff **2.2e-16** |
| `gue_theory` column       | —           | `1 − sinc²` | max diff 1.7e-16     |
| RMSE vs GUE, `0<u<5`      | 0.036858    | 0.036858    | exact                |
| MAE vs GUE, `0<u<5`       | 0.029108    | 0.029108    | exact                |
| Pearson, `0<u<5`          | 0.990774    | 0.990774    | exact                |
| mean over `10<u<30`       | 0.999607    | 0.999607    | exact                |
| mean NN spacing           | 1.000023001 | 1.000023001 | exact                |
| density                   | 1.000077007 | 1.000077007 | exact                |


Every published number regenerates bit-for-bit from the artifacts. This is a
strong reproducibility result and satisfies criterion 4 outright.

*Documentation nit:* the two normalisation figures are different statistics —
`1.000023001 = L/(N−1)` (mean spacing) and `1.000077007 = N/L` (density). They
are mutually consistent (`N/L = (N/(N−1))·(N−1)/L`), but the report presents them
as if they were the same check twice. State the definitions.

## 2. Data provenance — independently verified

The report substitutes a regenerated table for Odlyzko's file and documents the
substitution rather than hiding it. That is the right call. I verified the
substitution is harmless:

- `mpmath.zetazero` at 30 dps on **10 indices** spanning the range
(n = 1, 2, 10, 100, 1000, 2500, 5000, 7500, 9999, 10000): max deviation
**1.8e-12** (relative ≈ 2e-16, i.e. float64 round-off).
- Hardy `Z(γ)` evaluated at sampled ordinates: max `|Z|` = **1.6e-11**. These are
genuinely zeros, not near-misses.
- Index contiguous 1…10000, `γ` and `x` strictly increasing, no NaN.

**Completeness check (not in the report, and the one that matters most).** A
skipped zero cannot be detected by spot-checking individual values — it shows up
as a permanent unit shift in the counting offset. Writing
`S̃(n) = n − ½ − x_n`, a missing zero forces `S̃` to step by 1 and never return.
Measured: `S̃ ∈ [−0.853, +0.949]`, mean **0.0000**, std **0.2888**, with no
drift. For comparison, `S(t)` has variance `≈ (1/2π²)·log log(t/2π)`, giving
`≈ 0.31` at these heights. **No zeros are missing, and the fluctuation is the
right size.** Worth adding to Appendix A — it is a stronger provenance argument
than the spot checks.

## 3. The estimator is mathematically correct

For a stationary process of intensity `ρ` and pair correlation `g`, the second
factorial moment measure gives, for a window `W = [0,L]` and bin `B_k`,

```
E[C_k] = ρ² ∫_{B_k} g(v) · |W ∩ (W − v)| dv = ρ² ∫_{B_k} g(v)(L − v) dv
       ≈ ρ² g(u_k)(L − u_k) Δu ,
```

since the set-covariance of an interval is `|W ∩ (W−v)| = L − |v|`. Inverting
gives exactly the report's

```
R̂₂(u_k) = C_k / [ ρ̂² (L − u_k) Δu ] ,   ρ̂² = N(N−1)/L² .
```

So the `(L − u_k)` factor is the exact translation edge correction, not an
approximation, and `N(N−1)/L²` is the natural plug-in for the *factorial* moment
(it removes the self-pair). **The estimator is right.** Two second-order caveats:

- **Bin-centre vs bin-average.** `E[C_k]` involves the average of `g` over the
bin; the report compares against `g` at the bin centre. Where `g` is convex
this biases the expected value low. Material only in the first bin:
at `u = 0.05` the bin average of the GUE curve is **+32.7%** above the centre
value (0.01088 vs 0.00820); by `u = 0.25` it is +0.8%. Fix by integrating the
GUE curve over each bin. This makes the deficit in §5 slightly *larger*.
- **Window endpoints are data points.** `L = x_N − x_1` conditions on both
endpoints being points, biasing `ρ̂` marginally high. `O(1/N) ≈ 0.01%`.
Negligible, worth one sentence.



## 4. Two checks the report should add

**(a) The sum rule.** For any determinantal process with the sine kernel,

```
∫₀^∞ (R₂(u) − 1) du = −½ ,
```

exactly — a parameter-free consequence of the "correlation hole" containing
exactly one missing point. Measured on the data: **−0.5072**, against **−0.4983**
for the GUE curve integrated over the same `0<u<30` window. This tests
normalisation and rigidity simultaneously, with nothing fitted, and it passes.
It is a far better headline check than "mean over `10<u<30` ≈ 1".

**(b) A synthetic control through the identical pipeline.** Running the report's
own estimator on point processes with known answers, at matched sample size:


| input                              | pairs `u<0.5` | GUE-expected | deviation  | z         |
| ---------------------------------- | ------------- | ------------ | ---------- | --------- |
| synthetic GUE (3 reps, 10,400 pts) | 3,526         | 3,531        | −0.1%      | **−0.09** |
| synthetic CUE (3 reps, 10,000 pts) | 3,435         | 3,395        | +1.2%      | **+0.69** |
| Poisson (10,000 pts)               | 4,999         | 1,131        | +342%      | +115      |
| **zeta (the experiment)**          | **878**       | **1,131**    | **−22.4%** | **−7.5**  |


The estimator recovers the sine-kernel answer to well within noise, and correctly
identifies Poisson. **So the zeta deviation in §5 is a property of the data, not
of the method.** This control is cheap and settles the question; it belongs in the
paper.

## 5. The principal finding — the report understates its own result

Report §6 and §9 say the empirical curve *"closely tracks the predicted GUE shape
at short range"* and grade criterion 2 a plain PASS. **The data say otherwise.**
Scoring bin counts against the bin-averaged GUE expectation:


| u    | observed | GUE-expected | ratio | z         |
| ---- | -------- | ------------ | ----- | --------- |
| 0.05 | 5        | 10.9         | 0.46  | −1.78     |
| 0.15 | 37       | 74.1         | 0.50  | **−4.31** |
| 0.25 | 121      | 190.9        | 0.63  | **−5.06** |
| 0.35 | 282      | 344.0        | 0.82  | **−3.34** |
| 0.45 | 433      | 511.5        | 0.85  | **−3.47** |
| 0.55 | 642      | 672.1        | 0.96  | −1.16     |
| 0.65 | 805      | 808.0        | 1.00  | −0.11     |
| 0.75 | 1,032    | 908.2        | 1.14  | **+4.11** |


`χ²` over `0<u<1` on 10 bins = **91.8** (mean `z²` = 9.2, expected 1).

The structure is not random scatter: a **coherent deficit across** `0.1 ≲ u ≲ 0.5`
**followed by a compensating excess at** `u ≈ 0.75`. Total pairs with `u<1` are only
1.6% low (1.2σ) — the *mass* is right, the *shape* is shifted. The empirical
correlation hole is wider than GUE's and its first peak is displaced to larger `u`
and overshoots. This is plainly visible in `pair_correlation_u_0_5.png`: the blue
curve lies to the right of the orange one through the entire rise.

**The report's own exported error bars already show this.** Comparing
`gue_theory` against the exported `block_ci95_*` columns: the 95% band **excludes**
the GUE value in 5 of the 10 bins with `u<1`, including `u = 0.25` at 6.9 block-SEs.
The evidence was in the CSV; it was not compared against the theory column.

**Uncertainty calibration.** The quoted per-bin SEs are optimistic. In the flat
region `u>5`, where residuals should be pure noise, the observed scatter of
`R̂ − R_GUE` is **0.0489** against a mean quoted `block_se` of **0.0330** — an
inflation factor of **1.48** (and 21% of bins exceed ±1.96 SE against a nominal
5%). The `block_se` happens to track naive counting noise closely (median ratio
1.01 over `u>1`), so both underestimate the true scatter; pair counts in a bin are
not Poisson, and neighbouring bins are correlated. Rescaling by 1.48, the
short-range deviations remain significant: `z = −3.2, −4.7, −2.7, −2.3, +2.5` at
`u = 0.15, 0.25, 0.35, 0.45, 0.75`. **The conclusion survives an honest error
budget** — and the synthetic controls in §4(b) confirm it independently.

## 6. What the deviation most likely is — and what was *not* established

The natural reading is finite height. Montgomery's limit is `T → ∞`, and the
approach is governed by corrections of relative order `1/L`, `L = log(γ/2π)`.
Across this sample `L` runs from **0.81** (at `γ₁ = 14.13`) to **7.36** (at
`γ₁₀₀₀₀ = 9877.78`), so `1/L ≈ 0.14–0.18` over the bulk — the asymptotic regime is
simply not reached. Odlyzko's well-known close agreement with GUE is at heights
many orders of magnitude above this sample.

I tested the scaling by quartile of height:


| quartile | γ range       | median `L` | deficit (`u<0.5`) |
| -------- | ------------- | ---------- | ----------------- |
| Q1       | 14 – 3,031    | 5.60       | 27.5%             |
| Q2       | 3,033 – 5,448 | 6.52       | 20.8%             |
| Q3       | 5,449 – 7,708 | 6.96       | 24.0%             |
| Q4       | 7,709 – 9,878 | 7.25       | 17.3%             |


The trend has the right sign (`corr(1/L, deficit) = 0.82`), **but it is not
statistically resolved.** Each quartile carries ≈ ±5% counting error, so Q1 vs Q4
is 10.2 ± 7.4, only **1.4σ**. A least-squares fit of `deficit = a/L + b` over an
`L`-range of just 5.6–7.2 cannot constrain the intercept, and I would not quote
one. **Honest statement: the deviation is real and robust; its attribution to
finite height is plausible and directionally supported, but not demonstrated by
this dataset.**

The decisive move is to stop comparing finite-height data against the `T → ∞`
limit. Either:

1. compare against an explicit finite-`T` prediction (Bogomolny–Keating /
  Berry–Keating give the arithmetic corrections to the form factor), or
2. get a real lever arm on `L` by using Odlyzko's published high-height tables
  (zeros near the `10^12`-th and `10^21`-st), where `L` roughly doubles or
   triples and the correction should visibly shrink.

Option 2 is mostly an ingestion job and would turn a 1.4σ hint into a real
measurement.

## 7. Possible corrections to make in the report

1. **§6/§9 criterion 2.** Replace "closely tracks the predicted GUE shape at short
  range" with the quantified statement: qualitative GUE shape is reproduced, with
   a systematic and highly significant short-range excess repulsion. Criterion 2
   still passes as written in v0.4 ("expected short-range suppression and
   *qualitative* agreement") — but the deviation is a finding, not noise, and
   burying it costs the paper its most interesting number.
2. **§7.** State that the block band is descriptive *and* measurably ~1.5× too
  tight in the flat region; do not use it for per-bin inference.
3. **§4.** Compare against the bin-*averaged* GUE curve, not the centre value.
4. **§3.** Distinguish `L/(N−1)` from `N/L`; add the `S̃` completeness check.
5. **§6.** Add the sum-rule check (−0.5072 vs −½) and the synthetic-GUE control.
6. **§2.** The provenance gate the report flags is real but low-risk: the
  ordinates are correct to 1.8e-12 against independent computation, so the
   Odlyzko rerun is a documentation formality, not a numerical one. Say so.



## 8. Fitness for Experiment 2

Both required artifacts are present, correct, and reproducible. `X_ζ` is a clean
unit-density configuration with verified completeness. One consequence worth
carrying forward: since the zeta point process is measurably *more rigid* than
GUE at short range in this sample, the Experiment 3 zeta-vs-GUE comparison
already has a known level-1 discrepancy. That is useful rather than awkward — it
means the two-level test has something real to resolve, but it must be
**measured and reported at level 1 first**, or a level-2 inertia difference will
be misread as sensitivity beyond pair correlation when it is just the level-1
difference propagating through.