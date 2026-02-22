# orderlab -- PY-054

Order-pricing domain used as a white-box tool-evaluation fixture. One branch of
the Python 3.8 family: 24 branches across 3 build backends, 4 package managers
and 2 architectures. The domain layer is byte-identical on every branch, so any
difference in tool output is attributable to the branch variables alone.

## Branch variables

| Variable | This branch |
|---|---|
| Branch | `PY-054` |
| Python | 3.8.18 |
| Build backend | setuptools 75.3.4 |
| Backend metadata | pyproject [project] |
| Package manager | uv 0.12.9 |
| Architecture | Microservices |
| Scenario | 2 - Microservices |
| Source root | `packages/domain/src` |
| Branch usable | yes |

> **Build backend.** setuptools 75.3.4 -- the newest release admitting Python 3.8. Reads PEP 621 [project] natively, so the metadata lives in pyproject.toml and setup.cfg carries only the mutmut and pytest sections. On this family that also makes it uv-compatible, which poetry-core is not.

> **Package manager.** uv 0.12.9 runs here -- 3.8 is exactly its floor, and this is the CURRENT LATEST uv, not a rolled-back one. Verified in-session: `uv venv --python 3.8` succeeds, `uv pip install` resolves, `uv lock` produces a lockfile, and `uv python install 3.8` installs a managed CPython 3.8.20. After two families in which this axis was entirely dark, it is live. NOTE: uv requires a PEP 621 [project] table, so it cannot drive a poetry-core branch.

## Supported tools

29 tools are wired on this branch: 15 primary and 14 alternative, covering the
103-metric white-box framework. **12 of them can run on Python 3.8;
17 cannot.**

That is the measurement, not a defect. Every tool is pinned at its current
latest release, identically on all 24 branches, and the pins that this
interpreter excludes are guarded with an environment marker so they drop out of
resolution instead of failing it. A tool that cannot run exits **3**, not 0 --
a skip that looks like a pass is the failure mode this corpus exists to expose.

### Running here

| Tool | Role | Pin | Why |
|---|---|---|---|
| `Radon` | primary | `radon==6.0.1` | radon 6.0.1 declares no Requires-Python and imports cleanly on 3.8.. |
| `Lizard` | primary | `lizard==1.24.0` | lizard 1.24.0 -- a silent import crash on the 3.6 family, working from 3.7 onward. |
| `cognitive-ast` | primary | _binary / stdlib_ | Not a PyPI package -- no distribution of that name exists. |
| `jscpd` | primary | `jscpd@5.1.1` | jscpd 5.1.1 is an npm package that runs on Node, not on the project interpreter, so the Python version is irrelevant to it. |
| `Beniget` | primary | `beniget==0.5.0` | beniget 0.5.0 declares >=3.6 and means it. |
| `PyDriller` | primary | `pydriller==2.10` | pydriller 2.10 finally works. |
| `Ruff` | alternative | `ruff==0.16.5` | ruff 0.16.5 -- alternative for 19 of the 103 metrics. |
| `complexipy` | alternative | `complexipy==7.0.1` | complexipy 7.0.1 declares >=3.8. |
| `Opengrep` | alternative | _binary / stdlib_ | Standalone binary with its own parser. |
| `Opengrep (taint mode)` | alternative | _binary / stdlib_ | Same binary, taint mode. |
| `Trivy` | alternative | _binary / stdlib_ | Standalone binary; scans manifests and lockfiles, never the interpreter. |
| `sys.settrace driver (stdlib)` | alternative | _binary / stdlib_ | stdlib sys.settrace driver, written 3.6-compatible.. |

### Dark here

