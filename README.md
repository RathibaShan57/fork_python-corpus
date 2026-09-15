# orderlab -- PY_V37_UV_UV_MONO

Order-pricing domain used as a white-box tool-evaluation fixture. One branch of
the Python 3.7 family: 24 branches across 3 build backends, 4 package managers
and 2 architectures. The domain layer is byte-identical on every branch, so any
difference in tool output is attributable to the branch variables alone.

## Branch variables

| Variable | This branch |
|---|---|
| Branch | `PY_V37_UV_UV_MONO` |
| Python | 3.7.17 |
| Build backend | uv_build 0.12.9 |
| Backend metadata | pyproject [project] |
| Package manager | uv 0.12.9 |
| Architecture | Monolith |
| Scenario | 1 - Monolithic |
| Source root | `src` |
| Branch usable | **no** -- uv 0. |

> **Build backend.** uv_build 0.12.9 -- MANDATES PEP 621 [project] and requires Python >=3.8. No release has ever admitted 3.7 either, so this backend cannot execute on this branch. Declared, never invoked.

> **Package manager.** uv 0.12.9 REFUSES Python 3.7: "Python 3.7.17 is not supported. Please use Python 3.8 or newer." uv 0.0.5, its first release, already declared >=3.8, and `uv python install 3.7` fails because python-build-standalone's floor is 3.8. Moving the family up one minor version did not help and will not until 3.8.

## Supported tools

29 tools are wired on this branch: 15 primary and 14 alternative, covering the
103-metric white-box framework. **10 of them can run on Python 3.7;
19 cannot.**

That is the measurement, not a defect. Every tool is pinned at its current
latest release, identically on all 24 branches, and the pins that this
interpreter excludes are guarded with an environment marker so they drop out of
resolution instead of failing it. A tool that cannot run exits **3**, not 0 --
a skip that looks like a pass is the failure mode this corpus exists to expose.

### Running here

| Tool | Role | Pin | Why |
|---|---|---|---|
| `Radon` | primary | `radon==6.0.1` | radon 6.0.1 declares no Requires-Python and imports cleanly on 3.7.. |
| `Lizard` | primary | `lizard==1.24.0` | lizard 1.24.0 declares no Requires-Python and, on 3.7, imports and runs. |
| `cognitive-ast` | primary | _binary / stdlib_ | Not a PyPI package -- no distribution of that name exists. |
| `jscpd` | primary | `jscpd@5.1.1` | jscpd 5.1.1 is an npm package that runs on Node, not on the project interpreter, so the Python version is irrelevant to it. |
| `Beniget` | primary | `beniget==0.5.0` | beniget 0.5.0 declares >=3.6 and means it. |
| `Ruff` | alternative | `ruff==0.16.5` | ruff 0.16.5 declares Requires-Python >=3.7, so 3.7 is exactly its floor -- it is refused on the 3.6 family and installs here. |
| `Opengrep` | alternative | _binary / stdlib_ | Standalone binary with its own parser. |
| `Opengrep (taint mode)` | alternative | _binary / stdlib_ | Same binary, taint mode. |
| `Trivy` | alternative | _binary / stdlib_ | Standalone binary; scans manifests and lockfiles, never the interpreter. |
| `sys.settrace driver (stdlib)` | alternative | _binary / stdlib_ | stdlib sys.settrace driver, written 3.6-compatible.. |

### Dark here

