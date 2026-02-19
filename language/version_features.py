"""Syntax introduced by Python 3.14. NOT part of the byte-identical domain.

This file exists so the parser-based tools in the roster meet syntax that
`src/` cannot contain -- the domain layer is held to the 3.6 language subset so
it can stay byte-identical across every family in the corpus.

PEP 695 type parameters and PEP 701 f-strings arrived in 3.12; PEP 696 defaults
and PEP 742 TypeIs in 3.13; **PEP 750 template strings** are new in 3.14.

The type-parameter section below covers the FULL PEP 695 construct space:
generic alias, generic class, generic subclass, generic function, and -- new to
this family -- **ParamSpec (`**P`) and TypeVarTuple (`*Ts`) in the new syntax**.
The 3.12 and 3.13 fixtures covered only TypeVar, which left two of the four
parameter kinds unexercised. That gap was recorded as an open item and is
closed here.
"""
from collections.abc import Callable, Iterable
from string.templatelib import Template
from typing import TypeIs, override

type Money = float                              # alias, no type parameter
type Listing[T] = list[T]                       # GENERIC alias


class Box[T = int]:                             # PEP 696 default on a class
    """A generic container. `T` is bound for the whole class body."""

    def __init__(self, item: T) -> None:
        self.item = item

    def get(self) -> T:
        return self.item


class LoudBox[T = int](Box[T]):
    @override                                   # PEP 698
    def get(self) -> T:
        return self.item


def first[T = int](items: Iterable[T]) -> T | None:
    for item in items:
        return item
    return None


def keep_signature[**P, R](fn: Callable[P, R]) -> Callable[P, R]:
    """PEP 695 ParamSpec syntax. Never covered before this family."""
    return fn


def as_tuple[*Ts](items: tuple[*Ts]) -> tuple[*Ts]:
    """PEP 695 TypeVarTuple syntax. Never covered before this family."""
    return items


def is_money(value: object) -> TypeIs[float]:   # PEP 742
    return isinstance(value, float)


def audit_line(order_id: str, total: Money) -> Template:
    """PEP 750, new in 3.14. A t-string evaluates to a Template, not a str."""
    return t"order {order_id} total {total:.2f}"


def render(template: Template) -> str:
    """Templates are iterable: literal strings alternate with Interpolations."""
    parts = []
    for piece in template:
        if isinstance(piece, str):
            parts.append(piece)
        else:
            parts.append(format(piece.value, piece.format_spec))
    return "".join(parts)


def describe(rates: dict[str, Money]) -> str:
    """PEP 701: the outer quote character may be reused inside the expression."""
    return f"gold={rates["gold"]}"


def total(prices: list[Money]) -> Money:
    return sum(prices) if prices else 0.0
