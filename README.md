# orderlab -- PY_V36_POETRY_CONDA_MONO

Order-pricing domain used as a white-box tool-evaluation fixture. One branch of
the Python 3.6 family: 24 branches across 3 build backends, 4 package managers
and 2 architectures. The domain layer is byte-identical on every branch, so any
difference in tool output is attributable to the branch variables alone.

## Branch variables

| Variable | This branch |
|---|---|
| Branch | `PY_V36_POETRY_CONDA_MONO` |
| Python | 3.6.15 |
| Build backend | poetry-core 1.0.8 |
| Backend metadata | [tool.poetry] |
| Package manager | conda (solver-resolved) |
| Architecture | Monolith |
| Scenario | 1 - Monolithic |
| Source root | `src` |
| Branch usable | yes |

> **Build backend.** poetry-core 1.0.8 -- last release admitting Python 3.6. Predates poetry-core 2, so metadata lives in [tool.poetry], not PEP 621 [project].

> **Package manager.** conda can create a python=3.6.15 environment from conda-forge, but conda.anaconda.org and repo.anaconda.com are 403 at this build host's egress proxy, so no solved lock could be produced here. environment.yml is complete and solves on the operator's machine.

## Supported tools

29 tools are wired on this branch: 15 primary and 14 alternative, covering the
103-metric white-box framework. **8 of them can run on Python 3.6;
21 cannot.**

That is the measurement, not a defect. Every tool is pinned at its current
latest release, identically on all 24 branches, and the pins that this
interpreter excludes are guarded with an environment marker so they drop out of
resolution instead of failing it. A tool that cannot run exits **3**, not 0 --
a skip that looks like a pass is the failure mode this corpus exists to expose.

### Running here

| Tool | Role | Pin | Why |
|---|---|---|---|
| `Radon` | primary | `radon==6.0.1` | radon 6.0.1 declares no Requires-Python and imports cleanly on 3.6. |
| `cognitive-ast` | primary | _binary / stdlib_ | Not a PyPI package -- no distribution of that name exists. |
| `jscpd` | primary | `jscpd@5.1.1` | jscpd 5.1.1 is an npm package that runs on Node, not on the project interpreter, so the Python version is irrelevant to it. |
| `Beniget` | primary | `beniget==0.5.0` | beniget 0.5.0 declares >=3.6 and, unlike lizard and pydriller, means it. |
| `Opengrep` | alternative | _binary / stdlib_ | Standalone binary with its own parser. |
| `Opengrep (taint mode)` | alternative | _binary / stdlib_ | Same binary, taint mode. |
| `Trivy` | alternative | _binary / stdlib_ | Standalone binary; scans manifests and lockfiles, never the interpreter. |
| `sys.settrace driver (stdlib)` | alternative | _binary / stdlib_ | stdlib sys.settrace driver, written 3.6-compatible.. |

### Dark here

