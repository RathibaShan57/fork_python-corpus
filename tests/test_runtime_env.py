"""The Python 3.13 runtime lock.

Fails on 3.12 AND on 3.14+, so a branch built or run against the wrong
interpreter says so immediately instead of producing plausible numbers.

Two things separate this family from 3.12, and the second is the larger:

  * PEP 696 gives type parameters DEFAULTS, and PEP 742 adds typing.TypeIs.
    Both are exercised in language/version_features.py.

  * PEP 594 REMOVES SIXTEEN STDLIB MODULES -- the largest deletion in the
    language's history. That is a floor assertion with teeth: any tool or
    dependency still importing one of them dies here. This roster survives it,
    and the two places it could have died are recorded in TRAPS-PY313.md #1.
"""
import importlib
import sys

import pytest


def test_interpreter_is_python_313():
    assert sys.version_info[:2] == (3, 13)


# ---- floor: everything below fails on 3.12 ------------------------------------

def test_pep696_type_parameter_defaults_compile():
    # PEP 696, new in 3.13. The 3.12 family asserts the OPPOSITE.
    namespace = {}
    exec("type Listing[T = int] = list[T]", namespace)
    assert "Listing" in namespace


def test_pep696_default_on_a_generic_class():
    namespace = {}
    exec("class Box[T = int]:\n"
         "    def __init__(self, item: T) -> None:\n"
         "        self.item = item\n", namespace)
    assert namespace["Box"](3).item == 3


def test_typing_typeis_exists():
    # PEP 742, new in 3.13.
    import typing
    assert hasattr(typing, "TypeIs")


def test_copy_replace_exists():
    # copy.replace, new in 3.13.
    import copy
    import dataclasses

    @dataclasses.dataclass
    class Line:
        tier: str
        qty: int

    assert copy.replace(Line("gold", 1), qty=5).qty == 5


def test_warnings_deprecated_exists():
    # PEP 702, new in 3.13.
    import warnings
    assert hasattr(warnings, "deprecated")


def test_os_process_cpu_count_exists():
    # os.process_cpu_count, new in 3.13. The 3.12 family asserts the OPPOSITE --
    # and that slot originally named random.binomialvariate, which is 3.12 and
    # failed on the interpreter it was written for.
    import os
    assert hasattr(os, "process_cpu_count")


def test_glob_translate_exists():
    # glob.translate, new in 3.13.
    import glob
    assert hasattr(glob, "translate")


def test_dbm_sqlite3_exists():
    # dbm.sqlite3, new in 3.13.
    assert importlib.import_module("dbm.sqlite3") is not None


# PEP 594: the sixteen modules deleted in 3.13. This is the largest stdlib
# removal in the language's history, and it is a genuine compatibility cliff --
# anything still importing one of these fails here and nowhere earlier.
PEP_594_REMOVED = [
    "aifc", "audioop", "cgi", "chunk", "crypt", "imghdr", "lib2to3", "mailcap",
    "nntplib", "pipes", "sndhdr", "spwd", "sunau", "telnetlib", "uu", "xdrlib",
]


def test_pep594_modules_are_gone():
    still_here = []
    for name in PEP_594_REMOVED:
        try:
            importlib.import_module(name)
        except ImportError:
            continue
        still_here.append(name)
    assert not still_here, (
        "these PEP 594 modules were removed in 3.13 but are importable: %s"
        % still_here)


def test_the_roster_survives_pep594():
    # The two roster dependencies that DO reference a removed module guard
    # correctly: dill checks `sys.hexversion < 0x30d00a1` before importing
    # xdrlib, and boltons reaches cgi only through an `except ImportError`
    # fallback that never fires. Both are import-time, so importing them
    # proves the guards.
    #
    # SKIPPED rather than failed when the dev requirements are absent. The rest
    # of this file asserts properties of the INTERPRETER and must pass on a bare
    # `pytest` with nothing installed; this one assertion is about installed
    # DEPENDENCIES, and a lock that fails because a package is missing is
    # testing the wrong thing. It is kept here, beside the PEP 594 list, because
    # that is where a reader will look for it.
    pytest.importorskip("dill", reason="cosmic-ray not installed")
    pytest.importorskip("boltons.tableutils", reason="semgrep not installed")


# ---- ceiling: everything below fails on 3.14+ ---------------------------------

def test_pep750_tstrings_do_not_compile():
    # PEP 750 template strings landed in 3.14.
    try:
        compile('greeting = t"hello"', "<lock>", "exec")
    except SyntaxError:
        return
    raise AssertionError("t-strings compiled -- this is not Python 3.13")


def test_annotationlib_is_not_available():
    # PEP 649/749 gave 3.14 an annotationlib module.
    try:
        importlib.import_module("annotationlib")
    except ImportError:
        return
    raise AssertionError("annotationlib imported -- this is not Python 3.13")


def test_compression_namespace_is_not_available():
    # The compression.* namespace (compression.zstd and friends) is 3.14.
    try:
        importlib.import_module("compression")
    except ImportError:
        return
    raise AssertionError("compression imported -- this is not Python 3.13")


def test_concurrent_interpreters_is_not_available():
    # PEP 734 concurrent.interpreters is 3.14.
    try:
        importlib.import_module("concurrent.interpreters")
    except ImportError:
        return
    raise AssertionError("concurrent.interpreters imported -- not Python 3.13")


def test_string_templatelib_is_not_available():
    # string.templatelib accompanies PEP 750 in 3.14.
    import string
    assert not hasattr(string, "templatelib")
