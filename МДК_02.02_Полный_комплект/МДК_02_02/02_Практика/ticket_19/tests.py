"""Автоматические проверки практического задания."""
import unittest

from safe_access import get_element

class Tests(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(get_element([10, 20, 30], 1), 20)
        self.assertEqual(get_element([10, 20, 30], 0), 10)
        self.assertEqual(get_element([10, 20, 30], 2), 30)
    def test_bounds(self):
        for sequence, index in [([10, 20, 30], 3), ([10], -1), ([], 0)]:
            with self.subTest(sequence=sequence, index=index), self.assertRaises(IndexError):
                get_element(sequence, index)
    def test_bad_index_type(self):
        for index in [1.0, "1", True]:
            with self.subTest(index=index), self.assertRaises(TypeError):
                get_element([10, 20], index)


if __name__ == "__main__":
    unittest.main(verbosity=2)
