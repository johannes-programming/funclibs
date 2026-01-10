from typing import *
from abc import abstractmethod
from copyable import Copyable
from inspect import Signature, signature


__all__ = ["Freezable"]

class OperatorABC(Copyable):
    __slots__ = ()

    @abstractmethod
    def __call__(self:Self, *args:Any, **kwargs:Any) -> Any:...

    @property
    def __module__(self:Self) -> str:
        return self._outermost().__module__
    
    @property
    def __name__(self:Self) -> str:
        return self._outermost().__name__
    
    @property
    def __qualname__(self:Self) -> str:
        return self._outermost().__qualname__
    
    @property
    def __signature__(self: Self) -> Signature:
        inner : Signature
        outer: Signature
        inner = signature(self._innermost())
        outer = signature(self._outermost())
        return inner.replace(return_annotation=outer.return_annotation)

    @abstractmethod
    def _innermost(self: Self) -> Callable: ...

    @abstractmethod
    def _outermost(self: Self) -> Callable: ...
    
