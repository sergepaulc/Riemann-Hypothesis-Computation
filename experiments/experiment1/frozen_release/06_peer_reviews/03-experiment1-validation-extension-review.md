# Review — Experiment 1 Validation Extension ("Additions - 1")

Second reviewer pass. Every numerical claim below was re-derived independently:
the unfolding claims analytically and numerically from the raw ordinates, and
the Monte Carlo calibration by writing a separate sampler with a different seed
(400 replicates against their 200).

**Verdict: all four checks are correct and reproduce. Two are stronger than the
report claims, one is weaker than the report claims, and there is one real
process defect (no data artifacts were delivered). The scientific conclusion —
mass conserved, shape anomalous — is sound and is the most valuable result in
the package, though the report ranks it third.**

---

## 1. Independent replication summary

| claim | report | my independent value | status |
|---|---|---|---|
| max unfolding shift | 0.000469298 | 0.000469298 | exact |
| mean unfolding shift | 2.84741e-06 | 2.847408e-06 | exact |
| max Δ(NN spacing) | 0.000153804 | 0.000153803 | exact |
| bins changed by θ-unfolding | 6 of 300 | 6 of 300 | exact |
| max Δ count per bin | 1 | 1 | exact |
| Δ pairs at `u<0.5` | 0 | 0 | exact |
| `D_0.5^ζ` (10-block) | 0.223872 | 0.223876 | ✓ (4e-6, quadrature) |
| `D_0.5^ζ` (single window) | 22.4010% | 0.224010 | exact |
| GUE `D_0.5` mean | 0.001558 | −0.000972 | ✓ 1.2σ apart |
| GUE `D_0.5` sd | 0.024797 | 0.025707 | ✓ 0.6σ apart |
| `z` for zeta | 8.97 | 8.75 | ✓ |
| replicates ≥ zeta | 0/200 | 0/400 | ✓ |
| `S_30^ζ` (10-block) | −0.511017 | −0.511010 | ✓ |
| GUE `S_30` mean ± sd | −0.499315 ± 0.006857 | −0.498186 ± 0.006913 | ✓ |
| `S_30` two-sided tail | 0.129 | 0.122 | ✓ |

My sampler was written from scratch (Dumitriu–Edelman β=2 Hermite tridiagonal,
n=1200, central 1000 retained, moment-matched semicircle unfolding), seed 12345
against their 20260827. The agreement across all ensemble moments is strong
evidence that the calibration is correctly implemented on both sides.

## 2. Check 1 — Odlyzko provenance: accepted, and the gate is trivially closable

Eleven decile anchors within 1.499e-9 of a table quoted to ≈3e-9 is consistent.
Combined with my earlier 10-index `mpmath` check (max 1.8e-12) and the `S̃`
completeness diagnostic, the numerical case is closed.

The report attributes the remaining gap to a sandbox that "can access but cannot
stream bytes into Python." **On the local Mac this is a one-line fix.** Earlier
in this project `curl` with a browser User-Agent retrieved a file that `WebFetch`
refused with HTTP 403; the same approach fetches `zeros1` directly and permits a
SHA-256 lock. I have not downloaded it — that is your call — but the gate should
not be carried into a manuscript as though it were hard.

## 3. Check 2 — unfolding sensitivity: correct, but weaker evidence than presented

The three shift statistics reproduce to every digit. I can also give the closed
form the report omits. From the standard expansions,

    θ(T)/π = T/(2π)·log(T/2π) − T/(2π) − 1/8 + 1/(48πT) + 7/(5760πT³) + …

so with `N̄_θ = 1 + θ(T)/π` and `N̄_asym = T/(2π)log(T/2π) − T/(2π) + 7/8`,

    **N̄_θ(T) − N̄_asym(T) = 1/(48πT) + 7/(5760πT³) + O(T⁻⁵).**

I verified this against the numerics to 4.2e-12. It reproduces the reported
maximum exactly: at `γ₁ = 14.1347`, `1/(48πγ₁) + 7/(5760πγ₁³) = 4.69298e-4`.

**This is why the check had to come out the way it did.** The discrepancy between
the two unfoldings is a smooth, monotone, positive function bounded by `4.7e-4`
— **213× smaller than the 0.1 bin width** — and because it varies slowly it
almost cancels in *differences* `x_j − x_i`, which is all the estimator uses.
Reporting "the deficit changes from 22.4010% to 22.4010%" as a headline finding
overstates it: the outcome was forced before the computation ran.

The check is still worth keeping — it closes an obvious referee question — but it
should be stated as *"as expected from the O(1/T) closed form, and confirmed"*,
not as independent evidence. More importantly, it does **not** test the concern a
sceptic would actually raise, because both candidates are global smooth counting
functions differing negligibly. What is untested is whether unfolding by a
*global* smooth function is appropriate at all when `L = log(γ/2π)` varies from
0.81 to 7.36 across the sample. I do not think it is a real problem — the smooth
counting function is the correct and standard choice, and the alternative
(unfolding by exact `N(T)`) would trivially produce a perfect lattice — but the
report should say that explicitly rather than let the θ-check stand in for it.

## 4. Check 3 — matched GUE calibration: the central result, correctly executed

This is the strongest addition and it replicates cleanly. The design is right:
matched block geometry, predeclared statistic, fixed seed, plus-one tail.

**Statistical framing.** The report is careful — it explicitly disclaims an
analytic p-value — but the "8.97 standard deviations" is still doing rhetorical
work it cannot support. With 600 pooled replicates (their 200 + my 400, zero
exceedances) the defensible statement is

    p < 1/601 = 0.0017   by direct enumeration,

