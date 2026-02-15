# PY-029 -- Monolith -- Python 3.7 -- setuptools / uv
#
# uv 0.12.9 REFUSES Python 3.7: "Python 3.7.17 is not supported. Please use Python 3.8 or newer." uv 0.0.5, its first release, already declared >=3.8, and `uv python install 3.7` fails because python-build-standalone's floor is 3.8. Moving the family up one minor version did not help and will not until 3.8.
PYTHON ?= python3

.PHONY: help setup install lock test check tools verify audit clean

help:
	@echo "PY-029  (setuptools 68.0.0 / uv 0.12.9 / Python 3.7.17)"
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
