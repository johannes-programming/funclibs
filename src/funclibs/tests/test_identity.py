import unittest

from funclibs.elementary.identity import identity
from typing import *

class TestIdentity(unittest.TestCase):
    def test_returns_same_value_for_primitives(self:Self)->None:
        self.assertEqual(identity(0), 0)
        self.assertEqual(identity(123), 123)
        self.assertEqual(identity(-5), -5)
        self.assertEqual(identity(3.14), 3.14)
        self.assertEqual(identity("hello"), "hello")
        self.assertEqual(identity(True), True)
        self.assertIs(identity(None), None)

    def test_returns_same_object_for_mutables(self:Self)->None:
        x:dict[str, int]
        y:list[int]
        z:set[int]
        x = {"a": 1}
        self.assertIs(identity(x), x)

        y = [1, 2, 3]
        self.assertIs(identity(y), y)

        z = {1, 2}
        self.assertIs(identity(z), z)

    def test_returns_same_object_for_custom_instance(self:Self)->None:
        class C:
            pass
        inst:C
        inst = C()
        self.assertIs(identity(inst), inst)

    def test_positional_only_argument(self:Self)->None:
        with self.assertRaises(TypeError):
            identity(value=1)  # positional-only, so this must fail


if __name__ == "__main__":
    unittest.main()
