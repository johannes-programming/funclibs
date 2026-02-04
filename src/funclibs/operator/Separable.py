from __future__ import annotations

from typing import *

from ..abc.Treelike import Treelike

__all__ = ["Separable"]


class Separable(Treelike):

    args: list[Callable]
    kwargs: dict[str, Callable]
    outer: Callable

    __slots__ = ()

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
