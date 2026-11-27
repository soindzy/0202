"""Автоматические проверки практического задания."""
import unittest

from maximum import find_maximum

class Tests(unittest.TestCase):
    def test_maximum(self):
        for values, expected in [([3, 8, 2, 5], 8), ([-7, -2, -9], -2), ([4], 4), ([2, 2], 2)]:
            with self.subTest(values=values):
                self.assertEqual(find_maximum(values), expected)
    def test_empty(self):
        with self.assertRaises(ValueError):
            find_maximum([])


if __name__ == "__main__":
    unittest.main(verbosity=2)
