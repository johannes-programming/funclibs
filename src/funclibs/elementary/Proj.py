from typing import *
from copyable import Copyable
from overloadable import Overloadable
import setdoc
import operator

__all__=["Proj"]

class Proj(Copyable):
    default:Any
    key:int|str
    __slots__ = ("_key", "default")
    def __call__(self:Self, *args:Any, **kwargs:Any) -> Any:
        try:
            if isinstance(self.key, int):
                return args[self.key]
            else:
                return kwargs[self.key]
        except Exception:
            pass
        return self.default
    @Overloadable
    @setdoc.basic
    def __init__(self:Self, *args:Any, **kwargs:Any) -> None:
        return len(args) + len(kwargs) > 1
    @__init__.overload(False)
    @setdoc.basic
    def __init__(self:Self, key:Any) -> None:
        self.key = key
    @__init__.overload(True)
    @setdoc.basic
    def __init__(self:Self, key:Any, default:Any) -> None:
        self.key = key
        self.default = default
    @setdoc.basic
    def copy(self:Self)->Self:
        kwargs:dict[str, Any]
        kwargs=dict[str, Any](key=self.key)
        try:
            kwargs["default"]=self.default
        except AttributeError:
            pass
        return type(self)(**kwargs)
    @property
    def key(self:Self) -> int|str:
        return self._key
    @key.setter
    def key(self:Self, value:Any)->None:
        try:
            self._key = operator.index(value)
        except Exception:
            self._key = str(value)
    

