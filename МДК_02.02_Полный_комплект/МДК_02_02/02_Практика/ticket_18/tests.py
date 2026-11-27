"""Автоматические проверки практического задания."""
import unittest

from conversion import parse_integer

class Tests(unittest.TestCase):
    def test_required_number(self):
        self.assertEqual(parse_integer("15"), 15)
    def test_required_error(self):
        with self.assertRaisesRegex(ValueError, "целое число"):
            parse_integer("abc")
    def test_other_inputs(self):
        self.assertEqual(parse_integer(" -8 "), -8)
        for value in ["", "3.5"]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                parse_integer(value)
        with self.assertRaises(TypeError):
            parse_integer(None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
