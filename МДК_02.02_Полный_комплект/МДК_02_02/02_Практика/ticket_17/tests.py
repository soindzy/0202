"""Автоматические проверки практического задания."""
import unittest

from sorting import sort_numbers

class Tests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(sort_numbers([]), [])
    def test_unsorted(self):
        values = [3, 1, 2]
        self.assertEqual(sort_numbers(values), [1, 2, 3])
        self.assertEqual(values, [3, 1, 2])
    def test_duplicates(self):
        self.assertEqual(sort_numbers([2, 1, 2, 1]), [1, 1, 2, 2])
    def test_negative(self):
        self.assertEqual(sort_numbers([-1, -5, 0]), [-5, -1, 0])
    def test_already_sorted(self):
        self.assertEqual(sort_numbers([1, 2, 3]), [1, 2, 3])


if __name__ == "__main__":
    unittest.main(verbosity=2)
