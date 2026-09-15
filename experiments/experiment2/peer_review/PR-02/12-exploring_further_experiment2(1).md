# Exploring Further: why and where Experiment 2 failed

A complete account of the initiatives run to diagnose Experiment 2, the repairs
attempted, and the alternative objects tried in its place. Written so the dead
ends are recoverable, not just the conclusion.

**Summary.** Experiment 2 was executed cleanly — every published number
reproduces to the digit. It failed for a structural reason fixed before any data
existed: three of its four observables are functions of pair correlation *by
construction*. Six repairs were attempted; four were informative, two were
artifacts caught by controls. Two alternative objects (Davenport–Heilbronn, an
Epstein zeta of class number two) were built and measured; they converted the
central finding from an inference into a demonstration, and produced one apparent
discovery that a control then destroyed.

---

# Part I — Diagnosing the failure

## A. Structural analysis of the observables *(a priori, before data)*

The most decisive step, and it required no computation. Writing
`c := ‖C‖²_F/m = 1 + D_C`, and substituting the report's own identities:

| observable | what it can depend on |
|---|---|
| `tr H_λ = m(1−λ)` | **nothing** — independent of the data |
| `‖H_λ‖²_F = m(1−2λ) + λ²‖C‖²_F` | only `D_C = ∫k²(u)R₂(u)du` — **pure two-point** |
| `b_pos(λ) = (1−λ)²/[(1−2λ) + λ²c]` | only the scalar `c` — **pure two-point**, and block-size independent |
| `p_pos(λ) = F_C(1/λ)` | can see beyond, via `tr C^k`, `k ≥ 3` — but weakly and inseparably |

**Verdict: informative, and fatal.** Three of four observables cannot answer the
question the experiment was built to ask. Two corollaries followed immediately:
`b_pos` can never separate two processes sharing a second moment, and §9's
"important limiting result" (the bound going vacuous as `λ → 1`) is an algebraic
identity, true for any configuration, not an empirical finding.

Also derived here: `tr C = m` trivially, `tr C² ` is pure pair correlation, and
`tr C³` is the first quantity carrying three-point information. That framing
drove everything in Part II.

## B. The bridge circularity test

The report's finding #1 — that the frozen pair correlation predicts the Gram
second moment to 0.04% — was called "the strongest direct validation" of the
Experiment 1 → 2 bridge. Both sides are the same multiset of pair differences, so
the agreement should measure binning and nothing else. Two controls:

| process | rel. error |
|---|---:|
| zeta first 10⁴ | 0.0421% |
| CUE | 0.0750% |
| **Poisson** | **0.0443%** |
| lattice | −4.38% |

and the bin-width scaling on zeta: `Δu` = 0.4 / 0.2 / **0.1** / 0.05 →
1.00% / 0.255% / **0.042%** / 0.0144%, i.e. `≈ Δu²`.

**Verdict: informative.** Poisson agrees as well as zeta; the error is
piecewise-constant quadrature error. The check validates smoothness of `R̂₂` at
the 0.1 scale and consistency of two code paths — nothing about zeta. (The
lattice's −4.4% failure is real content: it detects a non-smooth `R₂`.)

## C. The power calculation

The report set `EXPERIMENT3_READY = TRUE` on internal stability, which is
necessary but not sufficient. Eight *independent* CUE realisations gave a
between-realisation sd of ≈0.0012 on mean `p_pos`, against a zeta-vs-CUE effect
of 0.0064 — effect/noise ≈ 5.2.

**Verdict: informative at the time, later moot.** The instrument was real. But
Experiment 3's question was subsequently answered by a better experiment (Part
III), so readiness stopped mattering.

## D. The height controls read as a natural experiment

The report treated §11.2 as a null ("no large persistent separation"). Set side
by side it is not:

| sample | Level 1 (pair correlation) | Level 2 (inertia vs CUE) |
|---|---|---|
| zeta, first 10⁴ | differs (`D₀.₅` = 0.224, z ≈ 9) | differs (≈ −3 to −4σ) |
| zeta, near 10²¹ | matches GUE | matches CUE (≤ 0.4σ) |

**Verdict: informative.** The two levels appear and disappear together; there is
no case of "Level 1 agrees, Level 2 differs", which is the only pattern that would
indicate sensitivity beyond pair correlation. This was the first real evidence on
the project's central question, and it came free with controls already run.

---

# Part II — Attempted repairs

## E. The moment ladder

Since `tr C² ` is pure two-point and `tr C³` is the first three-point quantity, the
proposed replacement observable was `μ_k = tr(K^k)/n` with `K_ij = sinc(x_i−x_j)`,
against the sine-process targets `1, 4/3, 2, 13/4` from Alpöge–Furman §7.2(f).
`μ₂` becomes a validation (forced by Experiment 1); `μ₃` becomes the measurement.

