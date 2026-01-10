import unittest
from typing import *

from funclibs.elementary.Const import Const


class TestConst(unittest.TestCase):
    def test_init_default_value_is_none(self: Self) -> None:
        c: Const
        c = Const()
        self.assertIsNone(c.value)

    def test_init_sets_value(self: Self) -> None:
        c: Const
        c = Const(123)
        self.assertEqual(c.value, 123)

    def test_value_property_get_set(self: Self) -> None:
        c: Const
        c = Const("a")
        self.assertEqual(c.value, "a")
        c.value = "b"
        self.assertEqual(c.value, "b")

    def test_call_returns_value_ignoring_args_kwargs(self: Self) -> None:
        c: Const
        c = Const("x")
        self.assertEqual(c(), "x")
        self.assertEqual(c(1, 2, 3), "x")
        self.assertEqual(c(a=1, b=2), "x")
        self.assertEqual(c(1, 2, a=3), "x")

    def test_copy_returns_new_instance_same_value(self: Self) -> None:
        c1: Const
        c2: Const
        c1 = Const({"k": 1})
        c2 = c1.copy()

        self.assertIsInstance(c2, Const)
        self.assertIsNot(c2, c1)
        self.assertIs(c2.value, c1.value)  # same object reference
        self.assertEqual(c2.value, {"k": 1})

    def test_slots_prevent_new_attributes(self: Self) -> None:
        c: Const
        c = Const(1)
        with self.assertRaises(AttributeError):
            c.new_attr = 42

    def test_generic_type_does_not_affect_runtime(self: Self) -> None:
        c: Const[int]
        c = Const(5)
        self.assertEqual(c.value, 5)
        self.assertEqual(c("ignored"), 5)


if __name__ == "__main__":
    unittest.main()
