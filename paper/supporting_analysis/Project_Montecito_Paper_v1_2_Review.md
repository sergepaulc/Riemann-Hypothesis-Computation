# Peer Review — Project Montecito Paper, Draft 1.2

**Manuscript:** *A Computational Walk from Pair Correlation to Higher-Order Spectral Statistics of Zeta Zeros* (Draft 1.2, 11 September 2026)
**Scope of review:** mathematics (every derivation and identity), numerical consistency (every figure cross-checked), claim-to-evidence match, citation accuracy, the Experiment 1 / Experiment 3 compatibility question, and arXiv-readiness.
**Method:** every stated identity was re-derived by hand; every z-scale, tail, ratio, and difference was recomputed from the tables; the finite-CUE μ₂ benchmark was compared with a numerical evaluation of the truncated-sine expectation for the paper's exact 512/128 window geometry.

---

## Overall verdict

The manuscript is mathematically sound and numerically self-consistent. Every derivation checks: Proposition 2.1, the full collision decomposition (Proposition 2.2 with the Appendix A.3 definitions — verified by exhaustive enumeration of all closed four-walks), the flat-window Fourier identity of §2.4, the erf integral of A.1, the positive-inertia bound of A.2, the thinning identity of §5.4, the extremal-distribution moments of §2.3, and the sine-process value μ₂ = 4/3. Every quoted z-scale is within bootstrap noise of 4Δ/σ from the tables, every quoted tail matches its z-value, every decomposition row sums, and every citation key resolves to a reference entry.

The paper's claim discipline is exemplary and its "establishes / does not establish" lists match the evidence. **It is close to submission-ready.** There are, however, two findings a referee will raise that go to the paper's one headline empirical statement — that the 10¹² sample is "marginally high" — and both are resolvable with data the project already has. These are Tier 1. Everything else is polish.

---

## Tier 1 — Resolve before submission

### 1. The finite-CUE μ₂ benchmark is quantitatively unexplained, and the Z₁₂ "marginally high" reading is sensitive to it at exactly that level.

§6.3 states that the finite-CUE moments lie below the sine targets "as expected under finite core-plus-halo geometry." I tested this. For the paper's exact geometry (512-point window, core at indices 192–319, unit-density sine process, linear sinc differences), the truncated-sine expectation of the core-anchored μ₂ is

    μ₂(truncated sine) = 1.33293   (4/3 − 0.00041)

i.e. window truncation accounts for **0.0004** of the gap below 4/3. The observed finite-CUE mean is **1.32631**, which is **0.0066 below** that expectation — **2.4 standard errors** of the 64-window CUE mean (SE = 0.0222/8 = 0.0028). The finite-N Dirichlet-kernel correction to the CUE₅₁₂ pair correlation goes the *wrong* way (it slightly *raises* μ₂), so it cannot explain the shortfall either. The stated justification therefore covers about 6% of the effect.

Why this matters: every zeta z-scale in §6.4 is measured against this benchmark. Z₁₂'s μ₂ = 1.33700 is +0.0107 above the observed CUE mean (+1.94 mean-scale SD, the "marginally high" headline). Against the analytically expected benchmark it would be +0.0041, about **+0.7 SD** — no longer marginal. The same question applies to raw μ₄ and μ₄^(>2), where I cannot compute the sine expectation by hand. So the paper's one empirical refinement over Experiment 1 currently rests on a benchmark whose value is 2.4 SE from where theory puts it, with no stated reason.

This may be a 2.4σ fluctuation (p ≈ 0.02 — unlucky but possible) or a systematic issue (e.g. the CUE eigenphases unfolded to a mean spacing slightly different from 1, an off-by-one in the circumference normalization, or a CMV-construction subtlety). The paper cannot tell the reader which, and neither can I.

