
#!/usr/bin/env python3
"""Download the exact Odlyzko source tables used for Riemann-Hypothesis-Computation provenance."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parent
CATALOG = json.loads((ROOT / "odlyzko_tables.json").read_text(encoding="utf-8"))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def download(name: str, output_dir: Path, force: bool) -> None:
    entry = CATALOG["tables"][name]
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / f"{name}.txt"
    if path.exists() and not force:
        digest = sha256(path)
        if digest == entry["sha256"]:
            print(f"{name}: already present and verified")
            return
        raise RuntimeError(f"{path} exists but has unexpected SHA-256 {digest}")
    request = urllib.request.Request(entry["url"], headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request) as response, path.open("wb") as out:
        while block := response.read(1 << 20):
            out.write(block)
    digest = sha256(path)
    if digest != entry["sha256"]:
        path.unlink(missing_ok=True)
        raise RuntimeError(f"{name}: SHA-256 mismatch: {digest}")
    print(f"{name}: verified {digest}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("tables", nargs="*", choices=sorted(CATALOG["tables"]), default=sorted(CATALOG["tables"]))
    parser.add_argument("--output-dir", type=Path, default=ROOT / "raw")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    for name in args.tables:
        download(name, args.output_dir, args.force)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
