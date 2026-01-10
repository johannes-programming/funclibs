from __future__ import annotations

from abc import abstractmethod
from typing import *

import setdoc
from copyable import Copyable
from datarepr import datarepr

__all__ = ["Treelike"]


class Treelike(Copyable):

    args: list
    kwargs: dict[str, Any]
    outer: Callable

    __slots__ = ("_args", "_kwargs", "_outer")

    @abstractmethod
    def __call__(self: Self, /, *args: Any, **kwargs: Any) -> Any: ...

    @setdoc.basic
    def __init__(
        self: Self,
        outer: Callable,
        /,
        *args: Callable,
        **kwargs: Callable,
    ) -> None:
        self._args = list(args)
        self._kwargs = dict(kwargs)
        self._outer = outer

    @setdoc.basic
    def __repr__(self: Self) -> Self:
        return datarepr(type(self).__name__, self.outer, *self.args, **self.kwargs)

    @property
    def args(self: Self) -> list:
        return self._args

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self.outer, *self.args, **self.kwargs)

    @property
    def kwargs(self: Self) -> dict[str, Any]:
        return self._kwargs

    @property
    def outer(self: Self) -> Callable:
        return self._outer
