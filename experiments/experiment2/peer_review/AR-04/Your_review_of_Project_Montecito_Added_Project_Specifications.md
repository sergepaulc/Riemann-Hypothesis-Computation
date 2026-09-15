Thank you. I read this third document carefully as a **proposed new direction for Project Montecito’s scope, deliverables, software, and publication strategy**.

My overall judgment is positive but qualified:

> **It contains an excellent software-and-reproducibility vision, and a valuable honest account of the project’s corrections. But I would not adopt it as a new Project Montecito specification in its present form.**

Several claims need to be narrowed, one project phase is closed too quickly, and the proposed “numerical companion” contains important assertions that cannot yet be treated as validated from this document alone.

## 1. The document is using the wrong specification baseline

The proposal says that it is “additive to v0.4,” that Experiment 3 is closed, that Experiment 4 is withdrawn, and that a draft v0.5 change specification is withdrawn.

But our actual current scientific baseline is **Project Montecito v0.6**, which already:

- removed the standalone Experiment 4;
- preserved Experiments 1–3;
- hardened Experiment 2’s numerical methodology;
- distinguished resolved and unresolved eigenvalue signs;
- introduced spectrum-first computation and block-stability requirements.

So this document cannot accurately be “additive to v0.4.” Nor can it say that it supersedes nothing while simultaneously closing an experiment and withdrawing prior directions.

I would reclassify it as:

> **Project Montecito — Proposed Publication and Software Release Plan v0.1**

It should not yet be called a scientific specification update. Once we agree on the scientific changes, those can be incorporated separately into a future specification version.

---

# 2. D1 — the negative result needs a major rewrite

The current claim is:

> A finite Hermitian apparatus Hλ=I−λC(X)H_\lambda=I-\lambda C(X) does not distinguish point processes arising from functions where RH holds from those where it fails.

There are three problems.

### First, we did not compare a known RH-true function with RH-false functions

The Riemann Hypothesis for ζ(s)\zeta(s) is not known to hold. CUE is a random-matrix point process, not a zeta or LL-function satisfying an RH theorem.

Therefore “functions where RH holds versus functions where it fails” is not an accurate description of the comparison.

We compared:

- Riemann-zeta ordinate data;
- CUE;
- critical-line ordinate subsets from two functions for which the analogue of RH is known to fail in the sampled ranges.

### Second, the apparatus does not receive the real parts of zeros

The toy input is a set of unfolded ordinates,

X={x(γi)}.X=\{x(\gamma_i)\}.

It does not receive

βi\beta_i

from

ρi=βi+iγi.\rho_i=\beta_i+i\gamma_i.

Thus the transformation

X⟼C(X)⟼Hλ(X)X\longmapsto C(X)\longmapsto H_\lambda(X)

is invariant under changes in the βi\beta_i’s that leave the ordinate data unchanged.

This gives us a precise structural limitation:

> **The ordinate-only Gaussian apparatus cannot directly encode critical-line membership. It can respond to RH failure only indirectly, insofar as off-line zeros alter the selected ordinate point process.**

That is stronger and cleaner than the present broad claim.

### Third, only two RH-false examples were tested

Davenport–Heilbronn and the selected Epstein zeta provide valuable stress tests. But two examples do not establish a universal impossibility theorem for the whole family of positive-definite kernels, all parameter choices, and all RH-false functions.

I would replace D1 with:

> **In the finite windows and parameter regime studied, the frozen ordinate-only Gaussian apparatus produced inertia profiles for the on-line zero subsets of Davenport–Heilbronn and the selected Epstein zeta that remained close to those of zeta and CUE, despite substantial finite-window evidence of off-line zeros. The experiment therefore found no reliable sensitivity to RH failure in these two controls. Structurally, this is consistent with the fact that the apparatus receives ordinates but not the real parts of the zeros.**

That is a credible negative result.

I would not write:

“the apparatus cannot detect RH failure.”\text{“the apparatus cannot detect RH failure.”}

---

# 3. D2 — the finite-height result is valid, but “vanishes” must be removed

The document says that the first-10410^4 finite-height effect “vanishes by height 101210^{12}.”

