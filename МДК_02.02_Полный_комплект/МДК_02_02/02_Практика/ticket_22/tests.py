"""Автоматические проверки практического задания."""
import unittest

from decimal import Decimal
from discount import discounted_price
from formatting import format_price

class Tests(unittest.TestCase):
    def test_first_example(self):
        self.assertEqual(discounted_price("1000.00"), Decimal("900.00"))
        self.assertEqual(format_price(discounted_price("1000.00")), "К оплате: 900.00 руб.")
    def test_second_example(self):
        self.assertEqual(discounted_price("250.50"), Decimal("225.45"))
        self.assertEqual(format_price(discounted_price("250.50")), "К оплате: 225.45 руб.")
    def test_rounding(self):
        self.assertEqual(discounted_price("0.05"), Decimal("0.05"))
    def test_invalid(self):
        for value in ["abc", "-1", "NaN", "Infinity"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                discounted_price(value)


if __name__ == "__main__":
    unittest.main(verbosity=2)
