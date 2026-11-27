"""Автоматические проверки практического задания."""
import unittest

from main import evaluate
from calculator import calculate

class Tests(unittest.TestCase):
    def test_operations(self):
        for op, expected in [("+", 12), ("-", 8), ("*", 20), ("/", 5)]:
            with self.subTest(operation=op):
                self.assertEqual(calculate(10, op, 2), expected)
    def test_integration(self):
        self.assertEqual(evaluate("10 + 2"), "Результат: 12")
    def test_errors(self):
        for text in ["abc", "a + 2", "1 ^ 2"]:
            with self.subTest(text=text), self.assertRaises(ValueError):
                evaluate(text)
        with self.assertRaises(ZeroDivisionError):
            evaluate("1 / 0")


if __name__ == "__main__":
    unittest.main(verbosity=2)
