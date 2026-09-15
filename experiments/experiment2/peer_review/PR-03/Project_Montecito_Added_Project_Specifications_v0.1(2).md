# Project Montecito — Added Project Specifications
## Version 0.1 — Outputs, publication, and the software package

**Status:** proposal. Additive to v0.4; supersedes nothing.
**Date:** 1 September 2026.
**Relationship to prior specs.** v0.4 specified Experiments 1–4. Experiments 1 and
2 are complete and independently reviewed. Experiment 3's question has been
answered by a stronger experiment (the RH-false controls) and is closed.
Experiment 4 is withdrawn as out of scope. The draft v0.5 change specification is
**withdrawn**: its central proposal, the moment ladder, was subsequently shown not
to reach a publishable number (see `notes/12-exploring_further_experiment2.md`,
Part II H).

This document specifies what the project produces and how it is shared.

---

# 1. What the project actually found

Stated plainly, so the deliverables below can be scoped honestly:

- A natural indefinite Hermitian construction built on zeta zeros **cannot detect
  RH-failure**, demonstrated against two independent RH-false functions.
- The first 10,000 zeta zeros are measurably **not** in the asymptotic regime, and
  the effect vanishes by height 10¹².
- The compressed Weil form of arXiv:2608.13637 can be built numerically and its
  mechanism made visible.
- Three apparent findings died to cheap controls, and the controls are more
  interesting than the findings would have been.

No new mathematics. No bound improved. No claim about RH.

---

# 2. The four deliverables

## D1 — The negative result

**Claim.** A finite Hermitian apparatus of the form `H_λ = I − λC(X)`, built from
an unfolded zero configuration with a fixed positive-definite kernel, does not
distinguish point processes arising from functions where RH holds from those where
it fails.

**Evidence.** Inertia profiles for Davenport–Heilbronn (8.3% of zeros off the
critical line) and an Epstein zeta of class number two (32.3% off), against zeta at
two heights and CUE. Differences ≤0.005 for DH and ≈0.02 for Epstein at λ ≥ 0.5.

**Why it is worth publishing.** Alpöge–Furman §1.4 concedes in one sentence that
their method's inputs hold verbatim for Davenport–Heilbronn and Epstein zeta
functions. This turns that sentence into a measurement, and shows the same holds
for a computational analogue.

**Scope limit to state.** This is a statement about one family of toy
constructions, not about the analytic method, and certainly not about RH.

## D2 — The finite-height ladder

**Claim.** The short-range pair-correlation deficit of zeta zeros relative to the
asymptotic GUE prediction falls from 22.4% (first 10⁴ zeros) to 1.6% (near the
10¹²-th) to −3.7% (near the 10²¹-st).

**Evidence.** `D₀.₅` with a matched 200-replicate GUE Monte Carlo calibration,
SHA-256-pinned Odlyzko inputs, arbitrary-precision θ-unfolding, independently
reproduced.

**Status.** A reproduction, not a discovery — the slow approach to GUE at low
height is documented (Odlyzko). The contribution is the artifact: a clean,
checkable, end-to-end demonstration with an explicit statistic and a calibrated
null.

## D3 — The numerical companion (the software package)

**Claim.** None. It is a tool.

**Content.** Specified in §3 below.

**Why it is worth publishing.** arXiv:2608.13637 ships a Lean formalisation and no
numerical companion. There is currently no way to *see* the mechanism — on-line
zeros producing positive rank-one directions, off-line pairs producing hyperbolic
(1,1) blocks, the constant emerging from a one-line variational problem — without
writing it yourself.

**This is the deliverable most likely to be used by someone else.**

## D4 — The method narrative

**Claim.** None. It is an account.

**Content.** `notes/12-exploring_further_experiment2.md`: eleven initiatives, four
informative, two artifacts caught by controls, one closed by a mathematical
obstruction. Includes the two traps that would have inverted a conclusion (wrong
unfolding; scan resolution biasing toward the hypothesis).

**Why it is worth publishing.** It is an honest record of what careful
computational mathematics looks like from the inside, including three retractions.
For a general-audience venue this is likely the most readable of the four.

---

# 3. Software package specification

## 3.1 Organising principle

> **Every numerically checkable claim in arXiv:2608.13637 gets one runnable check
> that prints the paper's value, the computed value, and a pass/fail.**

That is the product. Everything else is support.

## 3.2 The paper-to-code map

