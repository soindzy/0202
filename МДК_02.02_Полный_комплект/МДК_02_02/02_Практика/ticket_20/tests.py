"""Автоматические проверки практического задания."""
import unittest

from parity import is_even

class Tests(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(8))
    def test_odd(self):
        self.assertFalse(is_even(7))
    def test_zero(self):
        self.assertTrue(is_even(0))
    def test_negative(self):
        self.assertTrue(is_even(-4))


if __name__ == "__main__":
    unittest.main(verbosity=2)