Scouting run, n = 4000, showed it discriminates sharply — Poisson 1.99/4.90/14.0,
lattice exactly 1/1/1 (`sinc` vanishes at nonzero integers, so `K = I`), zeta at
10²¹ within 0.3% of all four targets — and that it carries the same finite-height
signature as Experiment 1.

**Verdict: informative, and it became change C2 of the draft v0.5 spec.**

## F. The k = 3 → k = 4 correction

The proposal put `μ₃` at the centre. That was wrong, and the arithmetic is
elementary. The Alpöge–Furman extremal (⅔N simple + ⅙N doubles) has normalised
spectrum = three atoms: 0 at weight ⅙, 1 at ⅔, 2 at ⅙. Its moments:

| k | extremal | true sine process |
|---|---|---|
| 1 | 1 | 1 |
| 2 | 4/3 | 4/3 |
| 3 | **2** | **2** |
| 4 | **10/3 ≈ 3.3333** | **13/4 = 3.25** |

**The extremal and the truth are indistinguishable through three moments and
first separate at the fourth.** This is exactly why §7.2(f) names `HL*(4)` as the
first conditional improvement.

**Verdict: informative, and it is one of the two small observations in this
project I have not found stated anywhere.**

## G. The `μ₄` measurement

Measurable and discriminating: zeta 10²¹ gives 3.2601 ± 0.0198, i.e. 0.5σ from the
true value and 3.7σ from the extremal; low-height zeta is 12.8σ low.

But the estimator carries a **finite-block bias**. Sub-blocking a sample into
blocks of 2500 gives a bias of −0.018; using whole clean runs of the same size
gives **−0.0007**. The bias is an artifact of block-edge truncation, not intrinsic.

**Verdict: informative, marginal.** The measurement works at ~4σ, but only when
compared against a matched, identically-biased control rather than the theoretical
13/4 — the shared bias has to cancel.

## H. The Christoffel ladder — two blockers, one fatal

Alpöge–Furman §7.2(d) states that with normalised moments to order `2m`, the sharp
lower bound for `n₊/d` is `1 − Λ_m(0)`, `Λ_m` the Christoffel function at 0. The
proposal was to compute that ladder empirically past `k = 4`, where the paper
stops.

The machinery works. `Λ_m(0) = 1/(H⁻¹)₀₀` with `H = [m_{i+j}]` the Hankel matrix
— derived by minimising `cᵀHc` subject to `c₀ = 1` — and from the exact moments it
returns **Λ₂ = 5/36**, reproducing the paper's stated value exactly.

**Blocker 1 (numerical).** Hankel conditioning explodes: 14.3 → 225 → **3510**.
Propagating only the measured `m₅, m₆` errors, 42% of draws are not valid moment
sequences and the `Λ₃` band is six times the quantity. Resolving it needs ~1100×
more data (~18 hours) — annoying, not prohibitive.

**Blocker 2 (mathematical, fatal).** `1 − Λ_m(0)` is **not** the certified
proportion:

| m | `1 − Λ_m` | Alpöge–Furman's constant |
|---|---:|---:|
| 1 | 0.7500 | **0.6667** (= 2 − m₂) |
| 2 | 0.8611 | **0.7222** (= 13/18) |

They do not coincide, by no constant offset or ratio. Converting `Λ_m` into a
proportion of simple on-line zeros needs the on-line/off-line block accounting,
which the paper writes out only for `m = 1`. Deriving it is mathematics, not
computation, and inventing it would be exactly the overreach the integrity rules
exist to prevent.

**Verdict: closed. The redesign died here.**

---

# Part III — Alternative objects

The premise: an apparatus claiming to see something RH-relevant must be tested
against a function where the analogue of RH is **false**. This discipline came
from the original Alpöge–Furman campaign, which demanded such a control in every
research brief, and was independently in use in `teal-sea/zeta-lab`. The v0.4
spec had it as an optional later extension. It produced everything below.

## I. Davenport–Heilbronn

`f(s) = 5^{-s} Σ_{r=1..5} a_r ζ(s, r/5)`, `(a₁…a₅) = (1, ξ, −ξ, −1, 0)`,
`ξ = 0.2840790438`. Functional equation ✓ (5.7e−26), real Hardy Z ✓ (3e−15),
**off-line zeros located directly** — including the documented
`0.808517 + 85.699348i`, reproduced independently. Counting deficit **8.3%**.

**Two traps caught, both of which would have inverted the conclusion:**

- *Scan resolution.* Step 0.1 found 108 zeros on [2000,2100] where 0.05/0.02/0.01
  all find 110. The missed 2% are the **close pairs** — which would have made DH
  look artificially repulsive, i.e. more GUE-like, in exactly the measurement the
  control depends on.
