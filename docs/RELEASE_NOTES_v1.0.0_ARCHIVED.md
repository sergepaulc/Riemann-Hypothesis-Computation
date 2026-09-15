# Release notes — v1.0.0

This is the first GitHub-ready reproducibility release for the Project Montecito
paper.

## Included

- Experiment 1 frozen derived inputs, pair-correlation artifacts, validation,
  figures, reports, original code fragments, and a clean public reproduction
  runner.
- Experiment 2 complete primary code, frozen inputs, spectra, inertia tables,
  figures, independent verifier, validation extension, final report, closure
  report, and peer-review record.
- Experiment 3 corrected bounded-study release v1.1, including code, protocol,
  exact controls, tests, independent validators, all endpoint rows, figures,
  reports, and peer review.
- Repository-level SHA-256 manifest, paper-to-code map, isolated reproduction
  runner, CI workflow, citation metadata, and repository-linked manuscript v1.3.

## Data policy

Raw third-party Odlyzko tables are not redistributed. Exact authoritative URLs
and SHA-256 fingerprints are provided in `data/odlyzko_tables.json`, with a
fail-closed downloader. Checksum-locked derived unfolded coordinates used by the
experiments are included.

## Validation

The release-level verifier covers every committed file. Smoke tests validate the
Experiment 1 headline statistics, all 19 Experiment 2 frozen verification checks,
and all 8 Experiment 3 unit tests. Experiment 3's corrected release also retains
its prior independent clean-copy, end-to-end replication record.

## Deferred work

The larger preregistered higher-order attribution study is not represented as
executed and is not part of this paper's reproducibility claim.
