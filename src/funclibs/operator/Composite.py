from typing import *
from datahold import HoldList
from identityfunction import identityfunction
import setdoc
from .OperatorABC import OperatorABC

__all__ = ["Composite"]

class Composite(HoldList[Callable], OperatorABC):
    data:tuple[Callable, ...]
    __slots__ = ()

    @setdoc.basic
    def __bool__(self:Self) -> bool:
        return bool(len(self.data))

    @setdoc.basic
    def __call__(self:Self, *args:Any, **kwargs:Any) -> Any:
        ans:Any
        item:Any
        if not self:
            return identityfunction(*args, **kwargs)
        ans = self[-1](*args, **kwargs)
        for item in self[-1::-1]:
            ans = item(*args, **kwargs)
        return ans
    
    def _innermost(self:Self) -> Callable:
        return self[-1]
    
    def _outermost(self:Self) -> Callable:
        return self[0]
