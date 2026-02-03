"""The Python 3.7 runtime lock.

This branch targets Python 3.7 and nothing else. The assertions below fail on
3.6 AND on 3.8+, so a branch built or run against the wrong interpreter says so
immediately instead of producing plausible numbers.

The floor half is what separates this family from the 3.6 one: dataclasses,
contextvars, time.time_ns and PEP 563 postponed annotations all arrive in 3.7.
The ceiling half is unchanged -- the walrus operator is still 3.8.
"""
import sys


def test_interpreter_is_python_37():
    assert sys.version_info[:2] == (3, 7)


# ---- floor: everything below fails on 3.6 -------------------------------------

def test_dataclasses_are_available():
    # PEP 557, new in 3.7. The 3.6 family asserts the OPPOSITE of this.
    import dataclasses

    @dataclasses.dataclass
    class Point:
        x: int
        y: int = 0

    assert Point(1).y == 0


def test_contextvars_is_available():
    # PEP 567, new in 3.7.
    import contextvars
    var = contextvars.ContextVar("tier", default="standard")
    assert var.get() == "standard"


def test_time_ns_is_available():
    # PEP 564, new in 3.7.
    import time
    assert isinstance(time.time_ns(), int)


def test_postponed_annotations_compile():
    # PEP 563, new in 3.7. Fails to compile on 3.6 -- which is exactly why
    # lizard 1.24.0 crashes on the 3.6 family and runs here.
    compile("from __future__ import annotations\nx: Undefined = 1",
            "<lock>", "exec")


def test_module_level_getattr_is_available():
    # PEP 562, new in 3.7.
    import types
    module = types.ModuleType("probe")
    exec("def __getattr__(name):\n    return name.upper()", module.__dict__)
    assert module.__getattr__("tier") == "TIER"


def test_dicts_preserve_insertion_order_by_guarantee():
    # An implementation detail in 3.6; GUARANTEED from 3.7 onward.
    seen = {}
    for key in ("c", "a", "b"):
        seen[key] = True
    assert list(seen) == ["c", "a", "b"]


# ---- ceiling: everything below fails on 3.8+ ----------------------------------

def test_walrus_operator_is_not_available():
    # PEP 572 landed in 3.8. Compiling it must fail here.
    try:
        compile("(x := 1)", "<lock>", "eval")
    except SyntaxError:
        return
    raise AssertionError("walrus compiled -- this is not Python 3.7")


def test_positional_only_parameters_are_not_available():
    # PEP 570 landed in 3.8.
    try:
        compile("def f(a, /, b): pass", "<lock>", "exec")
    except SyntaxError:
        return
    raise AssertionError("positional-only params compiled -- not Python 3.7")


def test_importlib_metadata_is_not_in_the_stdlib():
    # importlib.metadata landed in 3.8.
    try:
        import importlib.metadata  # noqa: F401
    except ImportError:
        return
    raise AssertionError("importlib.metadata imported -- this is not Python 3.7")


def test_math_prod_is_not_available():
    # math.prod landed in 3.8.
    import math
    assert not hasattr(math, "prod")
