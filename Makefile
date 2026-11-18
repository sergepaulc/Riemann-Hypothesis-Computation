.PHONY: check reproduce
check:
	python scripts/verify_repository.py
	python scripts/smoke_test.py
	python -m pytest -q
reproduce:
	python scripts/reproduce.py --experiment all
