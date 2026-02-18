# orderlab -- PY-085

Order-pricing domain used as a white-box tool-evaluation fixture. One branch of
the Python 3.9 family: 24 branches across 3 build backends, 4 package managers
and 2 architectures. The domain layer is byte-identical on every branch, so any
difference in tool output is attributable to the branch variables alone.

## Branch variables

| Variable | This branch |
|---|---|
| Branch | `PY-085` |
| Python | 3.9.23 |
| Build backend | uv_build 0.12.9 |
| Backend metadata | pyproject [project] |
| Package manager | uv 0.12.9 |
| Architecture | Monolith |
| Scenario | 1 - Monolithic |
| Source root | `src` |
| Branch usable | yes |

> **Build backend.** uv_build 0.12.9 -- MANDATES PEP 621 [project] and requires Python >=3.8, comfortably below this family. Runs at the current latest release, not a rolled-back one.

> **Package manager.** uv 0.12.9 runs here at the current latest, not a rollback. Verified in-session: `uv venv` succeeds, `uv pip install` resolves, `uv lock` produces a lockfile, and `uv python install 3.9` installs a managed CPython 3.9.23 in seconds. uv also drives the poetry-core branches on this family, because poetry-core 2.2.1 emits PEP 621 -- the one thing that blocked that pairing on the earlier families.

## Supported tools

29 tools are wired on this branch: 15 primary and 14 alternative, covering the
103-metric white-box framework. **16 of them can run on Python 3.9;
13 cannot.**

That is the measurement, not a defect. Every tool is pinned at its current
latest release, identically on all 24 branches, and the pins that this
interpreter excludes are guarded with an environment marker so they drop out of
resolution instead of failing it. A tool that cannot run exits **3**, not 0 --
a skip that looks like a pass is the failure mode this corpus exists to expose.

### Running here

| Tool | Role | Pin | Why |
|---|---|---|---|
| `CrossHair` | primary | `crosshair-tool==0.0.110` | crosshair-tool 0.0.110 declares >=3.8 but its real floor is 3.9. |
| `Radon` | primary | `radon==6.0.1` | radon 6.0.1 declares no Requires-Python and imports cleanly on 3.8.. |
| `Lizard` | primary | `lizard==1.24.0` | lizard 1.24.0 -- a silent import crash on the 3.6 family, working from 3.7 onward. |
| `cognitive-ast` | primary | _binary / stdlib_ | Not a PyPI package -- no distribution of that name exists. |
| `jscpd` | primary | `jscpd@5.1.1` | jscpd 5.1.1 is an npm package that runs on Node, not on the project interpreter, so the Python version is irrelevant to it. |
| `cosmic-ray` | primary | `cosmic-ray==8.7.0` | cosmic-ray 8.7.0 declares >=3.9. |
| `Beniget` | primary | `beniget==0.5.0` | beniget 0.5.0 declares >=3.6 and means it. |
| `PyDriller` | primary | `pydriller==2.10` | pydriller 2.10 works. |
| `Ruff` | alternative | `ruff==0.16.5` | ruff 0.16.5 -- alternative for 19 of the 103 metrics. |
| `complexipy` | alternative | `complexipy==7.0.1` | complexipy 7.0.1 declares >=3.8. |
| `Opengrep` | alternative | _binary / stdlib_ | Standalone binary with its own parser. |
| `Opengrep (taint mode)` | alternative | _binary / stdlib_ | Same binary, taint mode. |
| `Trivy` | alternative | _binary / stdlib_ | Standalone binary; scans manifests and lockfiles, never the interpreter. |
| `SlipCover` | alternative | `slipcover==1.1.0` | slipcover 1.1.0 declares >=3.9,<3.15. |
| `pylint + vulture` | alternative | `vulture==2.16` | vulture 2.16 declares >=3.9. |
| `sys.settrace driver (stdlib)` | alternative | _binary / stdlib_ | stdlib sys.settrace driver, written 3.6-compatible.. |

### Dark here

