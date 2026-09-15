# orderlab -- PY_V313_UV_POETRY_MICRO

Order-pricing domain used as a white-box tool-evaluation fixture. One branch of
the Python 3.13 family: 24 branches across 3 build backends, 4 package managers
and 2 architectures. The domain layer is byte-identical on every branch, so any
difference in tool output is attributable to the branch variables alone.

## Branch variables

| Variable | This branch |
|---|---|
| Branch | `PY_V313_UV_POETRY_MICRO` |
| Python | 3.13.7 |
| Build backend | uv_build 0.12.9 |
| Backend metadata | pyproject [project] |
| Package manager | poetry 2.4.2 |
| Architecture | Microservices |
| Scenario | 2 - Microservices |
| Source root | `packages/domain/src` |
| Branch usable | yes |

> **Build backend.** uv_build 0.12.9 -- MANDATES PEP 621 [project] and requires Python >=3.8, comfortably below this family. Runs at the current latest release, not a rolled-back one.

> **Package manager.** poetry 2.4.2 -- the current latest release. On the 2.x line it reads and writes PEP 621 [project]; the [tool.poetry] table it still accepts is a compatibility path, not the source of truth.

## Supported tools

29 tools are wired on this branch: 15 primary and 14 alternative, covering the
103-metric white-box framework. **29 of them can run on Python 3.13;
0 cannot.**

That is the measurement, not a defect. Every tool is pinned at its current
latest release, identically on all 24 branches, and the pins that this
interpreter excludes are guarded with an environment marker so they drop out of
resolution instead of failing it. A tool that cannot run exits **3**, not 0 --
a skip that looks like a pass is the failure mode this corpus exists to expose.

### Running here

| Tool | Role | Pin | Why |
|---|---|---|---|
| `CrossHair` | primary | `crosshair-tool==0.0.110` | crosshair-tool 0.0.110 declares >=3.8 but its real floor is 3.9. |
| `Coverage.py` | primary | `coverage==7.16.0` | Coverage.py 7.16.0 declares >=3.10. |
| `Pymcdc` | primary | `pymcdc==0.2.6` | pymcdc 0.2.6 declares >=3.10. |
| `Radon` | primary | `radon==6.0.1` | radon 6.0.1 declares no Requires-Python and imports cleanly on 3.8.. |
| `Lizard` | primary | `lizard==1.24.0` | lizard 1.24.0 -- a silent import crash on the 3.6 family, working from 3.7 onward. |
| `testmon` | primary | `pytest-testmon==2.2.0` | pytest-testmon 2.2.0 declares >=3.10. |
| `cognitive-ast` | primary | _binary / stdlib_ | Not a PyPI package -- no distribution of that name exists. |
| `jscpd` | primary | `jscpd@5.1.1` | jscpd 5.1.1 is an npm package that runs on Node, not on the project interpreter, so the Python version is irrelevant to it. |
| `pylint` | primary | `pylint==4.0.8` | pylint 4.0.8 declares >=3.10. |
| `Semgrep OSS` | primary | `semgrep==1.176.0` | semgrep 1.176.0 declares >=3.10, and bandit 1.9.4 with it. |
| `Bandit` | primary | `bandit==1.9.4` | bandit 1.9.4 declares >=3.10. |
| `pip-audit` | primary | `pip-audit==2.10.1` | pip-audit 2.10.1 declares >=3.10. |
| `cosmic-ray` | primary | `cosmic-ray==8.7.0` | cosmic-ray 8.7.0 declares >=3.9. |
| `Beniget` | primary | `beniget==0.5.0` | beniget 0.5.0 declares >=3.6 and means it. |
| `PyDriller` | primary | `pydriller==2.11` | pydriller 2.11 works. |
| `Ruff` | alternative | `ruff==0.16.6` | ruff 0.16.6 -- alternative for 19 of the 103 metrics. |
| `complexipy` | alternative | `complexipy==8.0.0` | complexipy 8.0.0 declares >=3.8. |
| `symilar (pylint)` | alternative | `pylint==4.0.8` | symilar ships inside pylint 4.0.8, so it arrives with it. |
| `Opengrep` | alternative | _binary / stdlib_ | Standalone binary with its own parser. |
| `Opengrep (taint mode)` | alternative | _binary / stdlib_ | Same binary, taint mode. |
| `Trivy` | alternative | _binary / stdlib_ | Standalone binary; scans manifests and lockfiles, never the interpreter. |
| `SlipCover` | alternative | `slipcover==1.1.0` | slipcover 1.1.0 declares >=3.9,<3.15. |
| `mutmut` | alternative | `mutmut==3.7.0` | mutmut 3.7.0 declares >=3.10. |
| `diff-cover` | alternative | `diff-cover==10.5.1` | diff-cover 10.5.1 declares >=3.10. |
| `astroid` | alternative | `astroid==4.0.4` | astroid 4.0.4, NOT the latest 4.3.1 -- and this is the one place in the corpus where the latest-everywhere policy had to yield. |
| `pyan3 + astroid` | alternative | `pyan3==2.8.1` | pyan3 2.8.1 declares >=3.10,<3.16. |
| `pylint + vulture` | alternative | `vulture==2.16` | vulture 2.16 declares >=3.9. |
| `dulwich` | alternative | `dulwich==1.2.14` | dulwich 1.2.14 declares >=3.10. |
| `sys.settrace driver (stdlib)` | alternative | _binary / stdlib_ | stdlib sys.settrace driver, written 3.6-compatible.. |

