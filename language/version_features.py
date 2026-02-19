"""Syntax introduced by Python 3.13. NOT part of the byte-identical domain.

This file exists so the parser-based tools in the roster meet syntax that
`src/` cannot contain -- the domain layer is held to the 3.6 language subset so
it can stay byte-identical across every family in the corpus.

PEP 695 (type parameter syntax) arrived in 3.12. PEP 696 (defaults on type
parameters) and PEP 742 (typing.TypeIs) are new in 3.13. Nothing here is
imported by the domain; it is a target, not a dependency.

Note the GENERIC TYPE ALIAS below. The 3.12 family's fixture had only a
non-generic alias (`type Money = float`), which meant one construct that
triggers beniget's type-parameter bug went unexercised on that family. It is
included here, and the expected count in dataset.json reflects it.
"""
from collections.abc import Iterable
from itertools import batched
from typing import TypeIs, override

type Money = float                              # PEP 695 alias, no type parameter
type Listing[T] = list[T]                       # PEP 695 GENERIC alias


class Box[T = int]:                             # PEP 696: default on a class
    """A generic container. `T` is bound for the whole class body."""

    def __init__(self, item: T) -> None:
        self.item = item

    def get(self) -> T:
        return self.item


class LoudBox[T = int](Box[T]):
    @override                                   # PEP 698
    def get(self) -> T:
        return self.item


def first[T = int](items: Iterable[T]) -> T | None:   # PEP 696 on a function
    for item in items:
        return item
    return None


def is_money(value: object) -> TypeIs[float]:   # PEP 742, new in 3.13
    return isinstance(value, float)


def in_chunks(values: list[int], size: int) -> list[tuple[int, ...]]:
    """itertools.batched arrived in 3.12."""
    return list(batched(values, size))


def describe(rates: dict[str, Money]) -> str:
    """PEP 701: the outer quote character may be reused inside the expression."""
    return f"gold={rates["gold"]}"


def total(prices: list[Money]) -> Money:
    return sum(prices) if prices else 0.0
