# orderlab -- PY-004

Order-pricing domain used as a white-box tool-evaluation fixture. One branch of
the Python 3.6 family: 24 branches across 3 build backends, 4 package managers
and 2 architectures. The domain layer is byte-identical on every branch, so any
difference in tool output is attributable to the branch variables alone.

## Branch variables

| Variable | This branch |
|---|---|
| Branch | `PY-004` |
| Python | 3.6.15 |
| Build backend | setuptools 59.6.0 |
| Backend metadata | setup.cfg |
| Package manager | poetry 1.1.15 |
| Architecture | Microservices |
| Scenario | 2 - Microservices |
| Source root | `packages/domain/src` |
| Branch usable | yes |

> **Build backend.** setuptools 59.6.0 -- last release admitting Python 3.6. Predates setuptools 61, so PEP 621 [project] is unsupported and all metadata lives in setup.cfg.

> **Package manager.** poetry 1.1.15 is the last release admitting Python 3.6 (2.4.2 needs >=3.10). Uses the pre-PEP-621 [tool.poetry] table.

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
make setup        # python -m pip install 'poetry==1.1.15'
make install      # poetry install
```

> Both the backend and the package manager on this branch run on Python 3.6.15 for real; the branch installs, locks and tests cleanly.

## Run

```
python -m orderlab
```

Each service is importable on its own:

```
python -c "from gateway_service import health; print(health())"
python -c "from pricing_service import quote; print(quote('gold', 600, 'retail', 'US', 100.0))"
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
python-p36-001-005/  (PY-004)
|-- .github/  (1 files)
|-- packages/  (23 files)
|-- services/  (6 files)
|-- tests/  (7 files)
|-- tools/  (74 files)
|-- .editorconfig
|-- .gitignore
|-- .python-version
|-- Makefile
|-- dataset.json
|-- poetry.toml
|-- pyproject.toml
|-- pytest.ini
|-- requirements-dev.txt
|-- requirements-runtime.txt
|-- setup.cfg
```

### Microservices

Five workspace members. `packages/domain` holds the same byte-identical domain
as the monolith branches; `packages/contracts` holds the wire schema with no
third-party dependency at all, so a service whose own dependencies failed to
install still fails for its own reason. Three services consume both.

`services/gateway_service` is where untrusted input enters. That makes the
microservices branches the mirror image of the monolith ones for taint
analysis: the same domain code, reached through a request envelope rather than
through argv and environment. A tool that scores the two architectures
differently is telling you about its source model, not about the code.


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
| Duplication | [`packages/domain/src/orderlab/services/retail_order_processor.py`](packages/domain/src/orderlab/services/retail_order_processor.py) + [`wholesale_order_processor.py`](packages/domain/src/orderlab/services/wholesale_order_processor.py) | jscpd, symilar |
| Complexity | [`packages/domain/src/orderlab/analysis/complexity_sample.py`](packages/domain/src/orderlab/analysis/complexity_sample.py) | Radon, Lizard, complexipy, cognitive-ast |
| Lint | [`packages/domain/src/orderlab/analysis/lint_violations.py`](packages/domain/src/orderlab/analysis/lint_violations.py) | pylint, Ruff |
| SAST | [`packages/domain/src/orderlab/analysis/sast_fixture.py`](packages/domain/src/orderlab/analysis/sast_fixture.py) | Semgrep + Bandit, Opengrep |
| Taint | [`packages/domain/src/orderlab/analysis/taint_fixture.py`](packages/domain/src/orderlab/analysis/taint_fixture.py) | Opengrep taint mode |
| Dead code | [`packages/domain/src/orderlab/analysis/dead_code.py`](packages/domain/src/orderlab/analysis/dead_code.py) | vulture, pylint |
| Call graph | [`packages/domain/src/orderlab/analysis/call_graph_sample.py`](packages/domain/src/orderlab/analysis/call_graph_sample.py) | pyan3 + astroid, Beniget |
| Vulnerable pins | [`requirements-runtime.txt`](requirements-runtime.txt) | pip-audit, Trivy |

The duplicate pair also co-changes three times in the git history, so a
change-coupling tool and a duplication tool should agree on it.

The five planted pins carry 69 live advisories between them, confirmed against
the PyPI JSON API on 3 September 2026. Every one is genuinely imported by
[`packages/domain/src/orderlab/platform/integrations.py`](packages/domain/src/orderlab/platform/integrations.py) --
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
