# Review — Experiment 2 (indefinite Hermitian apparatus) — v2

**Revised 1 Sep 2026** after the Davenport–Heilbronn and Epstein controls. Three
changes from v1, marked **[v2]** below:

1. §5's Experiment-3 readiness verdict is **superseded** — Experiment 3's question
   has since been answered by a stronger experiment, so the readiness question is
   moot (new §10).
2. §6's inference that the apparatus sees only pair correlation is now a
   **demonstrated fact against two RH-false functions**, not an inference from
   the height controls (new §11).
3. §4's recommendation to promote `mu_max` is **withdrawn** — it is confounded
   (new §12).

Everything else in v1 stands and is unchanged.

Adversarial audit as requested. Everything below was recomputed independently
from the Experiment 1 artifacts and my own θ-unfolding of the raw Odlyzko files;
nothing is taken from the reports.

**Verdict: the computation is correct and reproduces exactly — every number I
could check, to all printed digits. The numerical workmanship is the best of the
three packages so far. But two of the five headline findings are near-tautologies
that the primary report over-claims (the Validation Extension already corrects
one of them, and the two documents disagree), and the `EXPERIMENT3_READY = TRUE`
decision was asserted rather than demonstrated. I ran the missing power
calculation: the decision is justified — and in doing so Experiment 2 turns out
to have already produced the project's first real evidence on its central
question, which neither document notices.**

---

## 1. Reproduction audit

Rebuilt from `zeta_unfolded_points.csv` and `data/high_height_unfolded.npz`.
Block manifest inferred as `np.linspace(0, 9488, 16).round()` with 256- and
128-blocks nested concentrically — every downstream number then matched, which
confirms the manifest is as described and not result-tuned (**Q4**).

| quantity | report | mine | status |
|---|---|---|---|
| `D_C^GUE`, σ = 0.5 / 1 / 2 | 0.241262 / 0.952040560 / 2.634701 | identical | exact |
| full-sample `D_C`, 9 values (3 samples × 3 σ) | see §2, Val.Ext. | identical | exact |
| block-mean `D_C`, m = 128/256/512 | 0.911447 / 0.917196 / 0.918209 | identical | exact |
| `p_pos` at 10 λ values, m = 512 | §8 table | identical | exact |
| location SD at 10 λ values | §8 table | identical | exact |
| `b_pos` at 10 λ values | §8 table | identical | exact |
| mean `μ_max`, 3 samples | 2.857267 / 3.174937 / 3.225853 | identical | exact |
| first crossing `1/μ_max` | 0.350134 / 0.315128 / 0.310351 | identical | exact |

Note the `D_C` reproduction runs through **my own** arbitrary-precision unfolding
of `zeros3.txt`/`zeros4.txt`, so the high-height rows validate the whole chain
from raw Odlyzko text to Gram second moment.

## 2. Mathematical audit (handoff questions 1–5)

**Q1 — the bridge formula.** Re-derived and correct. For a stationary process the
expected ordered-pair count at separation `u` carries the set-covariance factor
`L − u`, matching Experiment 1's convention; `ρ̂² = m(m−1)/L²` is the right
plug-in for the *factorial* moment; the factor 2 converts forward pairs to
ordered pairs. The analytic bin integral is right:

    ∫_a^b (L−u)e^{−u²}du = L∫e^{−u²} − ∫u e^{−u²}
                         = (L√π/2)(erf b − erf a) + ½(e^{−b²} − e^{−a²}) ,

since `∫_a^b u e^{−u²}du = ½(e^{−a²} − e^{−b²})`. The `u > 30` tail bound
`m(m−1)e^{−900}` is correct — `e^{−900} ≈ 1.4e−391`, times `512·511` gives
`3.6e−386`, matching the reported `3.57e−386`.

**Q2 — PSD and the inertia map.** The Gaussian kernel is positive definite by
Bochner (its Fourier transform is a positive Gaussian), so `C ≻ 0` for distinct
points; the reported minimum eigenvalue `9.421e−05 > 0` is consistent.
`η_j(H_λ) = 1 − λ μ_j(C)` is exact, not approximate, since `H_λ` and `C` are
simultaneously diagonalisable. Correct.

**Q3 — the sign-specific bound.** The derivation is correct: `tr H ≤ Σ_{j:α_j>0} α_j`
because negative eigenvalues only lower the trace, then Cauchy–Schwarz and
`Σ α_j² ≤ ‖H‖_F²`. **But the report omits the closed form.** Substituting the
identities `tr H_λ = m(1−λ)` and `‖H_λ‖_F² = m(1−2λ) + λ²‖C‖_F²`, and writing
`c := ‖C‖_F²/m = 1 + D_C`:

