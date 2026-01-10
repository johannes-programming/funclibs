from typing import *

import setdoc
from copyable import Copyable

__all__ = ["Const"]


class Const(Copyable):
    value: Any
    __slots__ = ("value",)

    def __call__(self: Self, *args: Any, **kwargs: Any) -> Any:
        return self.value

    @setdoc.basic
    def __init__(self: Self, value: Any = None) -> None:
        self.value = value

    @setdoc.basic
    def copy(self: Self) -> Self:
        return type(self)(self.value)
