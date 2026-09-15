
PYTHON ?= python

.PHONY: setup verify smoke test reproduce-exp1 reproduce-exp2 reproduce-exp3 reproduce-all manifest

setup:
	$(PYTHON) -m venv .venv
	.venv/bin/python -m pip install --upgrade pip
	.venv/bin/python -m pip install -r requirements.txt

verify:
	$(PYTHON) scripts/verify_repository.py

smoke:
	$(PYTHON) scripts/smoke_test.py

test:
	pytest -q experiments/experiment1/tests experiments/experiment3/frozen_release/01_code/tests

reproduce-exp1:
	$(PYTHON) scripts/reproduce.py --experiment 1

reproduce-exp2:
	$(PYTHON) scripts/reproduce.py --experiment 2

reproduce-exp3:
	$(PYTHON) scripts/reproduce.py --experiment 3

reproduce-all:
	$(PYTHON) scripts/reproduce.py --experiment all

manifest:
	$(PYTHON) scripts/create_manifest.py
