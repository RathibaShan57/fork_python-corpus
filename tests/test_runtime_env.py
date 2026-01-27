"""The Python 3.8 runtime lock.

Fails on 3.7 AND on 3.9+, so a branch built or run against the wrong
interpreter says so immediately instead of producing plausible numbers.

The floor half is what separates this family from 3.7: the walrus operator,
positional-only parameters, importlib.metadata, math.prod, typing.TypedDict and
functools.cached_property all arrive in 3.8. The walrus in particular is why
PyDriller works here and crashed on both earlier families.
"""
import sys


def test_interpreter_is_python_38():
    assert sys.version_info[:2] == (3, 8)


# ---- floor: everything below fails on 3.7 -------------------------------------

def test_walrus_operator_is_available():
    # PEP 572, new in 3.8. Both earlier families assert the OPPOSITE, and this
    # single statement is why pydriller could not be imported on either.
    values = [1, 2, 3, 4]
    assert (total := sum(values)) == 10
    assert total == 10


def test_positional_only_parameters_are_available():
    # PEP 570, new in 3.8.
    namespace = {}
    exec("def f(a, /, b):\n    return a + b", namespace)
    assert namespace["f"](1, b=2) == 3


def test_importlib_metadata_is_in_the_stdlib():
    # New in 3.8; a backport package on every earlier version.
    import importlib.metadata
    assert hasattr(importlib.metadata, "version")


def test_math_prod_is_available():
    # New in 3.8.
    import math
    assert math.prod([2, 3, 4]) == 24


def test_typed_dict_and_literal_are_in_typing():
    # PEP 589 and PEP 586, both new in typing at 3.8.
    import typing
    assert hasattr(typing, "TypedDict")
    assert hasattr(typing, "Literal")
    assert hasattr(typing, "Final")


def test_cached_property_is_available():
    # New in functools at 3.8.
    import functools
    assert hasattr(functools, "cached_property")


def test_fstring_equals_specifier():
    # PEP 572-adjacent f-string `=` form, new in 3.8.
    tier = "gold"
    assert eval('f"{tier=}"') == "tier='gold'"


# ---- ceiling: everything below fails on 3.9+ ----------------------------------

def test_dict_union_operator_is_not_available():
    # PEP 584 landed in 3.9.
    try:
        eval("{'a': 1} | {'b': 2}")
    except TypeError:
        return
    raise AssertionError("dict | dict worked -- this is not Python 3.8")


def test_removeprefix_is_not_available():
    # str.removeprefix landed in 3.9.
    assert not hasattr("orderlab", "removeprefix")


def test_functools_cache_is_not_available():
    # functools.cache landed in 3.9 (lru_cache has been there since 3.2).
    import functools
    assert not hasattr(functools, "cache")


def test_zoneinfo_is_not_in_the_stdlib():
    # PEP 615 landed in 3.9.
    try:
        import zoneinfo  # noqa: F401
    except ImportError:
        return
    raise AssertionError("zoneinfo imported -- this is not Python 3.8")


def test_builtin_generics_are_not_subscriptable():
    # PEP 585 landed in 3.9. list[int] raises TypeError at runtime here.
    try:
        eval("list[int]")
    except TypeError:
        return
    raise AssertionError("list[int] evaluated -- this is not Python 3.8")