| Tool | Role | Pin | Why |
|---|---|---|---|
| `CrossHair` | primary | `crosshair-tool==0.0.110` | crosshair-tool 0.0.110 declares Requires-Python >=3.8; pip refuses the pin on 3.7.. |
| `Coverage.py` | primary | `coverage==7.16.0` | coverage 7.16.0 declares Requires-Python >=3.10; pip refuses the pin on 3.7.. |
| `Pymcdc` | primary | `pymcdc==0.2.6` | pymcdc 0.2.6 declares Requires-Python >=3.10; pip refuses the pin on 3.7.. |
| `testmon` | primary | `pytest-testmon==2.2.0` | pytest-testmon 2.2.0 declares Requires-Python >=3.10; pip refuses the pin on 3.7.. |
| `pylint` | primary | `pylint==4.0.8` | pylint 4.0.8 declares Requires-Python >=3.10.0; pip refuses the pin on 3.7.. |
| `Semgrep OSS` | primary | `semgrep==1.176.0` | semgrep 1.176.0 declares Requires-Python >=3.10; pip refuses the pin on 3.7.. |
| `Bandit` | primary | `bandit==1.9.4` | bandit 1.9.4 declares Requires-Python >=3.10; pip refuses the pin on 3.7.. |
| `pip-audit` | primary | `pip-audit==2.10.1` | pip-audit 2.10.1 declares Requires-Python >=3.10; pip refuses the pin on 3.7.. |
| `cosmic-ray` | primary | `cosmic-ray==8.7.0` | cosmic-ray 8.7.0 declares Requires-Python >=3.9; pip refuses the pin on 3.7.. |
| `PyDriller` | primary | `pydriller==2.10` | pydriller 2.10 declares Requires-Python >=3.5, so pip installs it without complaint. |
| `complexipy` | alternative | `complexipy==7.0.1` | complexipy 7.0.1 declares Requires-Python >=3.8; pip refuses the pin on 3.7.. |
| `symilar (pylint)` | alternative | `pylint==4.0.8` | symilar ships inside pylint 4.0.8 (Requires-Python >=3.10.0); pip refuses the pin on 3.7.. |
| `SlipCover` | alternative | `slipcover==1.1.0` | slipcover 1.1.0 declares Requires-Python >=3.9,<3.15; pip refuses the pin on 3.7.. |
| `mutmut` | alternative | `mutmut==3.7.0` | mutmut 3.7.0 declares Requires-Python >=3.10; pip refuses the pin on 3.7.. |
| `diff-cover` | alternative | `diff-cover==10.5.1` | diff-cover 10.5.1 declares Requires-Python >=3.10; pip refuses the pin on 3.7.. |
| `astroid` | alternative | `astroid==4.3.1` | astroid 4.3.1 declares Requires-Python >=3.10.0; pip refuses the pin on 3.7.. |
| `pyan3 + astroid` | alternative | `pyan3==2.8.1` | pyan3 2.8.1 declares Requires-Python >=3.10,<3.16; pip refuses the pin on 3.7.. |
| `pylint + vulture` | alternative | `vulture==2.16` | vulture 2.16 declares Requires-Python >=3.9; pip refuses the pin on 3.7.. |
| `dulwich` | alternative | `dulwich==1.2.14` | dulwich 1.2.14 declares Requires-Python >=3.10; pip refuses the pin on 3.7.. |

One of those lies about itself:

| Tool | Declares | Actually |
|---|---|---|
| `pydriller` 2.10 | `>=3.5` | installs cleanly, then `SyntaxError: invalid syntax` on a walrus operator at `pydriller/utils/mailmap.py:72` |

A support matrix built from declared metadata marks it ACTIVE. It crashes.
`dataset.json` keeps it in a separate `toolsInactiveSilent` bucket for exactly
that reason.

### What moved since the earlier families

| Tool | On 3.6 | On 3.7 | Why |
|---|---|---|---|
| `ruff` 0.16.5 | refused | **runs** | declares `>=3.7` — 3.7 is exactly its floor. It is the alternative for 19 of the 103 metrics, so this one step restores more cross-checks than anything else between the two families |
| `lizard` 1.24.0 | installed, then crashed | **runs** | `from __future__ import annotations` is legal from 3.7. The pin did not change; the interpreter did |
| `pydriller` 2.10 | crashed | crashes | walrus operator, 3.8+. Unchanged until 3.8 |
| setuptools backend | `setup.cfg` only | **PEP 621 `[project]`** | 68.0.0 is post-setuptools-61; 59.6.0 was not |
| `uv` / `uv_build` | cannot run | cannot run | floor is 3.8. Moving up one minor version did not help |

## Build

```
make setup        # curl -LsSf https://astral.sh/uv/install.sh | sh
make install      # uv sync
```

> **This branch cannot be built.** `uv` refuses Python 3.7.17 before it reaches resolution, and no earlier release admits it either. The configuration above is complete and correct; it is simply unreachable. `uv.lock.MISSING` is committed in place of the lockfile so the absence is explicit rather than looking like an oversight, and `dataset.json` records it as `branchFunctional: false`.

## Run

```
python -m orderlab
```



## Test

```
make test         # pytest 7.4.4
make check        # tools/full_check.py -- cross-file consistency audit
```

pytest is pinned at 7.4.4, the last release admitting Python 3.7. It is
infrastructure, not one of the 29 roster tools, and so is exempt from the
latest-only policy: a branch whose tests cannot run is not a branch.

## Workspace layout

```
python-corpus/  (PY_V37_UV_UV_MONO)
|-- .github/  (1 files)
|-- src/  (20 files)
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
|-- uv.lock.MISSING
|-- uv.toml
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

The five planted pins carry 47 live advisories between them, confirmed against
the PyPI JSON API on 3 September 2026. This family uses the sibling
`python-repos-blueprint`'s canonical set: 3.7 is the first interpreter in this
corpus on which it installs, so unlike the 3.6 family nothing had to be rolled
back. `six` sits beside them in a clearly separated support section — paramiko
2.4.1 imports it without declaring it, and cryptography 42 no longer supplies
it by accident. Every one is genuinely imported by
[`src/orderlab/platform/integrations.py`](src/orderlab/platform/integrations.py) --
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
