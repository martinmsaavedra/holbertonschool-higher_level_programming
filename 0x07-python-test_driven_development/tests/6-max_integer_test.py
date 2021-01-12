#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Performfs test cases
    """
    def test_max_integer(self):
        self.assertAlmostEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_integer_middle(self):
        self.assertAlmostEqual(max_integer([10, 2, 20, 3, 4]), 20)

    def test_max_integer_one(self):
        self.assertAlmostEqual(max_integer([10]), 10)

    def test_isNone(self):
        self.assertAlmostEqual(max_integer(), None)

    def test_Dictionary(self):
        self.assertRaises(TypeError, max_integer, {1, 2, 3, 4})

    def test_String(self):
        self.assertRaises(TypeError, max_integer, [1, 2, "String", 4])

    def test_ListNone(self):
        self.assertRaises(TypeError, max_integer, [1, 2, None, 4])

    def test_ListWhitinList(self):
        self.assertRaises(TypeError, max_integer, [1, 2, [1, 7, 80], 4])

    def tests_max_zero(self):
        self.assertEqual(max_integer([-100, -1, 0]), 0)

if __name__ == '__main__':
    unittest.main()