### Dark here

_(none)_

**No tool on this branch lies about its own support, and one still
lies about its results.** `beniget` 0.5.0 installs, imports, runs, exits 0 and
reports every use of a PEP 695 type parameter as an unbound identifier -- for
the second family running, with no upstream fix available. `dataset.json`
records it as `active-degraded` and carries the expected count so a checker can
assert it. What is new here is that the degradation has now been *tracked*
across a family boundary rather than merely found: unchanged in kind, unchanged
in severity, and explicitly not deepened by PEP 696.

### What moved since the earlier families

| | 3.6 | 3.7 | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 | 3.13 |
|---|---|---|---|---|---|---|---|---|
| Tools running | 5 | 7 | 12 | 16 | 29 | 29 | 29 | **29** |
| Silent liars | 2 | 1 | 1 | 0 | 0 | 0 | 0 | **0** |
| Degraded (runs, wrong) | 0 | 0 | 0 | 0 | 0 | 0 | 1 | **1** |
| Branches that build | 12/24 | 12/24 | 22/24 | 24/24 | 24/24 | 24/24 | 24/24 | **24/24** |
| PEP 621 `[project]` | 0 | 8 | 16 | 24 | 24 | 24 | 24 | **24** |
| Infra pins at latest | none | none | uv | uv, wheel | all 7 | all 7 | all 7 | **all 7** |
| stdlib modules removed | — | — | — | — | — | — | 0 | **16** |

- **PEP 594 removes sixteen stdlib modules**, and nothing in the
  roster breaks. `dill` (a cosmic-ray dependency) guards its `xdrlib` import
  with an explicit `sys.hexversion < 0x30d00a1` check; `boltons` (a semgrep
  dependency) reaches `cgi` only through an `except ImportError` fallback that
  never fires. The largest compatibility cliff in the language's history, and
  the roster crosses it without a scratch.
- **One tool pin moved:** `pydriller` 2.10 to 2.11. Re-resolved live, as the
  policy requires; nothing about 3.13 excluded 2.10.
- **beniget is still degraded, and measurably no worse.** Still 0.5.0 upstream
  -- no release since -- and the 3.12 family's own fixture still yields exactly
  6 false positives on this interpreter. This family's fixture yields 7 only
  because it adds a generic type alias, a construct 3.12's fixture lacked.
- **PEP 696 defaults do NOT deepen the degradation.** Two files differing only
  in whether their type parameters carry defaults produce 7 false positives
  each. The 3.12 contract predicted this family would be the first chance to
  watch a degradation deepen across a family boundary. It does not deepen: the
  count tracks uses of the type parameter, not the syntax variant.
- **`language/` grows PEP 696 and PEP 742**, and gains the generic type alias
  the 3.12 fixture was missing.

## Build

```
make setup        # python -m pip install 'poetry==2.4.2'
make install      # poetry install
```

> Both the backend and the package manager on this branch run on Python 3.13.7 for real; the branch installs, locks and tests cleanly.

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
make test         # pytest 9.1.1
make check        # tools/full_check.py -- cross-file consistency audit
```

pytest is pinned at 9.1.1, which is its current latest
release -- on this family the infrastructure pins cost nothing. It is
infrastructure, not one of the 29 roster tools, and so is exempt from the
latest-only policy either way: a branch whose tests cannot run is not a
branch.

## Workspace layout

```
python-corpus/  (PY_V313_UV_POETRY_MICRO)
|-- .github/  (1 files)
|-- language/  (2 files)
|-- packages/  (23 files)
|-- services/  (6 files)
|-- tests/  (7 files)
|-- tools/  (76 files)
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

The five planted pins carry 45 live advisories between them,
confirmed against the PyPI JSON API on 3 September 2026. The planted set is unchanged from 3.10 onward -- `urllib3`
2.2.2 and `paramiko` 2.10.1, both moved at 3.10 for reasons unrelated to the
interpreter -- so the SCA metrics are directly comparable across those four
families.

`six` sits beside them in a clearly separated support section — paramiko
2.10.1 imports it without declaring it, and cryptography 42 no
longer supplies it by accident. Every one is genuinely imported by
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
