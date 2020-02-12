import unittest
import os
import sys

from calculator import calculator

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


class TestCalculator(unittest.TestCase):
    def test_correct_value(self):
        val1 = '1'
        val2 = '3'
        condition = '+'

        self.assertTrue(True, calculator(val1, val2, condition))

    def test_incorrect_val1(self):
        val1 = 'a'
        val2 = '3'
        condition = '+'
        with self.assertRaises(AssertionError):
            calculator(val1, val2, condition)

    def test_incorrect_val2(self):
        val1 = '1.0'
        val2 = 'aa'
        condition = '-'
        with self.assertRaises(AssertionError):
            calculator(val1, val2, condition)

    def test_incorrect_condition(self):
        val1 = '1'
        val2 = '2'
        condition = '+++'

        with self.assertRaises(AssertionError):
            calculator(val1, val2, condition)


if __name__ == '__main__':
    unittest.main()