| Tool | Role | Pin | Why |
|---|---|---|---|
| `CrossHair` | primary | `crosshair-tool==0.0.110` | crosshair-tool 0.0.110 declares Requires-Python >=3.8, pip installs it, AND `import crosshair` succeeds -- and then the tool dies the moment it is invoked: crosshair/libimpl/builtinslib.py line 3860 subscripts collections.abc.Mapping, which is PEP 585 and therefore 3.9+, raising TypeError: 'ABCMeta' object is not subscriptable. |
| `Coverage.py` | primary | `coverage==7.16.0` | coverage 7.16.0 declares Requires-Python >=3.10; pip refuses the pin on 3.8.. |
| `Pymcdc` | primary | `pymcdc==0.2.6` | pymcdc 0.2.6 declares Requires-Python >=3.10; pip refuses the pin on 3.8.. |
| `testmon` | primary | `pytest-testmon==2.2.0` | pytest-testmon 2.2.0 declares Requires-Python >=3.10; pip refuses the pin on 3.8.. |
| `pylint` | primary | `pylint==4.0.8` | pylint 4.0.8 declares Requires-Python >=3.10.0; pip refuses the pin on 3.8.. |
| `Semgrep OSS` | primary | `semgrep==1.176.0` | semgrep 1.176.0 declares Requires-Python >=3.10; pip refuses the pin on 3.8.. |
| `Bandit` | primary | `bandit==1.9.4` | bandit 1.9.4 declares Requires-Python >=3.10; pip refuses the pin on 3.8.. |
| `pip-audit` | primary | `pip-audit==2.10.1` | pip-audit 2.10.1 declares Requires-Python >=3.10; pip refuses the pin on 3.8.. |
| `cosmic-ray` | primary | `cosmic-ray==8.7.0` | cosmic-ray 8.7.0 declares Requires-Python >=3.9; pip refuses the pin on 3.8.. |
| `symilar (pylint)` | alternative | `pylint==4.0.8` | symilar ships inside pylint 4.0.8 (Requires-Python >=3.10.0); pip refuses the pin on 3.8.. |
| `SlipCover` | alternative | `slipcover==1.1.0` | slipcover 1.1.0 declares Requires-Python >=3.9,<3.15; pip refuses the pin on 3.8.. |
| `mutmut` | alternative | `mutmut==3.7.0` | mutmut 3.7.0 declares Requires-Python >=3.10; pip refuses the pin on 3.8.. |
| `diff-cover` | alternative | `diff-cover==10.5.1` | diff-cover 10.5.1 declares Requires-Python >=3.10; pip refuses the pin on 3.8.. |
| `astroid` | alternative | `astroid==4.3.1` | astroid 4.3.1 declares Requires-Python >=3.10.0; pip refuses the pin on 3.8.. |
| `pyan3 + astroid` | alternative | `pyan3==2.8.1` | pyan3 2.8.1 declares Requires-Python >=3.10,<3.16; pip refuses the pin on 3.8.. |
| `pylint + vulture` | alternative | `vulture==2.16` | vulture 2.16 declares Requires-Python >=3.9; pip refuses the pin on 3.8.. |
| `dulwich` | alternative | `dulwich==1.2.14` | dulwich 1.2.14 declares Requires-Python >=3.10; pip refuses the pin on 3.8.. |

**One tool on this branch lies about itself, and it lies one
level deeper than any before it.** `crosshair-tool` 0.0.110 declares `>=3.8`,
installs cleanly and `import crosshair` succeeds -- then the tool dies when
invoked, with `TypeError: 'ABCMeta' object is not subscriptable`, because it
subscripts `collections.abc.Mapping` and PEP 585 is 3.9. Declared support is a
claim, an import is better evidence, and only invoking the tool is the fact.

### What moved since the earlier families

| | 3.6 | 3.7 | 3.8 |
|---|---|---|---|
| Tools running | 5 | 7 | **12** |
| Silent liars | 2 | 1 | **1** |
| Branches that build | 12/24 | 12/24 | **22/24** |
| PEP 621 `[project]` | 0 | 8 | **16** |
| `uv` | refused | refused | **works, at latest** |

- **`uv` reaches its floor.** 3.8 is exactly it, for the tool
  and for python-build-standalone alike. The uv branches are the only ones in
  the corpus running their package manager at the current latest release.
- **`pydriller` works**, so Code Churn has a primary for the first time: it
  crashed on a walrus operator on both earlier families, and the walrus is 3.8.
- **`crosshair` and `complexipy`** both declare `>=3.8`. complexipy gives the
  seven Cognitive Complexity metrics their first cross-check; crosshair
  installs and imports but dies on invocation, which is the corpus's clearest
  example of why a status is measured by running a tool and not by importing it.
- **Two branches still cannot be locked**, and it is worth being precise about
  why: uv requires PEP 621, poetry-core 1.9.1 writes `[tool.poetry]`, and
  neither is broken. That is a metadata-shape incompatibility, not an
  interpreter floor -- a different class of finding from the previous
  families.


## Build

```
make setup        # curl -LsSf https://astral.sh/uv/install.sh | sh
make install      # uv sync
```

> Both halves run on Python 3.8.18 for real, and this is the **first family in the corpus where a uv branch works at all** — 3.8 is exactly uv's floor. It is also the only branch type running its package manager at the current latest release rather than a rolled-back one: uv 0.12.9, not a 2023 pin.

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
make test         # pytest 8.3.5
make check        # tools/full_check.py -- cross-file consistency audit
```

pytest is pinned at 8.3.5, the last release admitting this
interpreter. It is infrastructure, not one of the 29 roster tools, and so is
exempt from the latest-only policy: a branch whose tests cannot run is not a
branch.

## Workspace layout

```
python-p38-054-058/  (PY-054)
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
|-- pyproject.toml
|-- pytest.ini
|-- requirements-dev.txt
|-- requirements-runtime.txt
|-- setup.cfg
|-- uv.toml
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

The five planted pins carry 47 live advisories between them,
confirmed against the PyPI JSON API on 3 September 2026. The set is identical to the 3.6 and 3.7 families', so the
SCA metrics are directly comparable across all three.

`six` sits beside them in a clearly separated support section — paramiko
2.4.1 imports it without declaring it, and cryptography 42 no longer supplies
it by accident. Every one is genuinely imported by
[`packages/domain/src/orderlab/platform/integrations.py`](packages/domain/src/orderlab/platform/integrations.py) --
a pin nothing imports produces a manifest-versus-source disagreement that looks
like a tool defect and is not.

## History

Roughly 45 synthetic commits, authored as Prajith Kumaravel with three
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
