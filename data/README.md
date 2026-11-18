# Input data

The main reproduction commands use the derived unfolded coordinates supplied with each experiment. The source catalogue is `odlyzko_tables.json`. To download the original tables separately, run from the repository root:

```bash
python data/download_odlyzko_tables.py zeros1 zeros3 zeros4
```

This requires network access. Original source files are written under `data/raw/` and checked against their recorded fingerprints. Ordinary documentation edits do not affect these checks.
