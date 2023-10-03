#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Presence of docstrings"""

    def test_no_args(self):
        """No arguments"""
        self.assertIsNone(max_integer())

    def test_empty_list(self):
        """Empty list []"""
        test = []
        self.assertIsNone(max_integer(test))

    def test_max_at_end(self):
        """Increasing Numbers"""
        test = [12, 1, 18, 6, 14, 40]
        self.assertEqual(max_integer(test), 40)

    def test_two_of_max(self):
        """Maximum Number"""
        test = [12, 1, 40, 6, 14, 40]
        self.assertEqual(max_integer(test), 40)

    def test_none(self):
        """None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        """String"""
        test = [1, "string", 3, 4, 5]
        with self.assertRaises(TypeError):
            max_integer(test)

    def test_one_element(self):
        """1 number only"""
        test_ele = [10]
        self.assertEqual(max_integer(test_ele), 10)

    def test_max_at_beginning(self):
        """Beginning with maximum"""
        test_pos = [130, 129, 23, 6, 0, 10]
        self.assertEqual(max_integer(test_pos), 130)

    def test_max_at_middle(self):
        """Middle maximum"""
        test_max = [1, 10, 23, 30, 14, 12]
        self.assertEqual(max_integer(test_max), 30)

    def test_one_negative(self):
        """Negative numbers"""
        test = [10, -10, 1, 6, 4, 2]
        self.assertEqual(max_integer(test), 10)

    def test_all_10(self):
        """same number"""
        test = [10, 10, 10, 10, 10, 10]
        self.assertEqual(max_integer(test), 10)

    def test_all_negative(self):
        """all negative numbers"""
        test_neg = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(test_neg), -1)


if __name__ == "__main__":
    unittest.main()
