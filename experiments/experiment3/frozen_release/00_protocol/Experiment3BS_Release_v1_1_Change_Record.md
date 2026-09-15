# Project Montecito — Experiment 3BS Release v1.1 Change Record

**Date:** September 11, 2026  
**Internal name:** Experiment 3BS — Bounded Study  
**Paper-facing name:** Experiment 3  
**Release status:** Corrected publication candidate after independent peer review

## Relationship to the original bounded study

The original bounded-study protocol remains immutable:

```text
Experiment3_Bounded_Cloud_Closure_Protocol_v1.md
SHA-256: 815e08aec7f55ddb5ba00655a24df77be94bad9b05384027c39a0c316a16251e
```

The original v1 package is preserved as the historical execution record:

```text
Project_Montecito_Experiment3_Bounded_Cloud_Closure_v1.zip
SHA-256: 1fc334dabcc2ccd03fc421f0091c542d6f63c6348b4d5b51817a8c0ebd1ea48e
```

Release v1.1 does not change the protocol, data, random-seed derivation, windows, kernel, core/halo geometry, control counts, endpoint definitions, or claim boundary. It corrects the reproducibility package and the presentation after independent replication.

## Peer-review-driven corrections

1. `group_summary.csv` and `mu4_difference_decomposition_vs_cue.csv` are now generated deterministically from `all_window_endpoints.csv` by shipped code.
2. The residual-based `Q4` closure calculation is no longer presented as an independent reconstruction check. Direct ordered-quadruple enumeration validates every collision class on small matrices.
3. The complete unit-test source is shipped with its execution log.
4. The paper and result tables distinguish individual-CUE-window variability from the bootstrap variability of a 16-window CUE mean.
5. The paper distinguishes the marginally high `D1` sample near zero number `10^12` from the CUE-consistent `D2` sample near zero number `10^21`.
6. The exact homometric control is moved earlier in the paper because it establishes the fourth moment's information capacity before the zeta comparison.

## Scientific-equivalence rule

The corrected pipeline was rerun from the same frozen inputs and protocol. All common scientific endpoint values must match the v1 release within `1e-12`. Runtime, memory, release identifiers, new validation fields, and the retired circular check are excluded from this equivalence comparison.

## Preserved boundary

```text
EXPERIMENT_3BS_SCIENTIFIC_RESULT       = UNCHANGED
NEW_ZETA_DATA                          = NONE
NEW_CUE_OR_POISSON_DESIGN              = NONE
D3_ACCESS                              = FALSE
FULL_PREREGISTERED_EXPERIMENT_3        = PRESERVED_AND_DEFERRED
```
