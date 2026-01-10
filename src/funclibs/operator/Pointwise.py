from __future__ import annotations

from typing import *

from .OperatorABC import OperatorABC

__all__ = ["Pointwise"]


class Pointwise(OperatorABC):

    args: list
    kwargs: dict[str, Any]
    outer: Callable

    __slots__ = ()

    def __call__(self: Self, /, *args: Any, **kwargs: Any) -> Any:
        args_: list
        kwargs_: dict
        x: Any
        y: Any
        args_ = list()
        for y in self._args:
            args_.append(y(*args, **kwargs))
        kwargs_ = dict()
        for x, y in self._kwargs.items():
            kwargs_[x] = y(*args, **kwargs)
        return self._outer(*args_, **kwargs_)