**Recommended action (no new data required):** use the paper's own Experiment 2 bridge machinery. μ₂ is a pair statistic, so it can be reconstructed from the Experiment 1 histograms:

    μ₂^hist = 1 + 2 ρ̂² Σ_k R̂₂,k ∫_{bin k} (L−u) sinc²(u) du

for each of Z₀, Z₁₂, Z₂₁ **and for the sine curve** over the same finite geometry. This gives a benchmark-independent statement of where each zeta sample's pair-level μ₂ sits relative to the sine process, and it tells you immediately whether the CUE ensemble is low by fluctuation or by construction. Then either (a) explain the CUE shortfall and keep the wording, or (b) soften "as expected under finite core-plus-halo geometry," report the CUE-mean uncertainty, and restate the Z₁₂ result accordingly. Either outcome strengthens the paper; leaving it as is invites a ten-minute referee calculation.

### 2. The Experiment 1 / Experiment 3 compatibility question — the specific objection §6.4 does not yet answer.

§6.4 says the refinement "does not contradict Experiment 1" because "the experiments use different observables and different finite calibrations." True, but a referee will point to something sharper: **for Z₁₂, the two pair statistics disagree in sign.**

- Experiment 1: D₀.₅(Z₁₂) = +0.0176 — *fewer* close pairs than the sine curve (a slightly *wider* hole), 0.7 SD.
- Experiment 3: μ₂(Z₁₂) *above* finite CUE by 1.94 mean-SD — *more* sinc²-weighted pair mass (a slightly *narrower* effective hole).

For Z₀ and Z₂₁ the two experiments agree in direction (Z₀: deficit and low μ₂; Z₂₁: excess and slightly high μ₂). Only Z₁₂ flips. The ordering of the two high samples also flips: in Experiment 1, Z₂₁ is the more deviant (−1.5 SD) and Z₁₂ the less (0.7 SD); in Experiment 3 it is reversed.

There are two legitimate resolutions, and the paper should name whichever the data support:

(i) **Benchmark.** If the finite-CUE μ₂ is anomalously low (Tier 1, item 1), Z₁₂'s "high" reading is partly a benchmark artifact and the sign tension largely dissolves.

(ii) **u-weighting.** D₀.₅ counts only u < 0.5; μ₂ weights all separations by sinc²(u). A deficit below 0.5 with a compensating excess in 0.5 ≲ u ≲ 1 — exactly the redistribution the paper documents for Z₀ ("compensating excess near u ≃ 0.75") — can produce opposite signs. Note, though, that sinc²(0.75) ≈ 0.09 versus sinc²(0.25) ≈ 0.81, so the excess would have to be large relative to the deficit.

The histogram reconstruction in item 1 settles this: it yields μ₂(Z₁₂) directly from R̂₂ and shows whether the sinc-weighted pair mass genuinely exceeds the sine value. I would add one short paragraph to §6.4 stating the sign analysis, the reconstruction result, and the resolution. Also worth stating the calibration asymmetry precisely: Experiment 1 calibrates against 200 *full 10,000-point* replicates (already a sample-level scale), whereas Experiment 3's mean scale is a mean over 16 windows of 128 core points (2,048 core points) — the two "mean scales" are not equivalent.

---

## Tier 2 — Should fix

### 3. The mean-scale z ignores the sampling uncertainty of the CUE reference mean.

A.4 defines z_mean = (X̄ − Ȳ)/sd(Ȳ*₁₆). The denominator captures the variability of a 16-window mean but treats the 64-window CUE mean Ȳ as exact. Its standard error is s/8, half the bootstrap scale. The proper two-sample denominator is s·√(1/16 + 1/64), which deflates every z_mean by 1/√(1 + 16/64) = **0.894**:

| | paper | corrected |
|---|---:|---:|
| Z₀ μ₂ | −5.39 | −4.82 |
| Z₀ raw μ₄ | −5.62 | −5.03 |
| Z₀ μ₄^(>2) | −4.72 | −4.22 |
| Z₁₂ μ₂ | +1.94 | +1.74 |
| Z₁₂ raw μ₄ | +1.77 | +1.58 |
| Z₁₂ μ₄^(>2) | +1.07 | +0.96 |
| Z₂₁ μ₂ | +0.92 | +0.82 |

