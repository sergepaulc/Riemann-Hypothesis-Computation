# Version 1.0 — Validation and reproduction coverage

Checked November 17, 2026. These checks concern the supplied clean package, not external academic peer review.

## Source and environment

The computational baseline is the complete saved `Riemann-Hypothesis-Computation_GitHub_Repository_v1.0.1.zip` archive dated September 15, 2026. It was combined with the latest corrected Version 1.0 paper available in this conversation. The public version label is now **1.0**. Live GitHub retrieval was unavailable, so later online edits are not certified as included.

Tests ran on Linux with Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0, pandas 2.2.3, Matplotlib 3.10.8, mpmath 1.3.0, and pytest 9.0.2. Those packages were already installed; a fresh network installation was not performed.

## Checks actually completed

| Check | Result |
|---|---|
| Experiment 1 | Three 10,000-zero full-sample pair-correlation calculations rerun. Headline counts, short-range deficits and correlation integrals agree within the documented tolerances. |
| Experiment 2 | 144 spectra and 2,592 inertia classifications recomputed. All 19 numerical verification checks passed. The two compared primary CSV tables have zero numerical difference from the archived reference values in this environment. |
| Supplementary Experiment 2 | Eight supplementary Gaussian-width tables agree with their own archived outputs under relative and absolute tolerances of 2e-10. This is not a claim of bitwise equality; sensitive condition-number diagnostics can have small absolute rounding differences. |
| Experiment 3 | All 176 endpoint rows and three additional summary/decomposition tables agree exactly numerically with the archived values in this environment. The separate collision and high-precision moment validators passed. |
| Smoke checks | Passed for Experiments 1, 2 and 3. |
| Unit tests | 11 passed, including the eight Experiment 3 tests and checks of input fingerprints and recorded random-seed settings. |
| Markdown mathematics | All 589 expressions parsed in local MathJax with zero reported errors. All 89 display blocks and 500 protected inline expressions survived Markdown processing unchanged; 17 tables and eight figure links were retained. |
| Paper layout | All 34 PDF pages inspected. Word and PDF use the same source content. Real-part, piecewise, norm, and greater-than labels render without the conversion errors identified during preparation. No page number on the first page. |

The numerical scripts run into separate marked work directories. They do not overwrite the committed reference outputs. Supplementary-validator relative-error columns are compared to the same validator's archived output, since its error normalization differs from that of the primary runner.

## Formatting and packaging adjustments

The publication keeps Version 1.0. Paper formulas and numerical results are unchanged. Four appendix-availability sentences were adjusted so they do not promise removed administrative documents; software-release references were synchronized to v1.0. Word equation text is unchanged: only literal rendering properties for `>2` and `neg` labels were normalized to prevent conversion errors. The PDF was exported from that Word file and is 34 pages, rather than the previous separately typeset 35-page PDF.

Governance documents, internal review conversations, earlier paper drafts and Git history are not included. Scientific input fingerprints remain automated; ordinary documentation is not checksum-locked. Experiment 3's original seed namespace is retained in a JSON settings file so the numerical random streams do not depend on an excluded narrative protocol.

## Remaining limits

The source archive supplies Experiment 1's finite-GUE and Poisson calibration outputs and settings, but not a complete runnable generator for every original calibration. The main rerun therefore does **not** recreate those ensembles. The data are retained as reference results; this limitation has not been filled by inventing a replacement simulation.

The eight paper figures are supplied. Available diagnostic figure scripts were run, but every publication panel is not claimed to have been regenerated pixel-for-pixel. The [results map](RESULTS_MAP.md) identifies coverage, including the distinction between the stored bootstrap uncertainty comparison and the paper's finite-reference mean scale.

Original Odlyzko-table downloads and GitHub's live math preview were not retested. A final browser check after upload is still needed. No new external mathematical proof audit is claimed.

Machine-readable check results: [validation_results.json](validation_results.json).
