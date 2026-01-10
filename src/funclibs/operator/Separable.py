from typing import *
from .OperatorABC import OperatorABC
from frozendict import frozendict

__all__ = ["Separable"]

class Separable(OperatorABC):
    args:tuple[Callable, ...]
    kwargs:frozendict[str, Callable]
    outer:Callable
    __slots__ = ("_args", "_kwargs", "_outer")
    @property
    def args(self:Self) -> tuple[Callable, ...]:
        return self._args
    @args.setter
    def args(self:Self, value:Iterable[Callable]) -> None:
        self._args = tuple(value)
    @property
    def kwargs(self:Self) -> tuple[Callable, ...]:
        return self._kwargs
    @kwargs.setter
    def kwargs(self:Self, value:Any) -> None:
        frozen:frozendict
        keys:Iterable[str]
        frozen = frozendict(value)
        keys=map(str, frozen.keys())
        self._kwargs = frozendict(zip(keys, frozen.values()))
    

