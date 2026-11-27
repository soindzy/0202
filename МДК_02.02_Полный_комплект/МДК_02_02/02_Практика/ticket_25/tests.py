"""Автоматические проверки практического задания."""
import unittest

from user_data import create_user
from user_message import format_user

class Tests(unittest.TestCase):
    def test_message(self):
        self.assertEqual(format_user(create_user("Анна", 20)), "Пользователь: Анна. Возраст: 20.")
        self.assertEqual(format_user(create_user(" Иван ", 35)), "Пользователь: Иван. Возраст: 35.")
    def test_boundaries(self):
        self.assertEqual(create_user("А", 0).age, 0)
        self.assertEqual(create_user("А", 120).age, 120)
    def test_invalid(self):
        for name, age, error in [(" ", 10, ValueError), ("А", -1, ValueError), ("А", 121, ValueError), ("А", "20", TypeError), (None, 20, TypeError)]:
            with self.subTest(name=name, age=age), self.assertRaises(error):
                create_user(name, age)


if __name__ == "__main__":
    unittest.main(verbosity=2)
