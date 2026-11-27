"""Автоматические проверки практического задания."""
import unittest

from text_length import string_length

class Tests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(string_length(""), 0)
    def test_regular(self):
        self.assertEqual(string_length("Привет"), 6)
    def test_spaces(self):
        self.assertEqual(string_length("два слова"), 9)
        self.assertEqual(string_length("   "), 3)
    def test_type(self):
        with self.assertRaises(TypeError):
            string_length(None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
