"""Автоматические проверки практического задания."""
import unittest

from positive import count_positive

class Tests(unittest.TestCase):
    def test_counts(self):
        for values, expected in [([-2, 0, 3, 5, -1], 2), ([], 0), ([0, -3], 0), ([1, 2, 3], 3)]:
            with self.subTest(values=values):
                self.assertEqual(count_positive(values), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
