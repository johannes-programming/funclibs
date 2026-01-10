import unittest
from types import FunctionType
from typing import *

from funclibs.operator.Pointwise import Pointwise


class TestPointwise(unittest.TestCase):
    def test_example_transformation(self: Self) -> None:
        def o(*args: Any, **kwargs: Any) -> tuple[str, tuple, dict[str, Any]]:
            return ("O", args, kwargs)

        def a(*args: Any, **kwargs: Any) -> tuple[str, tuple, dict[str, Any]]:
            return ("A", args, kwargs)

        def b(*args: Any, **kwargs: Any) -> tuple[str, tuple, dict[str, Any]]:
            return ("B", args, kwargs)

        def c(*args: Any, **kwargs: Any) -> tuple[str, tuple, dict[str, Any]]:
            return ("C", args, kwargs)

        p: Pointwise
        got: Any
        expected: Any

        p = Pointwise(o, a, b, foo=c)
        got = p(1, 2, 3, bar=4, baz=6)
        expected = o(
            a(1, 2, 3, bar=4, baz=6),
            b(1, 2, 3, bar=4, baz=6),
            foo=c(1, 2, 3, bar=4, baz=6),
        )

        self.assertEqual(got, expected)

    def test_no_inner_functions_calls_outer_with_no_args_kwargs(self: Self) -> None:
        def o(*args: Any, **kwargs: Any) -> tuple[str, dict[str, Any]]:
            return (args, kwargs)

        p: Pointwise
        p = Pointwise(o)
        self.assertEqual(p(1, 2, x=3), o())

    def test_calls_each_inner_exactly_once_with_same_inputs(self: Self) -> None:
        a: Any
        b: Any
        c: Any
        calls: list
        p: Pointwise
        got: Any
        calls = []

        def mk(tag: Any) -> FunctionType:
            def f(*args: Any, **kwargs: Any) -> Any:
                calls.append((tag, args, dict(kwargs)))
                return tag

            return f

        def o(*args: Any, **kwargs: Any) -> tuple[tuple, dict[str, Any]]:
            return (args, kwargs)

        a = mk("a")
        b = mk("b")
        c = mk("c")
        p = Pointwise(o, a, b, foo=c)
        got = p(10, 20, k=30)

        self.assertEqual(got, o("a", "b", foo="c"))
        self.assertEqual(
            calls,
            [
                ("a", (10, 20), {"k": 30}),
                ("b", (10, 20), {"k": 30}),
                ("c", (10, 20), {"k": 30}),
            ],
        )

    def test_preserves_outer_keyword_names(self: Self) -> None:
        def o(*args: Any, **kwargs: Any) -> dict[str, Any]:
            return kwargs

        def c(*args: Any, **kwargs: Any) -> str:
            return "computed"

        p: Pointwise
        p = Pointwise(o, foo=c, bar=c)
        self.assertEqual(p(1, 2, x=3), {"foo": "computed", "bar": "computed"})


if __name__ == "__main__":
    unittest.main()
