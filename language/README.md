# language/ -- syntax introduced by this interpreter

**This directory is deliberately NOT byte-identical across families.** Every
other analysable file in this branch is. See `dataset.json`
(`languageFixture`).

`src/` is written to the Python 3.6 language subset so that the same domain
code can be held constant across every family in the corpus. That is what makes
a difference in tool output attributable to the branch variables. The cost is
that the domain can never exercise syntax newer than 3.6, and from the 3.12
family onward that stopped being free.

`version_features.py` carries **PEP 695** type parameters and **PEP 701**
f-strings (3.12), plus **PEP 696** type-parameter defaults and **PEP 742**
`TypeIs` (new here). It is a target for the parser-based tools, and the only
place in the branch where they meet syntax the domain cannot contain.

## What it measures

**`beniget` 0.5.0 is degraded, for the second family running.**

It has 69 visitor methods and none of them handles the `TypeVar` /
`ParamSpec` / `TypeVarTuple` nodes that `gast` 0.7.0 produces for PEP 695 type
parameters. gast parses the syntax correctly -- this is not a parse failure --
but beniget never creates the binding, so every *use* of a type parameter is
reported as a free variable:

```
$ python -m beniget language/version_features.py
W: unbound identifier 'T' at <unknown>:16:29
... 7 in total, all 'T'
```

It writes them to **stdout**, exits **0**, and reports no error. beniget is the
primary tool for the Data Flow metrics, so this is a wrong answer rather than a
missing one -- the failure mode no status check can see, and the reason
`dataset.json` gives this tool `status: "active-degraded"`.

### Tracked across a family boundary

The 3.12 family found this. This family is the first to *re-measure* it, which
was an open item in the build contract:

| Question | Answer |
|---|---|
| Fixed upstream? | **No.** beniget is still 0.5.0; there has been no release. |
| Same on the 3.12 fixture? | **Yes** -- exactly 6, unchanged, on this interpreter. |
| Does PEP 696 deepen it? | **No.** Two files differing only in whether their type parameters carry defaults produce 7 false positives each. |
| Why 7 here and 6 there? | This fixture adds a **generic type alias** (`type Listing[T] = list[T]`), a construct the 3.12 fixture lacked. One more use of `T`, not a new defect. |

**The rule, verified on four fixtures: exactly one false positive per USE of a
type parameter.** 6 uses gives 6; 7 uses gives 7, twice.

The 3.12 build contract predicted this family would be the first chance to
watch a degradation *deepen*. It does not deepen. That prediction is recorded
as corrected rather than quietly dropped.

Every other parser-based tool in the roster handles all of this correctly:
astroid, pylint, ruff, radon, lizard, vulture, bandit, semgrep, complexipy and
pyan3 read the same file without incident.

## Running the tools against it

```
bash tools/beniget/run_beniget.sh      # includes this directory
python tools/tool_integration.py --run
```
