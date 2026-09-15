
#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOKEN = "{{CODE_REPOSITORY_URL}}"
TEXT_SUFFIXES = {".md", ".cff", ".json", ".yml", ".yaml", ".toml", ".txt"}


def targets() -> list[Path]:
    this_file = Path(__file__).resolve()
    return sorted(
        p for p in ROOT.rglob("*")
        if p.is_file()
        and p.resolve() != this_file
        and p.suffix.lower() in TEXT_SUFFIXES
        and ".git" not in p.parts
        and "build" not in p.parts
    )



def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--github-url", required=True)
    args = parser.parse_args()
    if not args.github_url.startswith("https://github.com/"):
        raise SystemExit("--github-url must be a full https://github.com/... URL")
    changed = 0
    for path in targets():
        text = path.read_text(encoding="utf-8")
        if TOKEN in text:
            path.write_text(text.replace(TOKEN, args.github_url), encoding="utf-8")
            changed += 1
    subprocess.run([sys.executable, str(ROOT / "scripts/create_manifest.py")], check=True)
    print(f"Updated {changed} files and regenerated the repository manifest.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