| Tool | Role | Pin | Why |
|---|---|---|---|
| `CrossHair` | primary | `crosshair-tool==0.0.110` | crosshair-tool 0.0.110 declares Requires-Python >=3.8; pip refuses the pin on 3.6.. |
| `Coverage.py` | primary | `coverage==7.16.0` | coverage 7.16.0 declares Requires-Python >=3.10; pip refuses the pin on 3.6.. |
| `Pymcdc` | primary | `pymcdc==0.2.6` | pymcdc 0.2.6 declares Requires-Python >=3.10; pip refuses the pin on 3.6.. |
| `Lizard` | primary | `lizard==1.24.0` | lizard 1.24.0 declares NO Requires-Python at all, so pip installs it without complaint. |
| `testmon` | primary | `pytest-testmon==2.2.0` | pytest-testmon 2.2.0 declares Requires-Python >=3.10; pip refuses the pin on 3.6.. |
| `pylint` | primary | `pylint==4.0.8` | pylint 4.0.8 declares Requires-Python >=3.10.0; pip refuses the pin on 3.6.. |
| `Semgrep OSS` | primary | `semgrep==1.176.0` | semgrep 1.176.0 declares Requires-Python >=3.10; pip refuses the pin on 3.6.. |
| `Bandit` | primary | `bandit==1.9.4` | bandit 1.9.4 declares Requires-Python >=3.10; pip refuses the pin on 3.6.. |
| `pip-audit` | primary | `pip-audit==2.10.1` | pip-audit 2.10.1 declares Requires-Python >=3.10; pip refuses the pin on 3.6.. |
| `cosmic-ray` | primary | `cosmic-ray==8.7.0` | cosmic-ray 8.7.0 declares Requires-Python >=3.9; pip refuses the pin on 3.6.. |
| `PyDriller` | primary | `pydriller==2.10` | pydriller 2.10 declares Requires-Python >=3.5, so pip installs it without complaint. |
| `Ruff` | alternative | `ruff==0.16.5` | ruff 0.16.5 declares Requires-Python >=3.7; pip refuses the pin on 3.6.. |
| `complexipy` | alternative | `complexipy==7.0.1` | complexipy 7.0.1 declares Requires-Python >=3.8; pip refuses the pin on 3.6.. |
| `symilar (pylint)` | alternative | `pylint==4.0.8` | symilar ships inside pylint 4.0.8 (Requires-Python >=3.10.0); pip refuses the pin on 3.6.. |
| `SlipCover` | alternative | `slipcover==1.1.0` | slipcover 1.1.0 declares Requires-Python >=3.9,<3.15; pip refuses the pin on 3.6.. |
| `mutmut` | alternative | `mutmut==3.7.0` | mutmut 3.7.0 declares Requires-Python >=3.10; pip refuses the pin on 3.6.. |
| `diff-cover` | alternative | `diff-cover==10.5.1` | diff-cover 10.5.1 declares Requires-Python >=3.10; pip refuses the pin on 3.6.. |
| `astroid` | alternative | `astroid==4.3.1` | astroid 4.3.1 declares Requires-Python >=3.10.0; pip refuses the pin on 3.6.. |
| `pyan3 + astroid` | alternative | `pyan3==2.8.1` | pyan3 2.8.1 declares Requires-Python >=3.10,<3.16; pip refuses the pin on 3.6.. |
| `pylint + vulture` | alternative | `vulture==2.16` | vulture 2.16 declares Requires-Python >=3.9; pip refuses the pin on 3.6.. |
| `dulwich` | alternative | `dulwich==1.2.14` | dulwich 1.2.14 declares Requires-Python >=3.10; pip refuses the pin on 3.6.. |

Two of those deserve a second look, because their metadata lies:

| Tool | Declares | Actually |
|---|---|---|
| `lizard` 1.24.0 | **no `Requires-Python` at all** | installs, then `SyntaxError: future feature annotations is not defined` |
| `pydriller` 2.10 | `>=3.5` | installs, then `SyntaxError: invalid syntax` on a walrus operator |

A support matrix built from declared metadata marks both ACTIVE. Both crash.
`dataset.json` records them separately as `toolsInactiveSilent` for exactly
that reason.

## Build

```
make setup        # conda env create -f environment.yml
make install      # conda env update -f environment.yml
```

> `environment.yml` is complete but no solved lock ships with it: conda.anaconda.org and repo.anaconda.com are both 403 at the egress proxy of the host this corpus was built on. Run `conda list --explicit > conda-lock.txt` on a machine with access to close the gap.

## Run

```
python -m orderlab
```



## Test

```
make test         # pytest 7.0.1
make check        # tools/full_check.py -- cross-file consistency audit
```

pytest is pinned at 7.0.1, the last release admitting Python 3.6. It is
infrastructure, not one of the 29 roster tools, and so is exempt from the
latest-only policy: a branch whose tests cannot run is not a branch.

## Workspace layout

