"""Автоматические проверки практического задания."""
import unittest

from temperature import celsius_to_fahrenheit

class Tests(unittest.TestCase):
    def test_conversion(self):
        for value, expected in [(0, 32), (100, 212), (-40, -40), (37, 98.6)]:
            with self.subTest(celsius=value):
                self.assertAlmostEqual(celsius_to_fahrenheit(value), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
