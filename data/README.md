
# Data provenance

Raw third-party Odlyzko tables are not committed. Download and verify them with:

```bash
python data/download_odlyzko_tables.py zeros1 zeros3 zeros4
```

The authoritative source URLs and exact SHA-256 fingerprints are in
`odlyzko_tables.json`.

The **derived unfolded coordinates actually consumed by the three experiments
are committed inside the frozen experiment releases**. Therefore the principal
paper computations can be reproduced without downloading the raw tables. The
raw files are needed only to repeat the source-ingestion and provenance layer.
