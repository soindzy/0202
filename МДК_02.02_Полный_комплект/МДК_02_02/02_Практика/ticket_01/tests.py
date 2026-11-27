"""Автоматические проверки практического задания."""
import unittest

from addition import add

class Tests(unittest.TestCase):
    def test_add(self):
        for a, b, expected in [(7, 5, 12), (0, 0, 0), (-3, 2, -1), (1.5, 2.5, 4.0)]:
            with self.subTest(a=a, b=b):
                self.assertEqual(add(a, b), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
