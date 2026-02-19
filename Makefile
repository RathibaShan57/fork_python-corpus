# PY-054 -- Microservices -- Python 3.8 -- setuptools / uv
#
# uv 0.12.9 runs here -- 3.8 is exactly its floor, and this is the CURRENT LATEST uv, not a rolled-back one. Verified in-session: `uv venv --python 3.8` succeeds, `uv pip install` resolves, `uv lock` produces a lockfile, and `uv python install 3.8` installs a managed CPython 3.8.20. After two families in which this axis was entirely dark, it is live. NOTE: uv requires a PEP 621 [project] table, so it cannot drive a poetry-core branch.
PYTHON ?= python3

.PHONY: help setup install lock test check tools verify audit clean

help:
	@echo "PY-054  (setuptools 75.3.4 / uv 0.12.9 / Python 3.8.18)"
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
	curl -LsSf https://astral.sh/uv/install.sh | sh

install:
	uv sync

lock:
	uv sync --frozen

test:
	$(PYTHON) -m pytest -q

check:
	$(PYTHON) tools/full_check.py

tools:
	$(PYTHON) tools/tool_integration.py --run

verify:
	$(PYTHON) tools/tool_integration.py --verify

audit:
	uv pip list

clean:
	rm -rf reports build dist .pytest_cache .coverage coverage.xml
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
