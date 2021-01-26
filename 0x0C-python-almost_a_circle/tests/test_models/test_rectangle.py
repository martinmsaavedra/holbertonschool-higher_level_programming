#!/usr/bin/python3
"""test module for rectangle"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """testing the Rectangle class and its methods"""

    def test_inst_methods(self):
        """test methods"""
        test_inst = Rectangle(2, 3, 0, 0, 1)
        """test area of rectangle"""
        self.assertEqual(test_inst.area(), 6)
        """test str"""
        self.assertEqual(test_inst.__str__(), '[Rectangle] (1) 0/0 - 2/3')
        """test to_dictionary"""
        self.assertEqual(test_inst.to_dictionary(),
                         {'id': 1, 'width': 2, 'height': 3, 'x': 0, 'y': 0})

    def test_negatives(self):
        """test negative values"""
        with self.assertRaises(ValueError):
            """negative width"""
            fail_inst = Rectangle(-2, 3, 3, 0, 0)
        with self.assertRaises(ValueError):
            """negative height"""
            fail_inst = Rectangle(2, -3, 3, 0, 0)
        with self.assertRaises(ValueError):
            """negative x"""
            fail_inst = Rectangle(2, 3, -1, 0, 0)
        with self.assertRaises(ValueError):
            """negative y"""
            fail_inst = Rectangle(-2, 3, 0, -2, 0)

    def test_not_int(self):
        """test values without ints"""
        with self.assertRaises(TypeError):
            """on width"""
            fail_inst = Rectangle('testStr', 3, 0, 0, 1)
        with self.assertRaises(TypeError):
            """on height"""
            fail_inst = Rectangle(3, '3', 0, 0, 1)
        with self.assertRaises(TypeError):
            """on x"""
            fail_inst = Rectangle(1, 3, '0', 0, 1)
        with self.assertRaises(TypeError):
            """on y"""
            fail_inst = Rectangle(2, 3, 0, '0', 1)

    def test_None_values(self):
        """test None values"""
        with self.assertRaises(TypeError):
            """on width"""
            fail_inst = Rectangle(None, 3, 0, 0, 1)
        with self.assertRaises(TypeError):
            """on height"""
            fail_inst = Rectangle(2, None, 0, 0, 1)
        with self.assertRaises(TypeError):
            """on x"""
            fail_inst = Rectangle(2, 3, None, 0, 1)
        with self.assertRaises(TypeError):
            """on y"""
            fail_inst = Rectangle(2, 5, 0, None, 1)

    def test_arg_number(self):
        """test less that 3 args and more than 5 args"""
        with self.assertRaises(TypeError):
            inst = Rectangle(3, 3, 0, 0, 1, 5)
        with self.assertRaises(TypeError):
            inst = Rectangle(1)

    def test_update(self):
        """test update method"""
        inst_update = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(inst_update.to_dictionary(),
                         {'id': 1, 'width': 1, 'height': 1, 'x': 0, 'y': 0})
        inst_update.update(13, 3, 2, 0, 0)
        self.assertEqual(inst_update.to_dictionary(),
                         {'id': 13, 'width': 3, 'height': 2, 'x': 0, 'y': 0})

    def test_update_failure(self):
        """test failures of update method"""
        inst_up = Rectangle(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            """more than five args"""
            inst_up.update(1, 2, 3, 3, 1, 2)
        with self.assertRaises(TypeError):
            """wrong data type"""
            inst_up.update(1, 1, 'test', [1], 1)


if __name__ == '__main__':
    unittest.main()