No conclusion changes, but a statistics-minded referee will raise it, and the fix is one line in A.4 plus updated tables.

### 4. The "0.042085%" in §5.2 is mislabeled.

It is the relative discrepancy in ‖C‖²_F (equivalently in 1 + D_C), not in D_C: (0.920974609 − 0.920166507)/1.920166507 = 0.042085%, whereas the same difference relative to D_C is 0.088%. A reader who checks the arithmetic from the two displayed D_C values will conclude there is an error. Draft 1.1 said "relative Frobenius discrepancy"; restore that wording.

### 5. §2.4: L is never defined.

The flat-window identity is correct (I verified (1/L)φ̂²(Δ) = sin(LΔ/2)/(LΔ/2) and the substitution x = (L/2π)γ giving sinc_π), but L appears from nowhere. State L = log(T/2π) — the local mean-density scale — so the "local unfolding x = (L/2π)γ" is visibly the first-order form of x = N̄(γ), and label the identification with the Weil-form architecture as heuristic (the paragraph already hedges; make it explicit).

### 6. The CUE control geometry should be stated precisely.

The CUE matrix dimension is never given, nor whether linear or circular unfolded differences are used. If N = 512, the "window" is the full spectrum on a circle while zeta windows are truncated line segments — and "identical geometry" (§6.1) is only true if linear differences are used, in which case the far-apart-on-the-line endpoints are adjacent on the circle. It happens that this makes the effective truncation match, but the reader cannot verify the claim without N and the difference convention. Same for the "fixed-count circular Poisson" control. One sentence fixes it.

### 7. Attribution of the extremal spectral distribution (§2.3).

The three-atom distribution (0, 1, 2 at weights 1/6, 2/3, 1/6) is exactly the Alpöge–Furman extremal case — it yields 2/3 simple-on-line and 5/6 distinct, which is a nice thing to say. But check whether A–F *present* it as a distribution; if not, "implicit in" or "corresponding to the extremal configuration of" is safer than "described by."

### 8. Provenance and AI-assistance disclosure.

Two related points. (a) The introduction says "Alpöge and Furman obtain unconditional lower bounds…"; the arXiv comments field for that paper states the proof was discovered autonomously by an AI system and verified and communicated by the listed authors, and Lamzouri's abstract says the same. One clause acknowledging this keeps the attribution accurate; Draft 1.1's reference entry carried it and 1.2 dropped it. (b) Given the subject and the paper's integrity ethos, an explicit statement of AI tools used in *this* project (scripting, drafting assistance) is prudent and increasingly expected. A short "Use of AI tools" note alongside Acknowledgments would preempt any question.

### 9. Acknowledgments and the "independent reviewer."

§3.3 and B.3 lean heavily on an independent reviewer who verified checksums, audited code, deleted and reran the pipeline. That person is never identified or thanked, and "independent" is not defined (of the author? of the tooling?). Add an Acknowledgments section that names or thanks them (or states they are anonymous by request) and says what "independent" means.

---

## Tier 3 — Minor