We already corrected that wording after the High-Height Replication review.

The actual estimates are

D0.5=0.224,0.016,−0.037D_{0.5} = 0.224,\quad0.016,\quad-0.037

for the first 10410^4, the 101210^{12} region, and the 102110^{21} region. But the matched-GUE standard deviation is approximately 0.02480.0248, giving an approximate two-standard-deviation resolution of 0.050.05.

Therefore the supported statement is:

> **The 22.4% low-height distortion is suppressed below the experiment’s approximately 5% D0.5D_{0.5} detection scale at both high heights.**

It is not established to be mathematically zero.

The rest of D2 is well framed. Calling it a **reproduction rather than a discovery**, while emphasizing the quality of the end-to-end artifact and calibrated statistic, is scientifically honest.

---

# 4. Experiment 3 should not yet be declared closed

The proposal says that Experiment 3’s question has already been answered by the RH-false controls and that the original GUE, Poisson, and lattice comparisons would merely “add rows.”

I disagree.

The two sets of controls answer different questions.

## Original Experiment 3

GUE,Poisson,lattice\text{GUE},\quad \text{Poisson},\quad \text{lattice}

change the **point-process geometry in a controlled and interpretable way**.

They ask:

> How does the fixed apparatus respond to level repulsion, independence, and maximal regularity?

## Davenport–Heilbronn and Epstein

These ask:

> Does the on-line ordinate subset of an RH-false function look different enough for the ordinate-only toy to respond?

Those functions change many things simultaneously. More importantly, off-critical-line membership is not directly supplied to the matrix.

The RH-false controls are therefore not replacements for the synthetic controls. They are **additional falsification tests**.

I would not necessarily run a large new Experiment 3 from scratch. Some GUE/CUE, Poisson, and lattice calculations have apparently already been performed during the review and exploration. But they should be formally organized and validated.

My recommendation is to **reframe**, rather than close, Experiment 3:

> **Experiment 3 — Controlled Comparators and Falsification Tests**
>
> 1. GUE/CUE, Poisson, and lattice: controlled point-process calibration.
> 2. Davenport–Heilbronn and Epstein: RH-false stress tests.
> 3. Matched thinning controls: identify effects caused merely by deleting points.
> 4. Fixed mm, fixed σ\sigma, fixed λ\lambda-range, repeated realizations.

That would turn all the exploratory work into one coherent final experiment.

---

# 5. The moment-ladder direction should not be completely withdrawn

The proposal says the moment-ladder draft is withdrawn because it did not reach a “publishable number,” and later excludes the moment ladder as a primary observable.

I agree with half of this.

The attempted **Christoffel-function route to a new lower bound** is closed. The known values do not convert automatically into simple-critical-line proportions, and deriving the missing on-line/off-line accounting would require new mathematics. That was correctly stopped.

But the fourth-moment observation survives:

m1extremal=m1sine=1,m_1^{\rm extremal}=m_1^{\rm sine}=1,m2extremal=m2sine=43,m_2^{\rm extremal}=m_2^{\rm sine}=\frac43,m3extremal=m3sine=2,m_3^{\rm extremal}=m_3^{\rm sine}=2,

while

m4extremal=103≠134=m4sine.m_4^{\rm extremal}=\frac{10}{3} \neq \frac{13}{4} = m_4^{\rm sine}.

And the exploratory high-height computation gave a measurable μ4\mu_4, although with a significant block-edge bias requiring matched controls or a core-plus-halo estimator.

So I would write:

> **The Christoffel-to-proportion program is closed. The fourth spectral moment remains a secondary higher-order diagnostic, not a route to a new bound and not a primary project claim.**

The proposed software package itself includes `moments.py` and `check_moments.py`, so completely “withdrawing” the moment ladder while shipping it as a check is also internally inconsistent.

---

# 6. D3 — the software companion is the strongest part of the proposal

I agree with the document that a carefully built software package may be the deliverable most likely to help another reader.

The proposed architecture is thoughtful:

- one paper-to-code map;
- one runnable script per finite identity or numerical illustration;
- explicit expected and computed values;
- deterministic tests;
- process-specific unfolding assertions;
- RH-false controls as mandatory stress tests;
- raw-data provenance and checksums.

