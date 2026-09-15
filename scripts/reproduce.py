
#!/usr/bin/env python3
"""Run one or all experiments in isolated build directories."""
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "build"


def run(cmd: list[str], cwd: Path, *, numerical_threads: int | None = None) -> None:
    print("+", " ".join(cmd), f"(cwd={cwd})", flush=True)
    env = os.environ.copy()
    if numerical_threads is not None:
        for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
            env[name] = str(numerical_threads)
    subprocess.run(cmd, cwd=cwd, check=True, env=env)


def exp1() -> None:
    out = BUILD / "experiment1"
    out.mkdir(parents=True, exist_ok=True)
    run([sys.executable, str(ROOT / "experiments/experiment1/code/reproduce_experiment1.py"), "--output-dir", str(out)], ROOT)


def copy_clean(source: Path, target: Path) -> None:
    if target.exists():
        shutil.rmtree(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target)


def exp2() -> None:
    target = BUILD / "experiment2/frozen_release"
    copy_clean(ROOT / "experiments/experiment2/frozen_release", target)
    run([sys.executable, "src/experiment2_run.py"], target, numerical_threads=2)
    run([sys.executable, "src/verify_experiment2.py"], target, numerical_threads=2)


def exp3() -> None:
    target = BUILD / "experiment3/frozen_release"
    copy_clean(ROOT / "experiments/experiment3/frozen_release", target)
    run(["bash", "01_code/reproduce_experiment3bs_v1_1.sh", "--clean-generated"], target, numerical_threads=2)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment", choices=["1", "2", "3", "all"], required=True)
    args = parser.parse_args()
    if args.experiment in {"1", "all"}:
        exp1()
    if args.experiment in {"2", "all"}:
        exp2()
    if args.experiment in {"3", "all"}:
        exp3()
    print("Reproduction completed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
