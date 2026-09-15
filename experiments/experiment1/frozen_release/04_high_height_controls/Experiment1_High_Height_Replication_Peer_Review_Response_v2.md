# Project Montecito — Response to High-Height Replication Peer Review — Version 2

## Overall assessment

The third peer review is accepted as a strong end-to-end independent replication. It confirms every published numerical statistic and identifies one important confound that is worth closing explicitly.

## Dispositions

| Review item | Decision | Action |
|---|---|---|
| End-to-end replication exact | Accept | No numerical artifact regenerated |
| Precision handling correct | Accept | Label theoretical versus empirical local density |
| Nonlinear-unfolding confound | Strongly accept | Independently reproduced tail test and added it to the report |
| "Disappears" too strong | Strongly accept | Replaced with "suppressed below ~5% detection floor" |
| Sign test | Accept with qualification | Added as descriptive; do not call assumption-free |
| Block-SD comparison | Accept | Added explicit warning not to over-read n=10 SD differences |
| Refusal to fit convergence rate | Accept | Keep; log intermediate-height comparison only as a prospective question |
| Frozen GUE ensemble reuse | Accept | Continue using the preregistered 200-replicate control |
| High-height samples for future reference | Accept | Clarified migration roles of low- and high-height samples |

## One minor reviewer arithmetic correction

The review says the full first-10,000 theoretical local density changes by a factor of 3.6 while quoting `log(gamma/2pi)` endpoints 0.81 and 7.36.

With the stated density formula `rho(T) = log(T/2pi)/(2pi)`, the endpoint density ratio is actually approximately **9.08**.

This does not weaken the reviewer's objection. The important confound test uses tails where the density ratios are only 1.088, 1.035, and 1.012, and the large D0.5 deficit survives.

## Result status

No previously published point estimate changes.

The substantive wording update is:

> **High height suppresses the low-height D0.5 anomaly below the present experiment's ~5% detection floor; it does not prove D0.5 equals exactly zero.**

The finite-height interpretation remains strongly supported.
