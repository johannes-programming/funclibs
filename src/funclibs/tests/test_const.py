import unittest
from typing import *

from funclibs.elementary.Const import Const


class TestConst(unittest.TestCase):
    def test_init_default_value_is_none(self: Self) -> None:
        c: Const
        c = Const()
        self.assertIsNone(c.value)
        self.assertIs(c(), None)

    def test_init_sets_value(self: Self) -> None:
        c: Const
        c = Const(123)
        self.assertEqual(c.value, 123)
        self.assertEqual(c(), 123)

    def test_call_ignores_args_and_kwargs(self: Self) -> None:
        c: Const
        c = Const("x")
        self.assertEqual(c(1, 2, 3, a=4, b=5), "x")

    def test_copy_returns_new_instance_same_type(self: Self) -> None:
        c: Const
        ref: Const
        c = Const(10)
        ref = c.copy()
        self.assertIsInstance(ref, Const)
        self.assertIs(type(ref), type(c))
        self.assertIsNot(ref, c)
        self.assertEqual(ref.value, 10)
        self.assertEqual(ref(), 10)

    def test_copy_with_mutable_value_shares_reference(self: Self) -> None:
        # copy() is not deep-copy; it should preserve the same underlying object
        c: Const
        ref: Const
        shared: dict[str, int]

        shared = {"k": 1}
        c = Const(shared)
        ref = c.copy()

        self.assertIsNot(ref, c)
        self.assertIs(ref.value, c.value)
        self.assertIs(ref(), c())

        shared["k"] = 2
        self.assertEqual(c()["k"], 2)
        self.assertEqual(ref()["k"], 2)

    def test_slots_only_value_attribute(self: Self) -> None:
        c: Const
        c = Const(1)
        with self.assertRaises(AttributeError):
            c.other = 2  # __slots__ should prevent arbitrary attributes


if __name__ == "__main__":
    unittest.main()