```
python-corpus/  (PY_V36_POETRY_CONDA_MONO)
|-- .github/  (1 files)
|-- src/  (20 files)
|-- tests/  (7 files)
|-- tools/  (74 files)
|-- .editorconfig
|-- .gitignore
|-- .python-version
|-- Makefile
|-- dataset.json
|-- environment.yml
|-- pyproject.toml
|-- pytest.ini
|-- requirements-dev.txt
|-- requirements-runtime.txt
|-- requirements.lock
|-- setup.cfg
```

### Monolith

One deployable unit. `src/orderlab` holds the whole domain, and the analysis
fixtures sit alongside it. Untrusted input reaches the code through argv, the
process environment, file contents and public function parameters -- there is
no request object anywhere in this branch, which is the point: a taint engine
that only recognises a web request finds nothing here.


## Tool entry points

Every tool directory carries a `trigger.yaml` recording its pin, its declared
floor, its measured status on this interpreter and what a working run should
find. Run one tool directly, or all of them:

```
bash tools/radon/run_radon.sh
python tools/tool_integration.py --run
python tools/tool_integration.py --verify
```

`--run` distinguishes three outcomes: a tool that ran, a tool that skipped for
a reason `dataset.json` already records, and a tool that skipped for a reason
it does not. Only the third is a finding.

## Planted fixtures

Every tool is pointed at something it should find. Without these, a tool that
ran and reported nothing is indistinguishable from a tool that silently
no-opped.

| Fixture | File | Planted for |
|---|---|---|
| Duplication | [`src/orderlab/services/retail_order_processor.py`](src/orderlab/services/retail_order_processor.py) + [`wholesale_order_processor.py`](src/orderlab/services/wholesale_order_processor.py) | jscpd, symilar |
| Complexity | [`src/orderlab/analysis/complexity_sample.py`](src/orderlab/analysis/complexity_sample.py) | Radon, Lizard, complexipy, cognitive-ast |
| Lint | [`src/orderlab/analysis/lint_violations.py`](src/orderlab/analysis/lint_violations.py) | pylint, Ruff |
| SAST | [`src/orderlab/analysis/sast_fixture.py`](src/orderlab/analysis/sast_fixture.py) | Semgrep + Bandit, Opengrep |
| Taint | [`src/orderlab/analysis/taint_fixture.py`](src/orderlab/analysis/taint_fixture.py) | Opengrep taint mode |
| Dead code | [`src/orderlab/analysis/dead_code.py`](src/orderlab/analysis/dead_code.py) | vulture, pylint |
| Call graph | [`src/orderlab/analysis/call_graph_sample.py`](src/orderlab/analysis/call_graph_sample.py) | pyan3 + astroid, Beniget |
| Vulnerable pins | [`requirements-runtime.txt`](requirements-runtime.txt) | pip-audit, Trivy |

The duplicate pair also co-changes three times in the git history, so a
change-coupling tool and a duplication tool should agree on it.

The five planted pins carry 69 live advisories between them, confirmed against
the PyPI JSON API on 3 September 2026. Every one is genuinely imported by
[`src/orderlab/platform/integrations.py`](src/orderlab/platform/integrations.py) --
a pin nothing imports produces a manifest-versus-source disagreement that looks
like a tool defect and is not.

## History

Roughly 42 synthetic commits, authored as Prajith Kumaravel with three
co-authors carried in `Co-authored-by:` trailers. Measured on this family:
14-20% of commits each, three distinct names. A history tool
that reads only the author field reports one contributor at 100% and is wrong.
The processor pair co-changes three times; the tool runners co-change as a
cluster.

## Machine-readable

[`dataset.json`](dataset.json) carries every branch variable, the full tool
status breakdown with the verbatim reason for each dark tool, and the planted
fixture inventory. It is the answer key: a run is correct when what the tool
platform reports matches what `dataset.json` says should happen, **including
the tools that are supposed to be dark**.
