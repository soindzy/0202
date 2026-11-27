"""Автоматические проверки практического задания."""
import unittest

from square import square

class Tests(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(square(2), 4)
    def test_zero(self):
        self.assertEqual(square(0), 0)
    def test_negative(self):
        self.assertEqual(square(-3), 9)
    def test_fraction(self):
        self.assertAlmostEqual(square(1.5), 2.25)


if __name__ == "__main__":
    unittest.main(verbosity=2)
