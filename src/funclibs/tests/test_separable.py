import unittest
from typing import *

from funclibs.operator.Separable import Separable


class TestSeparable(unittest.TestCase):
    def test_example_transformation(self: Self) -> None:
        def o(*args: Any, **kwargs: Any) -> tuple:
            return ("O", args, kwargs)

        def a(x: Any) -> tuple[str, Any]:
            return ("A", x)

        def b(x: Any) -> tuple[str, Any]:
            return ("B", x)

        def c(x: Any) -> tuple[str, Any]:
            return ("C", x)

        s: Separable
        got: Any
        expected: Any

        s = Separable(o, a, b, foo=c)

        got = s(1, 2, 3, bar=4, foo=5, baz=6)
        expected = o(a(1), b(2), 3, bar=4, foo=c(5), baz=6)

        self.assertEqual(got, expected)

    def test_no_positional_transformers(self: Self) -> None:
        def o(*args: Any, **kwargs: Any) -> tuple[tuple, dict[str, Any]]:
            return (args, kwargs)

        s: Separable
        s = Separable(o)
        self.assertEqual(s(1, 2, x=3), o(1, 2, x=3))

    def test_positional_transformers_only_apply_to_existing_args(self: Self) -> None:
        calls: list
        s: Separable
        got: Any
        calls = []

        def o(*args: Any, **kwargs: Any) -> tuple[tuple, dict[str, Any]]:
            return (args, kwargs)

        def t(x: Any) -> Any:
            calls.append(x)
            return x * 10

        s = Separable(o, t, t, t)  # more transformers than args passed
        got = s(1)  # only first transformer should be used
        self.assertEqual(got, o(10))
        self.assertEqual(calls, [1])

    def test_keyword_transformers_only_apply_when_key_present(self: Self) -> None:
        def o(*args: Any, **kwargs: Any) -> tuple[tuple, dict[str, Any]]:
            return (args, kwargs)

        def kwt(x: Any) -> Any:
            return x + 1

        s: Separable

        s = Separable(o, foo=kwt, bar=kwt)
        self.assertEqual(s(1, foo=10), o(1, foo=11))
        self.assertEqual(s(1, baz=10), o(1, baz=10))

    def test_transforms_do_not_mutate_input_kwargs_dict(self: Self) -> None:
        def o(*args: Any, **kwargs: Any) -> dict[str, Any]:
            return kwargs

        def inc(x: Any) -> Any:
            return x + 1

        s: Separable
        kw: dict
        out: Any

        s = Separable(o, foo=inc)

        kw = {"foo": 1, "bar": 2}
        out = s(**kw)
        self.assertEqual(out, {"foo": 2, "bar": 2})
        self.assertEqual(kw, {"foo": 1, "bar": 2})  # original unchanged

    def test_repr_is_string(self: Self) -> None:
        def o(x: Any) -> Any:
            return x

        s: Separable
        r: str
        s = Separable(o)
        r = repr(s)
        self.assertIsInstance(r, str)
        self.assertTrue(len(r) > 0)

    def test_copy_produces_equivalent_callable(self: Self) -> None:
        def o(*args: Any, **kwargs: Any) -> tuple[tuple, dict[str, Any]]:
            return (args, kwargs)

        def a(x: Any) -> Any:
            return x * 2

        s1: Separable
        s2: Separable

        s1 = Separable(o, a, foo=a)
        s2 = s1.copy()

        self.assertIsNot(s1, s2)
        self.assertEqual(s1(3, foo=4), s2(3, foo=4))
        self.assertEqual(s1(3, 5, foo=4), s2(3, 5, foo=4))


if __name__ == "__main__":
    unittest.main()