However, the package should **not describe all of these as checks of the paper**.

There are at least four different epistemic categories.

## A. Exact finite identities

Examples:

R(ψ0)=43,R(\psi_0)=\frac43,

the arithmetic conversion from R(ψ)R(\psi) to 2/32/3 and 5/65/6, or the eigenvalues/signature of a finite 2×22\times2 block.

These can genuinely print:

```text
PASS
```

## B. Numerical reproductions of stated constants

Examples:

R(ψMT)=12+12cot⁡ ⁣(12)R(\psi_{\rm MT}) = \frac12+\frac1{\sqrt2}\cot\!\left(\frac1{\sqrt2}\right)

evaluated to a fixed precision.

These can report expected value, computed value, error, and tolerance.

## C. Finite numerical illustrations of asymptotic mathematics

Examples:

tr⁡G~N=0.9948\frac{\operatorname{tr}\widetilde G}{N}=0.9948

or

∥G~∥HS2N=1.2926versus1.32750.\frac{\|\widetilde G\|_{\rm HS}^2}{N} = 1.2926 \quad\text{versus}\quad 1.32750.

These do not “check” an asymptotic theorem unless a mathematically justified finite-TT error threshold is known. They should print:

```text
ILLUSTRATION / FINITE-T OBSERVATION
```

not `PASS`.

## D. Exploratory or falsification experiments

Examples:

- Davenport–Heilbronn;
- Epstein;
- moment measurements;
- random trials of the rank–trace inequality.

These are Montecito experiments, not checks of claims in the Alpöge–Furman paper.

This distinction matters especially for these proposed scripts:

- `check_theorem_a.py`
- `check_rank_trace.py`
- `check_weil_form.py`

A program that reproduces the constants 2/32/3 and 5/65/6 does not check Theorem A. It checks arithmetic following from the theorem’s formulas.

Six thousand random trials cannot verify Lemma 3.2. They can test an implementation and search for counterexamples.

And a finite numerical construction cannot validate the analytic asymptotics used in the theorem.

I would therefore rename them along these lines:

```text
reproduce_theorem_constants.py
verify_finite_block_signatures.py
illustrate_compressed_zero_side.py
test_rank_trace_implementation.py
measure_finite_T_trace_moments.py
run_rh_false_controls.py
```

The software would become more credible by claiming less.

---

# 7. The largest unsupported assertion in this document is D3’s Weil-form implementation

The document states that:

> “The compressed Weil form of arXiv:2608.13637 can be built numerically and its mechanism made visible.”

It also says that sixteen checks have already been run at least once.

But this attachment contains only the **specification of that package**, not:

- `weilform.py`;
- the check scripts;
- the generated outputs;
- the exact formulas used;
- an execution log;
- an independent audit.

Therefore, based on this document alone, I cannot treat D3 as a completed and validated deliverable.

I can say:

> **D3 is a promising and well-designed software proposal.**

I cannot yet say:

> **D3 successfully implements the Alpöge–Furman compressed form.**

That will require its own review.

And one distinction will be particularly important: does `weilform.py` construct the actual finite compression defined in the paper, or a zero-side illustrative matrix that reproduces the desired rank-one and (1,1)(1,1) blocks? Both can be valuable, but they are not the same claim.

---

# 8. “The Lean formalisation verifies it” should be removed or narrowed

The integrity section says that nothing in Montecito validates the theorem and then adds:

> “the Lean formalisation is what verifies it.”

Unless we have separately audited the exact scope and fidelity of that formalization, I would not make that assertion.

A safer statement is:

> **Nothing in this numerical package verifies the Alpöge–Furman theorem. The theorem rests on the mathematical proof and any accompanying formalization, whose scope is separate from this project.**

That avoids making Montecito responsible for assessing the completeness of the formal proof.

---

# 9. D4 — the method narrative is genuinely valuable

I strongly support preserving the record of failed interpretations and the controls that corrected them.

The best episodes are:

- the pair-correlation bridge turning out to be quadrature reconstruction;
- the Christoffel conversion failing at a mathematical rather than numerical step;
- the coarse DH scan missing close pairs in exactly the direction favorable to the hypothesis;
- the wrong DH unfolding producing plausible but invalid statistics;
- the number-variance ladder being explained by thinning.

