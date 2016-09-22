import unittest
from change import get_change


class TestChange(unittest.TestCase):
    def test_number(self):
        self.assertTrue(type(get_change(5)).__name__ == 'int')

    def test_two(self):
        self.assertEqual(get_change(2), 2)
        self.assertEqual(get_change(20), 2)

    def test_one(self):
        self.assertEqual(get_change(1), 1)
        self.assertEqual(get_change(5), 1)
        self.assertEqual(get_change(10), 1)

    def test_mixed(self):
        self.assertEqual(get_change(6), 2)
        self.assertEqual(get_change(16), 3)
        self.assertEqual(get_change(19), 6)
        self.assertEqual(get_change(28), 6)

if __name__ == "__main__":
    unittest.main()
