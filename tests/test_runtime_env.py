"""The Python 3.6 runtime lock.

This branch targets Python 3.6 and nothing else. The assertions below fail on
3.5 and on 3.7+, so a branch that was built or run against the wrong
interpreter says so immediately instead of producing plausible numbers.
"""
import sys


def test_interpreter_is_python_36():
    assert sys.version_info[:2] == (3, 6)


def test_fstrings_are_available():
    # PEP 498, new in 3.6. Fails to parse on 3.5.
    value = 3
    assert f"v{value}" == "v3"


def test_variable_annotations_are_available():
    # PEP 526, new in 3.6.
    total: int = 7
    assert total == 7


def test_dicts_preserve_insertion_order():
    # An implementation detail in 3.6, guaranteed from 3.7 -- true either way.
    seen = {}
    for key in ("c", "a", "b"):
        seen[key] = True
    assert list(seen) == ["c", "a", "b"]


def test_dataclasses_are_not_available():
    # dataclasses landed in 3.7. Its absence is the ceiling half of the lock:
    # this assertion fails on every interpreter above 3.6.
    try:
        import dataclasses  # noqa: F401
    except ImportError:
        return
    raise AssertionError("dataclasses imported -- this is not Python 3.6")


def test_walrus_operator_is_not_available():
    # PEP 572 landed in 3.8. Compiling it must fail here.
    try:
        compile("(x := 1)", "<lock>", "eval")
    except SyntaxError:
        return
    raise AssertionError("walrus compiled -- this is not Python 3.6 or 3.7")
