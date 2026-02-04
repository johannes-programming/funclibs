from typing import *

import setdoc
from funclibs.abc.Callable import Callable

__all__ = ["Const"]

Value = TypeVar("Value")


class Const(Callable, Generic[Value]):
    value: Value
    __slots__ = ("_value",)

    def __call__(self: Self, *args: Any, **kwargs: Any) -> Any:
        return self.value
    
    @setdoc.basic
    def __cmp__(self:Self, other:Any) -> Optional[int]:
        if type(self) is not type(other):
            return
        try:
            if (self.value<=other.value)and(other.value<=self.value):
                return 0
            if (not self.value<=other.value)and(other.value<=self.value):
                return 1
            if (self.value<=other.value)and(not other.value<=self.value):
                return -1
        except Exception:
            if self.value==other.value:
                return 0
        return float("nan")

    @setdoc.basic
    def __init__(self: Self, value: Value = None) -> None:
        self.value = value

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self.value)

    @property
    def value(self: Self) -> Value:
        return self._value

    @value.setter
    def value(self: Self, value_: Value) -> None:
        self._value = value_
