"""The Python 3.9 runtime lock.

Fails on 3.8 AND on 3.10+, so a branch built or run against the wrong
interpreter says so immediately instead of producing plausible numbers.

The floor half is what separates this family from 3.8: PEP 585 builtin
generics, PEP 584 dict union, str.removeprefix, functools.cache and zoneinfo
all arrive in 3.9. PEP 585 in particular is why crosshair-tool works here and
crashed on 3.8 despite declaring >=3.8.
"""
import sys


def test_interpreter_is_python_39():
    assert sys.version_info[:2] == (3, 9)


# ---- floor: everything below fails on 3.8 -------------------------------------

def test_builtin_generics_are_subscriptable():
    # PEP 585, new in 3.9. The 3.8 family asserts the OPPOSITE -- and this is
    # exactly the feature crosshair-tool needs but declares it does not.
    assert list[int] is not None
    assert dict[str, int] is not None
    import collections.abc
    assert collections.abc.Mapping[int, str] is not None


def test_dict_union_operator():
    # PEP 584, new in 3.9.
    merged = {"a": 1} | {"b": 2}
    assert merged == {"a": 1, "b": 2}


def test_removeprefix_and_removesuffix():
    # New str methods in 3.9.
    assert "orderlab-core".removeprefix("orderlab-") == "core"
    assert "orderlab.py".removesuffix(".py") == "orderlab"


def test_functools_cache_is_available():
    # functools.cache, new in 3.9.
    import functools

    @functools.cache
    def double(value):
        return value * 2

    assert double(21) == 42


def test_zoneinfo_is_in_the_stdlib():
    # PEP 615, new in 3.9.
    import zoneinfo
    assert "UTC" in zoneinfo.available_timezones() or True


def test_relaxed_decorator_grammar():
    # PEP 614, new in 3.9: any valid expression may be a decorator.
    compile("buttons = [lambda f: f]\n@buttons[0]\ndef f(): pass",
            "<lock>", "exec")


# ---- ceiling: everything below fails on 3.10+ ---------------------------------

def test_match_statement_is_not_available():
    # PEP 634 structural pattern matching landed in 3.10.
    try:
        compile("match 1:\n    case 1:\n        pass", "<lock>", "exec")
    except SyntaxError:
        return
    raise AssertionError("match compiled -- this is not Python 3.9")


def test_pep604_unions_are_not_available_at_runtime():
    # int | str as a TYPE landed in 3.10.
    try:
        eval("int | str")
    except TypeError:
        return
    raise AssertionError("int | str evaluated -- this is not Python 3.9")


def test_itertools_pairwise_is_not_available():
    # itertools.pairwise landed in 3.10.
    import itertools
    assert not hasattr(itertools, "pairwise")


def test_dataclass_slots_is_not_available():
    # dataclasses slots= landed in 3.10.
    import dataclasses
    try:
        @dataclasses.dataclass(slots=True)
        class Point:
            x: int
    except TypeError:
        return
    raise AssertionError("dataclass(slots=True) accepted -- not Python 3.9")


# NOTE: parenthesized context managers are deliberately NOT asserted against
# here. They are documented as a 3.10 feature, but CPython 3.9's PEG parser
# (PEP 617) already accepts them, so `compile("with (open(a) as f, ...):")`
# succeeds on 3.9 and the obvious ceiling assertion FAILS. Documentation and
# implementation disagree by one minor version -- the same shape as
# crosshair-tool declaring >=3.8 while actually needing 3.9.


def test_encoding_warning_is_not_available():
    # PEP 597 EncodingWarning landed in 3.10.
    import builtins
    assert not hasattr(builtins, "EncodingWarning")


def test_zip_strict_is_not_available():
    # zip(strict=) landed in 3.10.
    try:
        zip([1], [2], strict=True)
    except TypeError:
        return
    raise AssertionError("zip(strict=) accepted -- this is not Python 3.9")
