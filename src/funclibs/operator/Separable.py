from __future__ import annotations

from typing import *

import setdoc
from copyable import Copyable
from datarepr import datarepr

__all__ = ["Separable"]


class Separable(Copyable):

    args: list[Callable]
    kwargs: dict[str, Callable]
    outer: Callable

    __slots__ = ("_args", "_kwargs", "_outer")

    def __call__(self: Self, /, *args: Any, **kwargs: Any) -> Any:
        args_: list
        kwargs_: dict[str, Any]
        x: Any
        y: Any
        args_ = list()
        for x, y in enumerate(args):
            if x < len(self.args):
                args_.append(self.args[x](y))
            else:
                args_.append(y)
        kwargs_ = dict()
        for x, y in kwargs.items():
            if x in self.kwargs.keys():
                kwargs_[x] = self.kwargs[x](y)
            else:
                kwargs_[x] = y
        return self.outer(*args_, **kwargs_)

    @setdoc.basic
    def __init__(
        self: Self,
        outer: Callable,
        /,
        *args: Callable,
        **kwargs: Callable,
    ) -> None:
        self._outer = outer
        self._args = list(args)
        self._kwargs = kwargs

    @setdoc.basic
    def __repr__(self: Self) -> str:
        return datarepr(type(self).__name__, *self.args, **self.kwargs)

    @property
    def args(self: Self) -> list[Callable]:
        return self._args

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self.outer, *self.args, **self.kwargs)

    @property
    def kwargs(self: Self) -> dict[str, Callable]:
        return self._kwargs

    @property
    def outer(self) -> Callable:
        return self._outer

    @outer.setter
    def outer(self: Self, value: Callable) -> None:
        self._outer = value
