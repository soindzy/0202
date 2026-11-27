"""Автоматические проверки практического задания."""
import unittest

from decimal import Decimal
from price_source import get_prices
from price_total import total_prices
from price_output import format_total

class Tests(unittest.TestCase):
    def test_pipeline(self):
        self.assertEqual(total_prices(get_prices()), Decimal("130.00"))
        self.assertEqual(format_total(total_prices(get_prices())), "Общая стоимость: 130.00 руб.")
    def test_empty(self):
        self.assertEqual(total_prices([]), Decimal("0.00"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