The number-variance episode is especially instructive because the apparent result was retracted after the appropriate control reproduced it.

But I would not market all of these as “retractions.”

They are different:

- **retraction:** the number-variance arithmetic interpretation;
- **withdrawn interpretation:** μmax⁡\mu_{\max} as a rigidity proxy;
- **reframing:** the pair-correlation bridge;
- **closed research branch:** the Christoffel-to-bound route;
- **retained secondary idea:** μ4\mu_4.

That classification is more accurate and more informative.

---

# 10. A practical concern: distributing the raw Odlyzko data

The software rules say that the raw Odlyzko files should be committed to the repository.

Before doing that publicly, I would verify whether redistribution is permitted.

The safest default is usually:

- provide a download script pointing to the authoritative source;
- pin the URL;
- publish expected SHA-256 checksums;
- refuse to run if the downloaded file has the wrong checksum;
- keep derived Montecito artifacts in the repository if their redistribution status is clear.

That gives full reproducibility without assuming permission to republish the source tables.

---

# 11. My disposition of the proposal


| Proposal item                              | My assessment                                  |
| ------------------------------------------ | ---------------------------------------------- |
| Shift toward concrete deliverables         | **Strongly accept**                            |
| D1 as currently worded                     | **Major revision required**                    |
| D2 finite-height artifact                  | **Accept, replace “vanishes”**                 |
| D3 numerical companion                     | **Strong proposal; validation still required** |
| D4 method narrative                        | **Strongly accept**                            |
| Close Experiment 3                         | **Do not accept yet**                          |
| Withdraw Christoffel-to-bound route        | **Accept**                                     |
| Withdraw all higher-moment work            | **Do not accept completely**                   |
| Remove number variance as arithmetic claim | **Accept**                                     |
| Demote HλH_\lambda from recommended tool   | **Accept with softer wording**                 |
| Unfolding assertion in code                | **Strongly accept**                            |
| RH-false controls as mandatory gates       | **Strongly accept for relevant observables**   |
| Every script prints PASS/FAIL              | **Revise into evidence categories**            |
| Keep corrections in public record          | **Strongly accept**                            |


---

# 12. What I think the final Montecito structure should become

This document is trying to combine three different things:

1. a scientific specification;
2. a publication plan;
3. a software product specification.

That is why several statements conflict.

I would separate them.

## A. Scientific specification update

This would eventually say:

- Experiment 1 is frozen;
- Experiment 2 is numerically valid but structurally underpowered for its original higher-order question;
- the pair-correlation bridge is reconstruction;
- bposb_{\rm pos} is algebraic;
- synthetic and RH-false controls form the next falsification phase;
- μ4\mu_4 remains a secondary higher-order diagnostic;
- number variance and Christoffel-to-bound claims are closed.

## B. Numerical companion specification

This would contain the software map, modules, checks, environment, provenance, and evidence categories.

## C. Publication plan

This would contain:

- the finite-height reproduction;
- the ordinate-only toy’s limitations;
- controlled comparisons and falsification tests;
- the software companion;
- the methodological narrative.

That separation would make the project much easier to understand and defend.

## Final assessment

The third document contains a strong possible **endgame for Project Montecito**, especially in its emphasis on reproducible software and intellectual honesty.

But its central negative claim is presently too broad, its high-height language is too strong, and it closes Experiment 3 too early. Its software plan is excellent in spirit but must sharply distinguish:

exact identity≠numerical reproduction≠finite illustration≠experimental control≠proof verification.\text{exact identity} \neq \text{numerical reproduction} \neq \text{finite illustration} \neq \text{experimental control} \neq \text{proof verification}.

The most promising synthesis is not:

> “Experiment 2 failed, so stop.”

It is:

> **Experiment 2 was mathematically clean but underpowered for the question. That failure exposed exactly what information the apparatus contains, motivated stronger controls, and led to a more useful software and methodological contribution.**

I would use this third document as the basis for a revision, but I would not approve it unchanged as the next official Project Montecito specification.