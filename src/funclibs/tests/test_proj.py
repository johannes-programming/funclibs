from typing import *
import unittest

from funclibs.elementary.Proj import Proj

__all__=["TestProj"]

class TestProj(unittest.TestCase):
    def test_int_key_projects_from_args(self:Self)->None:
        p:Proj
        q:Proj

        p = Proj(0)
        self.assertEqual(p("a", "b"), "a")

        q = Proj(1)
        self.assertEqual(q("a", "b"), "b")

    def test_int_key_out_of_range_returns_default(self:Self)->None:
        p:Proj
        p = Proj(5, default="D")
        self.assertEqual(p("a", "b"), "D")

    def test_negative_int_key_behaves_like_python_indexing(self:Self)->None:
        p:Proj
        p = Proj(-1)
        self.assertEqual(p("a", "b"), "b")

    def test_str_key_projects_from_kwargs(self:Self)->None:
        p:Proj
        p = Proj("x")
        self.assertEqual(p(x=10, y=20), 10)

    def test_missing_kw_returns_default(self:Self)->None:
        p:Proj
        p = Proj("missing", default="D")
        self.assertEqual(p(x=1), "D")

    def test_with_no_default_attribute_returns_none_if_missing(self:Self)->None:
        # If constructed with only key, self.default isn't set; __call__ catches and returns None.
        p:Proj
        p = Proj("missing")
        self.assertIsNone(p(x=1))

    def test_key_coercion_indexable_becomes_int(self:Self)->None:
        class Indexable:
            def __index__(self:Self)->None:
                return 2

        p:Proj
        p = Proj(Indexable())
        self.assertIsInstance(p.key, int)
        self.assertEqual(p.key, 2)
        self.assertEqual(p("a", "b", "c"), "c")

    def test_key_coercion_non_indexable_becomes_str(self:Self)->None:
        p:Proj
        q:Proj
        p = Proj(object())
        self.assertIsInstance(p.key, str)

        # Ensure it uses kwargs lookup when key is str
        q = Proj("k", default="D")
        self.assertEqual(q(k=123), 123)

    def test_any_error_in_lookup_returns_default(self:Self)->None:
        # kwargs lookup error (missing) -> default
        p:Proj
        q:Proj
        p = Proj("k", default="D")
        self.assertEqual(p(x=1), "D")

        # args lookup error (type mismatch shouldn't happen due to coercion, but keep a safety check)
        q = Proj(0, default="D")
        self.assertEqual(q(), "D")  # IndexError caught -> default

    def test_slots_prevent_extra_attributes(self:Self)->None:
        p:Proj
        p = Proj(0)
        with self.assertRaises(AttributeError):
            p.other = 1  # __slots__ should block this


if __name__ == "__main__":
    unittest.main()