- *Wrong unfolding.* `θ_DH/π` counts **all** zeros; the point set has only the
  on-line ones. Unfolding by it gave mean spacing 1.0909 and a residual drifting
  monotonically to −270. Every statistic from that pass was invalid. The on-line
  process must be unfolded by its own smooth counting function.

**Verdict: highly informative.** The apparatus cannot distinguish DH from zeta
(inertia differences ≤0.005 for λ≥0.5).

## J. Epstein zeta, class number two

Direct evaluation needs analytic continuation; genus theory removes it. For
`D = d₁d₂` of class number two,
`ζ_Q(s) = ζ(s)L(s,χ_D) ± L(s,χ_d₁)L(s,χ_d₂)`. With `D = −15 = (−3)(5)`, validated
against the **direct Epstein double sum**: ratio exactly 1.0 at `s=3`, and
`Q₁+Q₂ = 2ζ_K`.

Far more RH-false than DH: **12 off-line zeros for t < 80** (DH: 2 for t < 120),
one at **σ = 1.026, outside the critical strip** — which only a function with no
Euler product can do. Counting deficit **32.3%**.

**Verdict: highly informative.** It upgraded the central finding from one
counterexample to two, and to a far more extreme one: the apparatus remains nearly
blind (≈0.02 at λ≥0.7) with a third of the zeros off the line.

## K. The number-variance result, and the control that destroyed it

Σ²(L), the count variance in windows of L mean spacings, appeared to separate the
three functions decisively and monotonically in off-line fraction:

| process | off-line | Σ²(20) |
|---|---:|---|
| zeta near 10²¹ | 0% | 0.577 |
| DH | 8.3% | 2.352 |
| Epstein | 32.3% | 6.027 |

This was written up as a result — "GUE-like short-range repulsion, Poisson-like
long-range rigidity" — before the control was run.

**The control.** The on-line zeros of an RH-false function are a **thinned** subset
of all zeros. For independent thinning with retention `p`, rescaled to unit
density,

    Sigma^2_thin(L) = p^2 · Sigma^2_orig(L/p) + (1-p)·L ,

and since a rigid process contributes only logarithmically, `(1−p)L` dominates and
produces **linear growth** — the exact signature attributed to the arithmetic.
Rigid CUE with points deleted at random reproduced the observed values within ~2σ
at both fractions, residuals in both directions.

**Verdict: artifact. Claim retracted.** Σ²(L) recovers the off-line fraction,
which the counting deficit gives directly and more simply. Short-range residuals
beyond thinning do exist, but they are incoherent across the two controls (DH more
repulsive, Epstein less at u=0.2 and more at u=0.5) and confounded with finite
height, so nothing is claimed from them.

---

# Ledger

| # | initiative | cost | verdict |
|---|---|---|---|
| A | structural analysis of observables | none (algebra) | **informative — fatal, and free** |
| B | bridge circularity (Poisson + bin scaling) | minutes | **informative** — finding #1 is quadrature |
| C | power calculation, 8 CUE realisations | ~10 min | informative, later moot |
| D | height controls as natural experiment | none (re-reading) | **informative** |
| E | moment ladder | ~30 min | informative — became spec change C2 |
| F | k=3 → k=4 correction | none (arithmetic) | **informative — novel observation** |
| G | `μ₄` with bias analysis | ~20 min | informative, marginal |
| H | Christoffel ladder to m=3 | ~40 min | **closed — fatal mathematical blocker** |
| I | Davenport–Heilbronn | ~2 h | **highly informative** |
| J | Epstein zeta, h=2 | ~1 h | **highly informative** |
| K | Σ²(L) rigidity claim | ~1 h | **artifact — retracted by control** |

---

# Lessons

1. **The cheapest checks were the most decisive.** Initiative A required no data
   and killed the experiment's premise; F was three lines of arithmetic and
   produced a novel observation. Neither needed a run.
2. **Every apparent discovery that was tested died.** The bridge (B), the
   inertia's independence (A), and the rigidity result (K) all looked like
   findings and all collapsed under a control that cost minutes. The two that
   survived — apparatus blindness, and the finite-height ladder — survived
   controls rather than avoiding them.
3. **The negative control produced everything.** Items I, J and K exist only
   because the design insisted on a function where RH is false. That was an
   optional extension in v0.4. It should have been a gate.
4. **Wrong unfolding is the most dangerous error in this subject.** It is silent,
   it produces plausible numbers, and in the DH case it biased the result in
   exactly the direction that would have confirmed the hypothesis. Mean spacing
   ≠ 1.000 is the check that catches it; it should be an assertion in code, not a
   diagnostic to inspect.
