#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Defin unittest for [max-integer]."""

    def test_ordered_list(self):
        """to test the function in ordered list."""
        x = [1, 2, 3, 4]
        self.assertEqual(max_integer(x), 4)

    def test_unorder_list(self):
        """to test the function in unordered list."""
        x = [1, 3, 4, 2]
        self.assertEqual(max_integer(x), 4)

    def test_max_big(self):
        """to test the function when the biggest value at the biggining."""
        x = [4, 3, 1, 2]
        self.assertEqual(max_integer(x), 4)

    def test_empety_list(self):
        """to test the function in empety list."""
        x = []
        self.assertEqual(max_integer(x), None)

    def test_onevalue_list(self):
        """to test the function in one value list."""
        x = [5]
        self.assertEqual(max_integer(x), 5)

    def test_float_value(self):
        """to test the function in float value."""
        x = [4.1, 3.0, 1.5, 2.87]
        self.assertEqual(max_integer(x), 4.1)

    def test_float_int(self):
        """to test the function in float and int value."""
        x = [4.6, 4, 1, 2.5]
        self.assertEqual(max_integer(x), 4.6)

    def test_string_value(self):
        """to test the function in string."""
        x = "Marta"
        self.assertEqual(max_integer(x), 't')

    def test_liststring(self):
        """to test the function in string list."""
        x = ["marta", "name", "yesu", "pet"]
        self.assertEqual(max_integer(x), "yesu")

    def test_empetystring(self):
        """to test the function in empety string."""
        x = ""
        self.assertEqual(max_integer(x), None)


if __name__ == '__main__':
    unittest.main()
