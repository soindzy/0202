"""Автоматические проверки практического задания."""
import unittest

from geometry import rectangle_area

class Tests(unittest.TestCase):
    def test_area(self):
        self.assertEqual(rectangle_area(4, 6), 24)
        self.assertEqual(rectangle_area(0, 5), 0)
        self.assertAlmostEqual(rectangle_area(2.5, 4), 10)
    def test_negative(self):
        for sides in [(-1, 3), (3, -1)]:
            with self.assertRaises(ValueError):
                rectangle_area(*sides)


if __name__ == "__main__":
    unittest.main(verbosity=2)
