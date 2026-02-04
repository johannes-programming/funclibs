from __future__ import annotations

from abc import abstractmethod
from typing import *

import setdoc
from copyable import Copyable
from cmp3 import CmpABC

__all__ = ["Callable"]


class Callable(Copyable, CmpABC):
    
    __slots__ = ()

    @abstractmethod
    def __call__(self: Self, /, *args: Any, **kwargs: Any) -> Any: ...
    @abstractmethod
    @setdoc.basic
    def __repr__(self: Self) -> str: ...
    