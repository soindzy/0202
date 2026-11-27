"""Автоматические проверки практического задания."""
import unittest

from text_validation import is_nonempty
from main import process

class Tests(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_nonempty("текст"))
        self.assertEqual(process(" привет "), "Принято: привет")
    def test_empty(self):
        for value in ["", "   ", "\t\n"]:
            with self.subTest(text=value):
                self.assertFalse(is_nonempty(value))
                self.assertEqual(process(value), "Ошибка: ввод не должен быть пустым")
    def test_type(self):
        with self.assertRaises(TypeError):
            is_nonempty(None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