| paper | claim | expected | check |
|---|---|---|---|
| Thm A | 2/3, 5/6 | exact | `check_theorem_a.py` |
| Thm A / §7.2 | 0.67250070367941, 0.83625 | exact | `check_theorem_a.py` |
| §5.6 | `R(ψ₀) = 4/3` | exact | `check_variational.py` |
| §5.6 | `R(ψ_MT) = ½ + (1/√2)cot(1/√2)` | 8 digits | `check_variational.py` |
| — | ψ_MT is the minimiser | EL spread < 1e-7; free basis min agrees | `check_variational.py` |
| §2 | compressed form `G̃` from a configuration | constructs | `check_weil_form.py` |
| (Z) | on-line zero → signature (1,0) | exact | `check_block_structure.py` |
| (Z) | off-line pair → signature **(1,1)**, trace 2 | exact at every depth | `check_block_structure.py` |
| (Z) | `tr G̃ = (1+o(1))N` | 0.9948 at T=100 | `check_traces.py` |
| (P) | `‖G̃‖²_HS = (R(ψ)+o(1))N` | 1.2926 vs 1.32750 at T=100 | `check_traces.py` |
| Lem 3.2 | rank–trace inequality | 0 violations / 6000 trials | `check_rank_trace.py` |
| Lem 3.2 | extremal case attains it | gap **exactly 0** | `check_rank_trace.py` |
| §7.2(b) | extremal: ⅔N simple + ⅙N doubles | tr = N, HS = 4/3 N | `check_extremal.py` |
| §7.2(d) | `Λ₂(0;1) = 5/36` | exact | `check_christoffel.py` |
| §7.2(f) | `m_k(1) = 1, 4/3, 2, 13/4` | converging; 10²¹ within 0.3% | `check_moments.py` |
| **§1.4** | **inputs hold for Davenport–Heilbronn** | apparatus blind; off-line zeros located | `check_rh_false.py` |

Sixteen checks. Every one has already been run at least once during this project;
none is speculative.

## 3.3 Layout

```
montecito/
  windows.py                 psi_0, psi_MT, phi_T, R(psi), minimiser
  zeros.py                   zeta zeros, theta, Gram points, unfolding
  weilform.py                W_T, ZeroConfig (incl. planted off-line zeros),
                             signatures, rank-trace lemma, extremal case
  paircorr.py                pair correlation, Montgomery form factor
  pointproc.py               sine kernel, CUE, GUE, Poisson, Gaudin
  moments.py            NEW  moment ladder, Hankel/Christoffel function
  davenport_heilbronn.py     RH-false control #1
  epstein.py                 RH-false control #2
checks/                      one script per row of the map; each prints
                             paper value / computed value / PASS-FAIL
tests/                       the checks, wrapped as assertions
experiments/                 H_lambda = I - lambda C, the toy that failed,
                             kept ONLY as the subject of D1 and clearly
                             labelled as such
docs/paper-to-code.md        the map above, as the entry point
data/                        cached zeros (gitignored); raw Odlyzko committed
```

## 3.4 Rules

1. **`H_λ` is not part of the companion.** It moves to `experiments/` with a
   header stating it is the subject of a negative result and should not be used as
   a tool. It must not sit beside code a reader could mistake for a recommendation.
2. **Every check is runnable from a clean clone** with no arguments, and prints
   its own expected value. A check that needs an explanation is not finished.
3. **Assert `mean spacing ≈ 1` after every unfolding.** This is the error that
   silently inverted a conclusion in this project; it becomes a runtime assertion,
   not a diagnostic.
4. **RH-false controls are a gate, not an extension.** Any future observable added
   to the package ships with its DH and Epstein values.
5. **Cached data is regenerable; raw source data is committed.** Odlyzko
   `zeros1/3/4` and the Experiment 1 CSVs are committed with checksums; `.npz`
   caches are not.

## 3.5 Out of scope

Experiment 4 (Mertens / square-root cancellation); any attempt to improve a bound;
the Christoffel ladder beyond `m = 2`; the moment ladder as a primary observable;
Σ²(L) as a rigidity claim.

---

# 4. Publication shape

| deliverable | form | audience |
|---|---|---|
| D3 package | public repository, MIT or Apache-2.0 | anyone reading the paper |
| D1 + D2 | one technical note alongside the repo | number theory / RMT readers |
| D4 | long-form article | the blog's general audience |

**Order:** D3 first — the other three cite it. D4 is the most readable and can be
written from `notes/` largely as-is.

**Naming.** The repository should not be titled to imply progress on RH or on the
two-thirds theorem. "A numerical companion to arXiv:2608.13637" is accurate.

---

# 5. Integrity rules for the release

Carried from v0.4 §Research Integrity Rules, with three additions:

- **Nothing in this project constitutes evidence for or against RH, or validates
  the Alpöge–Furman theorem.** The package *illustrates* the mechanism; the Lean
  formalisation is what verifies it.
- **Retractions stay in the record.** The Σ²(L) rigidity claim, the bridge
  "validation", and the moment-ladder route are reported as things that failed,
  with the controls that killed them. Removing them would misrepresent the work.
- **Reproductions are labelled as reproductions.** D2 is a reproduction of a known
  phenomenon; it must say so in its first paragraph.

---

# 6. Execution order

1. `docs/paper-to-code.md` — write the map first; it determines the rest.
2. `checks/` — port the sixteen checks from existing session code.
3. `moments.py` — the one new module (ladder + Christoffel).
4. `tests/` — wrap the checks as assertions; add the unfolding assertion (§3.4.3).
5. Move `H_λ` to `experiments/` with its header.
6. Rewrite `README.md` as a companion, not a research log.
7. Package metadata, licence, environment pin.
8. Then D1/D2 note, then D4 article.

Steps 1–3 are the release. Steps 4–7 make it usable. Step 8 follows the code.