\[
b_{\rm pos}(\lambda)=\frac{(1-\lambda)^2}{(1-2\lambda)+\lambda^2 c}.
\]

I verified this reproduces every tabulated `b_pos` exactly. Two consequences the
report should state:

- **`b_pos` is independent of `m`**, and depends on the point process **only
  through the single scalar `c`**. It therefore *cannot* distinguish two
  processes with a common second moment. **Recommendation: drop `b_pos` as a
  discriminating observable in Experiment 3** and keep it only as an algebraic
  sanity check.
- §9's "important limiting result" — that the bound goes vacuous as `λ → 1` — is
  an **algebraic identity, not an empirical finding**. The numerator falls like
  `(1−λ)²` while the denominator tends to `c − 1 > 0`, for *any* configuration.
  It was predictable before any data existed and should be presented as such.

**Q5 — sign resolution.** Sound. At `λ = 0.95`, `‖H‖₂ ≈ λμ_max − 1 ≈ 1.71`, so the
screening scale is `≈1.7e−10`; the closest grid eigenvalue to zero is `2.516e−06`,
a margin of `≈1.5e4`, matching the reported `1.49e4`. No hidden zero assignments.

## 3. Q6 — the bridge is a reconstruction, and the two documents disagree

The Validation Extension states this correctly ("an internal
consistency/reconstruction result… both sides summarize the same underlying pair
differences"). **The primary report does not**: §7 calls it "the strongest direct
validation of the intended Experiment 1 → Experiment 2 bridge" and the executive
summary lists it as finding #1. Those cannot both stand.

The Validation Extension is right, and I can make it quantitative. Both sides are
the same multiset of pair differences; the only difference is binning. So the
agreement should measure **bin width and nothing else**. Two controls confirm it:

| process | direct `D_C` | bridge `D_C` | rel. error |
|---|---:|---:|---:|
| zeta first 10⁴ | 0.920167 | 0.920975 | **0.0421%** |
| CUE | 0.947585 | 0.949046 | 0.0750% |
| **Poisson** | 1.754202 | 1.755422 | **0.0443%** |
| lattice | 0.772556 | 0.694960 | −4.3777% |

and the bin-width scaling on zeta:

| `Δu` | 0.40 | 0.20 | **0.10** | 0.05 |
|---|---:|---:|---:|---:|
| rel. error | 1.00183% | 0.25488% | **0.04209%** | 0.01435% |

**Poisson agrees as well as zeta does (0.0443% vs 0.0421%)**, and the error falls
roughly like `Δu²` — the signature of piecewise-constant quadrature. The 0.04% is
the discretisation error of the frozen histogram, carrying no information about
the zeta zeros.

*One genuine content point in its favour:* the **lattice fails at −4.4%**, because
its `R₂` is a sum of point masses and the piecewise-constant approximation breaks.
So the check does detect a badly non-smooth two-point function. That is what it
validates — smoothness of `R̂₂` at the 0.1 scale and consistency of two code
paths — and that is how it should be described.

**Same issue applies to finding #2.** `D_C = ∫k²(u)R₂(u)du` is a *linear
functional* of `R₂`. So "the finite-height effect propagates into the
Gaussian-weighted second moment" is guaranteed by Experiment 1, not an
independent confirmation. Calling `D_C` "a second, independently weighted
two-point observable" overstates it: it is a smoothing of the observable already
measured. Findings #1 and #2 are the same fact stated twice, both downstream of
Experiment 1.

## 4. Q7, Q8 — sensitivity and spectral tails

**Q7.** The kernel-dependence conclusion is warranted and important, and the
recommendation to freeze `σ` across Experiment 3 is right.

**Q8.** The upper-tail reading is correct. I would add that the report has a
better single-number observable than it realises. The mean `μ_max(C)` orders the
processes cleanly:

    lattice 2.507  <  zeta low 2.857  <  zeta 10¹² 3.175
                   <  zeta 10²¹ 3.226  <  CUE 3.296  <  Poisson 6.865

This is a **rigidity ladder**, and low-height zeta sits *between the lattice and
high-height zeta* — i.e. more rigid than GUE, which is exactly Experiment 1's
central finding, recovered here in one scalar from a completely different
computation. `μ_max` deserves promotion to a reported primary observable; it is
cheaper than the whole `p_pos` curve and it is where the height signal actually
lives.

## 5. Q9 — Experiment 3 readiness: asserted, not demonstrated (but true)

The report sets `COMPUTATIONAL_EXPERIMENT3_READY = TRUE` on the strength of
block-size and location stability. That is necessary but not sufficient: the
question is whether the observable **responds to the point process** strongly
enough to see the comparison Experiment 3 exists to make. Neither document tests
this. I did.

**Dynamic range.** Mean `p_pos` at m = 512, 16 blocks:

| process | λ=0.35 | λ=0.50 | λ=0.70 | λ=0.95 | max \|Δ\| vs zeta, λ≥0.40 |
|---|---:|---:|---:|---:|---:|
| zeta first 10⁴ | 0.9987 | 0.7770 | 0.6697 | 0.5966 | — |
| zeta near 10²¹ | 0.9701 | 0.7812 | 0.6740 | 0.6010 | 0.0062 |
| CUE | 0.9694 | 0.7802 | 0.6736 | 0.6005 | 0.0072 |
| Poisson | 0.8849 | 0.8005 | 0.7266 | 0.6744 | 0.0779 |
| lattice | 1.0000 | 0.7871 | 0.6621 | 0.5801 | 0.0963 |

Full range across processes ≈ 0.10; the zeta-vs-GUE comparison occupies ~6% of it.

**Power calculation** (8 *independent* CUE realisations, 16 blocks each — the
report has only one realisation of each process, so it cannot estimate this):

| λ | CUE mean ± sd | zeta low | z | zeta 10²¹ | z |
|---|---|---:|---:|---:|---:|
| 0.50 | 0.7811 ± 0.0014 | 0.7770 | **−2.93** | 0.7812 | +0.13 |
| 0.70 | 0.6744 ± 0.0012 | 0.6697 | **−4.07** | 0.6740 | −0.37 |
| 0.85 | 0.6263 ± 0.0009 | 0.6232 | **−3.65** | 0.6265 | +0.20 |
| 0.95 | 0.6010 ± 0.0013 | 0.5966 | **−3.47** | 0.6010 | +0.00 |

Effect / noise ≈ **5.2**. **The readiness claim is correct.** But it should rest
on this, not on internal stability, and the between-realisation ensemble should be
part of the Experiment 3 design rather than reconstructed by a reviewer.

## 6. What Experiment 2 already found, without noticing

The height controls in §11.2 are a **natural experiment on the migration rule**,
and both documents read them as a null ("does not produce a large persistent
separation"). They are not a null. Setting the two levels side by side:

| sample | Level 1 (pair correlation) | Level 2 (inertia vs CUE) |
|---|---|---|
| zeta, first 10⁴ | **differs** (`D₀.₅ = 0.224`, z ≈ 9) | **differs** (≈ −3 to −4σ) |
| zeta, near 10²¹ | **matches** GUE | **matches** CUE (≤ 0.4σ) |

**The two levels appear and disappear together.** In no case does Level 1 agree
while Level 2 differs — which is the *only* outcome that would indicate the
apparatus responding to structure beyond pair correlation. This is the first
actual evidence bearing on the project's central question, it comes free with the
height controls already run, and it is consistent with the Level-2 signal being
entirely Level-1 propagating.

That is a genuine (negative) result and belongs in the report. It also raises the
value of the moment-ladder proposal in the v0.5 draft: `p_pos` cannot separate
"Level-1 propagating" from "genuinely higher-order", whereas `μ₂` vs `μ₃` can, by
construction.

## 7. Defects and required changes

1. **No data artifacts shipped — third package running.** The reproducibility map
   lists 13 files; **zero** are present. I could review only because everything
   was regenerable from Experiment 1. `block_matrix_metrics.csv`,
   `C_spectra_and_crossings.csv` and the frozen manifest are the ones that matter.
2. **Specification v0.6 is not in the repository.** The spec folder holds v0.4 and
   my v0.5 proposal. I therefore could not audit pre-registration compliance
   against the document the report claims to follow, only against its own
   internal statements.
3. **Reconcile the two documents on the bridge** (§3 above). The primary report's
   finding #1 and §7 must be brought into line with the Validation Extension.
4. **Restate §9 as algebra** and add the closed form for `b_pos`; drop `b_pos`
   from Experiment 3's discriminating observables.
5. **Block-size sensitivity is comparable to the effect being measured.** The
   report's own §10 gives a largest nested `m=128` vs `m=512` difference of
   **0.007202** at λ = 0.40, while the zeta-vs-CUE effect is **0.0064**. Any
   Experiment 3 comparison must therefore fix `m` exactly and avoid the crossing
   region, or report the two side by side. This is not currently stated.
6. **Promote `μ_max`** to a primary reported observable (§4).

## 8. On Groskin's failure mode

For once it mostly does not apply, and that is worth recording. `C` is computed in
closed form with no quadrature, the omitted tail is bounded at `1e−386`, and sign
margins are `1.5e4×` the screening scale — so the archimedean-tail pathology that
produced Groskin's spurious deep negatives has no analogue here. The apparatus is
numerically clean.

What *does* carry over is item 5: the residual truncation in this experiment is
the **block**, not the kernel, and its effect is the same size as the signal. The
v0.5 draft's change C4 (truncation-sensitivity gate) should be read as applying to
block size, and the report's §10 numbers already satisfy it — they simply need to
be compared against the effect size rather than reported in isolation.

## 9. Bottom line

Freeze Experiment 2 after items 1–6. The numerics are sound and independently
reproduced; what needs work is the framing of two findings, one dropped
observable, and shipping the data. Experiment 3 is genuinely ready, for a better
reason than the one given.

---

# ADDENDUM (v2, 1 Sep 2026)

## 10. [v2] The Experiment-3 readiness verdict is superseded

v1 §5 ran the power calculation the report omitted and concluded
`EXPERIMENT3_READY = TRUE` was justified — effect/noise ≈ 5.2 for the
zeta-vs-GUE comparison. That arithmetic stands, but the conclusion is now moot.

Experiment 3's design was: hold the apparatus fixed, vary the point process. That
experiment has since been run in a stronger form. Instead of GUE, Poisson and
lattice — whose answers were never in doubt, and whose Level-2 rows were computed
in a single call during this review — the apparatus was fed **two functions for
which RH is false**: Davenport–Heilbronn (8.3% of zeros off the critical line)
and an Epstein zeta of class number two (32.3% off the line).

That is the most informative possible process swap, and it returned a verdict.
Running the specified Experiment 3 now would add rows, not information.

## 11. [v2] The central finding, upgraded from inference to demonstration

v1 §6 observed that Level-1 and Level-2 differences appear and disappear together
across height, and inferred that the apparatus was probably seeing nothing beyond
pair correlation. That inference is now a measurement:

| process | off-line zeros | λ=.50 | λ=.70 | λ=.95 | `mu_max` |
|---|---:|---:|---:|---:|---:|
| **Epstein** | **32.3%** | 0.7769 | 0.6934 | 0.6274 | 3.892 |
| **DH** | **8.3%** | 0.7759 | 0.6709 | 0.6006 | 2.886 |
| zeta first 10⁴ | 0% | 0.7793 | 0.6714 | 0.5947 | 2.753 |
| zeta near 10²¹ | 0% | 0.7847 | 0.6772 | 0.6069 | 3.268 |
| CUE | — | 0.7812 | 0.6729 | 0.6021 | 3.181 |

**The apparatus cannot detect RH-failure.** It is blind to DH (differences ≤0.005
for λ≥0.5) and only weakly sensitive to Epstein (≈0.02 at λ≥0.7) — despite a third
of Epstein's zeros lying off the critical line. This is the computational
counterpart of Alpöge–Furman §1.4, where the analytic method's inputs are admitted
to hold verbatim for exactly these functions.

This is the result Experiment 2 produced. It is negative, it is about the
apparatus rather than about zeta, and it is worth having.

## 12. [v2] Withdrawn: `mu_max` is not a rigidity ladder

v1 §4 recommended promoting `mu_max` to a primary observable on the strength of
the ordering lattice < zeta-low < zeta-high < CUE < Poisson, read as a rigidity
ladder. **DH breaks it.**

| process | `mu_max` | `Sigma^2(20)` (rigidity) |
|---|---:|---:|
| lattice | 2.507 | 0.000 |
| zeta first 10⁴ | 2.753 | 0.535 |
| **DH** | **2.886** | **2.352** |
| CUE | 3.181 | 0.774 |
| zeta near 10²¹ | 3.268 | 0.577 |
| Epstein | 3.892 | 6.027 |
| Poisson | 6.390 | 16.277 |

DH has a *lower* `mu_max` than CUE while being three times *less* rigid. The two
orderings disagree precisely for the process that is short-range rigid and
long-range loose.

The explanation is instructive: `mu_max` of a Gaussian-kernel Gram matrix is
driven by short-range clustering, so it tracks the two-point function at
`|u| ≲ 1` and is blind past that. It is short-sighted in exactly the way the rest
of the apparatus is — which is why it inherits the same failure.

**Corrected recommendation:** report `mu_max` as a descriptive spectral statistic
only, never as a proxy for rigidity, and do not promote it.

## 13. [v2] What this does *not* change

The v1 audit is unaffected. Every number still reproduces exactly; the bridge is
still a reconstruction (Poisson agrees to 0.0443% against zeta's 0.0421%, and the
error scales as `Δu²`); `b_pos` is still `(1−λ)²/[(1−2λ)+λ²c]`, block-size
independent and a function of the process only through `c`; the data artifacts are
still missing; specification v0.6 is still not in the repository.

The defects list in v1 §7 stands as written, minus item 6 (`mu_max`), which §12
withdraws.