10. **S₃₀ for Z₀ is quoted two ways:** −0.507157 (§4.2) and −0.507158 (§4.3 table). Same quantity; use one value.
11. **D_C(Z₂₁) difference:** 0.951435 − 0.952040560 = −0.000606, paper says −0.000605. A rounding of an unrounded input; harmless, but give D_C to enough places that the displayed difference reproduces.
12. **PRZZ2020 reference:** "Res. Math. Sci. **7** (2020), no. 2" reads as issue 2; it is Paper No. 2 in vol. 7. Write "Paper No. 2."
13. **OdlyzkoTables:** add the URL and an access date (Draft 1.1 had the URL; 1.2 dropped it).
14. **Homometric μ₃ agreement:** homometry forces μ₂ equality (additive pair functional) but does *not* force μ₃ equality (a triangle statistic); the ten-digit agreement is a property of this particular pair. The paper states it correctly as an observation, but a one-clause note would preempt "isn't μ₃ pair-determined too?" and it is a genuine curiosity worth flagging.
15. **"First Hermitian Instrument"** as a capitalized proper noun (six occurrences) reads oddly in a journal register; consider lowercase.
16. **Figures:** five placeholders, no files. All must be produced; Figure 4 should show both uncertainty scales. Figure 3's caption promises kernel-width sensitivity, but the kernel-width table from Draft 1.1 (σ = 0.5, 1, 2) is no longer in the text — either restore the table or narrow the caption.
17. **Two unverified context constants** carried from earlier reviews: the ≈0.682 bandwidth-one ceiling and R(ψ₀) = 4/3 — confirm both against the A–F text.
18. **Abstract:** 1,774 characters including markup — under arXiv's 1,920-character cap. Fine as is; do not lengthen.
19. **arXiv category:** this version is a computational-research paper with a methodological claim, not an expository survey; primary **math.NT** (cross-list math.PR or math-ph) fits better than math.HO. First-time submission to math.NT requires endorsement — arrange it now.
20. **MSC:** 11M26, 11Y35, 15B52, 60G55 are reasonable; 15A18 (eigenvalues) is a plausible addition.

---

## What I verified as correct (for the record)

- Proposition 2.1: tr H_λ = m(1−λ); ‖H_λ‖²_F = m[(1−2λ) + λ²(1+D_C)]; b_pos closed form — all re-derived.
- Proposition 2.2 / A.3: exhaustive enumeration of closed four-walks from a core vertex. Per vertex pair {a,b}: 8 triangle walks (→ coefficient 4 on the ordered sum T₃), 2 walks of type K²_ia K²_ib (→ W⁽⁰⁾), 2 of type K²_ia K²_ab (→ W⁽¹⁾); two-index class gives 6S₂ + S₄; class sizes 1 + 7(n−1) + 6(n−1)(n−2) + (n−1)(n−2)(n−3) = n³. The "four placements of the repeated vertex" explanation is correct.
- §2.3 extremal moments 1, 4/3, 2, 10/3 from atoms 0,1,2 at 1/6, 2/3, 1/6; 10/3 − 13/4 = 1/12.
- §2.4 flat-window Fourier identity and the substitution to sinc_π.
- Sine-process μ₂ = 1 + ∫sinc² − ∫sinc⁴ = 1 + 1 − 2/3 = 4/3 (numerically confirmed).
- §5.4 thinning identity Σ²_thin(L) = p²Σ²_orig(L/p) + (1−p)L, from binomial thinning.
- A.1 erf integral; A.2 positive-inertia bound.
- The homometric pair {0,1,2,6,8,11} / {0,1,6,7,9,11}: identical difference multiset {1,1,2,2,3,4,5,5,6,6,7,8,9,10,11}.
- All z-scales (within bootstrap noise of 4Δ/σ), all tails (match their z), all decomposition row sums, 72%/80%, the 8.97 ratio, 176 = 48 + 128 rows, D_C height table, inertia table, and every frozen Experiment 1/2 number against the earlier drafts.
- Citation keys: every key cited is listed and every entry listed is cited.

---

## Suggested order of work

1. Run the histogram reconstruction of μ₂ for Z₀, Z₁₂, Z₂₁ and the sine curve (Tier 1.1). This one computation resolves items 1 and 2 together and determines the final wording of the Z₁₂ result.
2. Add the CUE-mean uncertainty to the z-scale (item 3) and regenerate the §6.4 table.
3. Fix the labeling, definitions, and geometry statements (items 4–6).
4. Add Acknowledgments and the AI-use / provenance notes (items 8–9).
5. Produce figures, finalize references, arrange endorsement.
