from typing import *
from copyable import Copyable
import setdoc


__all__ = ["Const"]

class Const(Copyable):
    value:Any
    __slots__ = ("_value",)

    def __call__(self:Self, *args:Any, **kwargs:Any) -> Any:
        return self._value
    
    @setdoc.basic
    def __init__(self:Self, value:Any = None) -> None:
        self.value = value
    
    @property
    def value(self:Self) -> Any:
        return self._value
    @value.setter
    def value(self:Self, value_:Any) -> None:
        self._value = value_
