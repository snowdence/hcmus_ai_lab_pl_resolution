import unittest
from exp import *


class ExprItemTest(unittest.TestCase):
    def test_init(self):
        i1 = ExprItem("-A")
        self.assertEqual(i1.op, "-")
        self.assertEqual(i1.label_variable, "A")

    def test_init_2(self):
        i2 = ExprItem("A")
        self.assertEqual(i2.op, "+")
        self.assertEqual(i2.label_variable, "A")

    def test_invert(self):
        a = ExprItem("A")
        invert_a = ~a
        self.assertEqual(invert_a.op, "-")
        self.assertEqual(invert_a.label_variable, "A")

    def test_equal(self):
        a1 = ExprItem("A")
        a2 = ExprItem("A")
        self.assertTrue(a1 == a2)

    def test_equal_2(self):
        a = ExprItem("A")
        invert_a = ~ExprItem("A")
        inv_inv_a = ~invert_a
        self.assertTrue(a == inv_inv_a)
