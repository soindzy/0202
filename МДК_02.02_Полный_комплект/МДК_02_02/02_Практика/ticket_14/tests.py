"""Автоматические проверки практического задания."""
import unittest

from average import average

class Tests(unittest.TestCase):
    def test_two_positive(self):
        self.assertEqual(average(2, 4), 3)
    def test_opposite(self):
        self.assertEqual(average(-4, 4), 0)
    def test_zero(self):
        self.assertEqual(average(0, 0), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
