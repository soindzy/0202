"""Автоматические проверки практического задания."""
import unittest

from division import divide

class Tests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(0, 5), 0)
        self.assertEqual(divide(-9, 3), -3)
    def test_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
    def test_bad_type(self):
        for a, b in [("abc", 2), (2, "abc"), (True, 2)]:
            with self.subTest(a=a, b=b), self.assertRaises(TypeError):
                divide(a, b)


if __name__ == "__main__":
    unittest.main(verbosity=2)
