"""Автоматические проверки практического задания."""
import unittest

from summation import sum_numbers

class Tests(unittest.TestCase):
    def test_regression(self):
        self.assertEqual(sum_numbers([1, 2, 3]), 6)
    def test_empty(self):
        self.assertEqual(sum_numbers([]), 0)
    def test_mixed(self):
        self.assertEqual(sum_numbers([-2, 5, -3]), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