| Tool | Role | Pin | Why |
|---|---|---|---|
| `Coverage.py` | primary | `coverage==7.16.0` | coverage 7.16.0 declares Requires-Python >=3.10; pip refuses the pin on 3.9.. |
| `Pymcdc` | primary | `pymcdc==0.2.6` | pymcdc 0.2.6 declares Requires-Python >=3.10; pip refuses the pin on 3.9.. |
| `testmon` | primary | `pytest-testmon==2.2.0` | pytest-testmon 2.2.0 declares Requires-Python >=3.10; pip refuses the pin on 3.9.. |
| `pylint` | primary | `pylint==4.0.8` | pylint 4.0.8 declares Requires-Python >=3.10.0; pip refuses the pin on 3.9.. |
| `Semgrep OSS` | primary | `semgrep==1.176.0` | semgrep 1.176.0 declares Requires-Python >=3.10; pip refuses the pin on 3.9.. |
| `Bandit` | primary | `bandit==1.9.4` | bandit 1.9.4 declares Requires-Python >=3.10; pip refuses the pin on 3.9.. |
| `pip-audit` | primary | `pip-audit==2.10.1` | pip-audit 2.10.1 declares Requires-Python >=3.10; pip refuses the pin on 3.9.. |
| `symilar (pylint)` | alternative | `pylint==4.0.8` | symilar ships inside pylint 4.0.8 (Requires-Python >=3.10.0); pip refuses the pin on 3.9.. |
| `mutmut` | alternative | `mutmut==3.7.0` | mutmut 3.7.0 declares Requires-Python >=3.10; pip refuses the pin on 3.9.. |
| `diff-cover` | alternative | `diff-cover==10.5.1` | diff-cover 10.5.1 declares Requires-Python >=3.10; pip refuses the pin on 3.9.. |
| `astroid` | alternative | `astroid==4.3.1` | astroid 4.3.1 declares Requires-Python >=3.10.0; pip refuses the pin on 3.9.. |
| `pyan3 + astroid` | alternative | `pyan3==2.8.1` | pyan3 2.8.1 declares Requires-Python >=3.10,<3.16; pip refuses the pin on 3.9.. |
| `dulwich` | alternative | `dulwich==1.2.14` | dulwich 1.2.14 declares Requires-Python >=3.10; pip refuses the pin on 3.9.. |

**No tool on this branch lies about itself.** This is the first
family in the corpus where every distribution that installs also imports, and
every one that imports also runs when invoked. `crosshair-tool` declared
`>=3.8` and needed 3.9; the claim and the behaviour agree from here on.

### What moved since the earlier families

| | 3.6 | 3.7 | 3.8 | 3.9 |
|---|---|---|---|---|
| Tools running | 5 | 7 | 12 | **16** |
| Silent liars | 2 | 1 | 1 | **0** |
| Branches that build | 12/24 | 12/24 | 22/24 | **24/24** |
| PEP 621 `[project]` | 0 | 8 | 16 | **24** |

- **All 24 branches build.** poetry-core 2.2.1 emits PEP 621,
  so the poetry-core + uv pairing that failed on 3.8 now locks -- `uv lock`
  resolves 78 packages. The build axis has finished converging.
- **The PEP 621 column is unanimous** for the first time: 0 branches could
  express `[project]` on 3.6, 8 on 3.7, 16 on 3.8, and 24 here.
- **`crosshair`, `cosmic-ray`, `slipcover` and `vulture` arrive.** Mutation
  Score gets a primary for the first time: 336 mutants, 336 killed, 0
  surviving.
- **No tool lies about its support.** crosshair declared `>=3.8` and needed
  3.9; here the claim and the behaviour finally agree.
- **Thirteen tools remain dark**, all declaring `>=3.10`, including Coverage.py
  -- primary for 40 of the 103 metrics. The next family is not an increment.


## Build

```
make setup        # curl -LsSf https://astral.sh/uv/install.sh | sh
make install      # uv sync
```

> uv 0.12.9 drives this branch at the current latest release, not a rolled-back pin. On the 3.8 family a uv branch over a poetry-core backend could not be locked at all, because poetry-core 1.9.1 emits no PEP 621 `[project]` table. poetry-core 2.2.1 does, so every backend on this family is uv-drivable and all 24 branches build — the first family for which that is true.

## Run

```
python -m orderlab
```



## Test

```
make test         # pytest 8.4.2
make check        # tools/full_check.py -- cross-file consistency audit
```

pytest is pinned at 8.4.2, the last release admitting this
interpreter. It is infrastructure, not one of the 29 roster tools, and so is
exempt from the latest-only policy: a branch whose tests cannot run is not a
branch.

## Workspace layout

```
python-p39-083-087/  (PY-085)
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

The five planted pins carry 47 live advisories between them,
confirmed against the PyPI JSON API on 3 September 2026. The set is identical to the three families below it, so the
SCA metrics are directly comparable across all four.

`six` sits beside them in a clearly separated support section — paramiko
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
