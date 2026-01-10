from typing import *

import setdoc
from copyable import Copyable

__all__ = ["Const"]

Value = TypeVar("Value")

class Const(Copyable, Generic[Value]):
    value: Value
    __slots__ = ("_value",)

    def __call__(self: Self, *args: Any, **kwargs: Any) -> Any:
        return self.value

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
