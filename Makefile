# PY-139 -- Monolith -- Python 3.11 -- poetry-core / poetry
#
# poetry 2.4.2 -- the current latest release. On the 2.x line it reads and writes PEP 621 [project]; the [tool.poetry] table it still accepts is a compatibility path, not the source of truth.
PYTHON ?= python3

.PHONY: help setup install lock test check tools verify audit clean

help:
	@echo "PY-139  (poetry-core 2.4.1 / poetry 2.4.2 / Python 3.11.13)"
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
	python -m pip install 'poetry==2.4.2'

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
