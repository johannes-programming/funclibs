import unittest

from funclibs.elementary.Const import Const


class TestConst(unittest.TestCase):
    def test_init_default_value_is_none(self):
        c = Const()
        self.assertIsNone(c.value)
        self.assertIs(c(), None)

    def test_init_sets_value(self):
        c = Const(123)
        self.assertEqual(c.value, 123)
        self.assertEqual(c(), 123)

    def test_call_ignores_args_and_kwargs(self):
        c = Const("x")
        self.assertEqual(c(1, 2, 3, a=4, b=5), "x")

    def test_copy_returns_new_instance_same_type(self):
        c = Const(10)
        cp = c.copy()
        self.assertIsInstance(cp, Const)
        self.assertIs(type(cp), type(c))
        self.assertIsNot(cp, c)
        self.assertEqual(cp.value, 10)
        self.assertEqual(cp(), 10)

    def test_copy_with_mutable_value_shares_reference(self):
        # copy() is not deep-copy; it should preserve the same underlying object
        shared = {"k": 1}
        c = Const(shared)
        cp = c.copy()

        self.assertIsNot(cp, c)
        self.assertIs(cp.value, c.value)
        self.assertIs(cp(), c())

        shared["k"] = 2
        self.assertEqual(c()["k"], 2)
        self.assertEqual(cp()["k"], 2)

    def test_slots_only_value_attribute(self):
        c = Const(1)
        with self.assertRaises(AttributeError):
            c.other = 2  # __slots__ should prevent arbitrary attributes


if __name__ == "__main__":
    unittest.main()