and nothing smaller. A 9σ Gaussian tail is ~10⁻¹⁹; that number is not in
evidence. In the null's favour, I checked its shape: skew −0.053, excess kurtosis
−0.116, Shapiro–Wilk p = 0.51 — **empirically indistinguishable from Gaussian**
over the ±2.5σ range actually sampled. So the extrapolation is not unreasonable,
merely unverified. Report the enumeration bound as the result and the σ-distance
as a descriptive effect size.

This limit is also **self-imposed and cheap to remove**: my 400 replicates took
95 seconds. 100,000 replicates is a few hours and would push the enumerated bound
to ~10⁻⁵. Whether that is worth doing depends on §5.

## 5. The deeper issue — the null being rejected is one nobody holds

`D_0.5` tests `H₀`: *the first 10,000 zeta zeros are distributed as the
**asymptotic** sine-kernel process.* Montgomery's conjecture is a `T → ∞`
statement; at `L ≈ 6.5` no one expects `H₀` to hold. Rejecting it at 9σ therefore
confirms that finite-height corrections exist — which was not in doubt — rather
than measuring them.

The scientifically loaded quantities are the ones the report ranks second and
third:

- **magnitude.** `D = 0.224` against `1/L ≈ 0.154` implies an O(1/L) coefficient
  of order 1.5. Plausible, but uninterpretable without a theoretical prediction.
- **shape.** Mass conserved, distribution shifted. This is the real finding.

**Recommendation: make Finding B the headline.** And note that it yields a
falsifiable constraint the report does not draw out. Writing the finite-height
correction as `δR₂(u) = R₂^ζ(u; T) − R₂^GUE(u)`, the sum-rule result says

    ∫₀^³⁰ δR₂(u) du = S_30^ζ − S_30^GUE = −0.0128 ± 0.0069 ,

i.e. **the correction integrates to zero to within ±0.007.** Any candidate
finite-`T` formula (Bogomolny–Keating / Berry–Keating) must satisfy that. That
converts a descriptive observation into a testable prediction, and it is a much
better use of the matched ensemble than driving the `D_0.5` p-value lower.

## 6. Check 4 — high height: correctly not claimed

The report says plainly that the `10^12`/`10^21` recomputation was not executed
and cites Odlyzko (1987) only for direction. That is the right call and the right
wording. Two notes:

- Odlyzko's 1987 study supports the *direction* but not the *magnitude*; it used
  a different statistic. It cannot calibrate `D_0.5`.
- Per §2, the ingestion obstacle is a sandbox artifact, not a real one. `zeros3`
  alone would raise `L` from ≈6.5 to ≈26.3 (height 2.68e11), a 4× lever arm. That
  single file would likely settle the finite-height hypothesis outright, and it
  is the highest-value remaining item in Experiment 1 by a wide margin.

## 7. Defects to fix

1. **No data artifacts delivered.** §7 lists six CSVs and four figures; the folder
   contains **zero CSVs and two figures**. I could review the claims only because
   I could regenerate them from `zeta_unfolded_points.csv` in the v1 folder. The
   Monte Carlo ensemble in particular (`gue_matched_monte_carlo_200.csv`) is not
   reproducible from what was shipped — a reader cannot check it without
   rewriting the sampler, as I had to. Given that v0.4 §Reproducibility requires
   "all figures generated from source data" and "raw-data preservation", this is
   the most important item in this review to fix.
2. **Two different `D_0.5` values presented without explanation.** §2 gives
   22.4010% and §3 gives 0.223872. Both are correct: the first is single-window
   geometry, the second matched 10-block geometry. I verified both. Say so, or it
   reads as an inconsistency.
3. **`unfolding_pair_correlation_comparison.png` is misleading as drawn.** The
   blue "Riemann–von Mangoldt" curve is completely hidden under the orange
   θ-curve. That *is* the point, but a reader cannot distinguish "coincident" from
   "not plotted". Use a dashed overlay or a thicker underlay, and annotate that
   the curves differ by at most one pair in six of 300 bins.
4. **Zeta blocks are not exchangeable.** The 10 calibration blocks span different
   heights, and the deficit varies across them (27.5% → 17.3% by quartile). The
   pooled `D_0.5` is unaffected, but no block-bootstrap or block-permutation test
   on the zeta side would be valid. Worth one sentence so nobody does it later.
5. Minor: the v2 peer-review response reports a synthetic control at matrix
   dimension **256** (+2.94%, z = +1.00). The n=1200 ensemble in the extension is
   the better control; n=256 has materially larger semicircle-unfolding bias. Cite
   the ensemble, and retire the n=256 number or label it as preliminary.

## 8. On the dispositions in the v2 response

The one recommendation of mine that was declined — rescaling all SEs by 1.48 —
was declined correctly. Replacing per-bin parametric inference with a matched
Monte Carlo ensemble is strictly better than patching the error bars, and it is
what I would have recommended had I thought of it. The remaining dispositions are
accurate, and the v2 report's incorporated numbers (the z-table, the `S̃`
diagnostic, the 1.48 factor, the quartile table) match my originals.

## 9. Fitness for Experiment 2

Unchanged and confirmed. The source artifacts remain valid and should not be
regenerated. The migration rule as written in v2 is correct and now has a
quantitative anchor: the Level-1 discrepancy is `D_0.5 = 0.224 ± 0.026` in GUE
ensemble units, with the total correlation-hole mass conserved to within ±0.007.
Those two numbers are what must be propagated through the fixed toy apparatus
before any Level-2 inertia difference is attributed to structure beyond pair
correlation.
