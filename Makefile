# PY-177 -- Monolith -- Python 3.13 -- uv_build / pip
#
# pip 26.2.1 -- the current latest release, running here without a rollback.
PYTHON ?= python3

.PHONY: help setup install lock test check tools verify audit clean

help:
	@echo "PY-177  (uv_build 0.12.9 / pip 26.2.1 / Python 3.13.7)"
	@echo ""
	@echo "  make setup     install the package manager this branch is pinned to"
	@echo "  make install   install the project and its tool pins"
	@echo "  make lock      install from the committed lockfile only"
	@echo "  make test      run the pytest suite"
	@echo "  make check     cross-file consistency audit (tools/full_check.py)"
	@echo "  make tools     run every wired tool, honouring skips (exit 3)"
	@echo "  make verify    check every tool is wired"
	@echo "  make audit     dependency listing for this branch's manager"

setup:
	python -m pip install --upgrade 'pip==26.2.1'

install:
	python -m pip install -e . -r requirements-dev.txt

lock:
	python -m pip install --no-deps -r requirements.lock

test:
	$(PYTHON) -m pytest -q

check:
	$(PYTHON) tools/full_check.py

tools:
	$(PYTHON) tools/tool_integration.py --run

verify:
	$(PYTHON) tools/tool_integration.py --verify

audit:
	python -m pip list --format=json

clean:
	rm -rf reports build dist .pytest_cache .coverage coverage.xml
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
