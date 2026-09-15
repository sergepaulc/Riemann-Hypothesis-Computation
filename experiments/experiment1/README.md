
# Experiment 1 — pair-correlation baseline

Experiment 1 measures the edge-corrected pair correlation of three 10,000-zero
samples: the first 10,000 zeros and samples near zero numbers `10^12` and
`10^21`. The public repository includes the frozen derived coordinates,
calibration outputs, figures, reports, and original source fragments.

## Public reproduction path

```bash
python code/reproduce_experiment1.py
```

from this directory, or from the repository root:

```bash
make reproduce-exp1
```

The public runner recomputes the pair histograms, `D_0.5`, and `S_30` from the
checksum-locked unfolded coordinates and validates them against the frozen
summary. It is a clean public reimplementation of the archived computation;
the original low-height script and high-height method note are preserved under
`frozen_release/`.

Raw Odlyzko tables are intentionally omitted. Use the repository-level downloader
in `data/download_odlyzko_tables.py` for raw-source provenance.
