"""Автоматические проверки практического задания."""
import unittest

from age_validation import validate_age

class Tests(unittest.TestCase):
    def test_boundaries(self):
        for value in [0, 1, 35, 119, 120]:
            with self.subTest(value=value):
                self.assertEqual(validate_age(value), value)
    def test_out_of_range(self):
        for value in [-1, 121]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_age(value)
    def test_types(self):
        for value in ["20", 20.0, None, True]:
            with self.subTest(value=value), self.assertRaises(TypeError):
                validate_age(value)


if __name__ == "__main__":
    unittest.main(verbosity=2)
