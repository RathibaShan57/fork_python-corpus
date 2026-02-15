# PY-019 -- Monolith -- Python 3.6 -- poetry-core / poetry
#
# poetry 1.1.15 is the last release admitting Python 3.6 (2.4.2 needs >=3.10). Uses the pre-PEP-621 [tool.poetry] table.
PYTHON ?= python3

.PHONY: help setup install lock test check tools verify audit clean

help:
	@echo "PY-019  (poetry-core 1.0.8 / poetry 1.1.15 / Python 3.6.15)"
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
	python -m pip install 'poetry==1.1.15'

install:
	poetry install

lock:
	poetry install --no-root

test:
	$(PYTHON) -m pytest -q

check:
	$(PYTHON) tools/full_check.py

tools:
	$(PYTHON) tools/tool_integration.py --run

verify:
	$(PYTHON) tools/tool_integration.py --verify

audit:
	poetry show --tree

clean:
	rm -rf reports build dist .pytest_cache .coverage coverage.xml
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
