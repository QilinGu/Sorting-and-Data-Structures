import unittest
from change import get_change
from fractional_knapsack import get_optimal_value
from dot_product import max_dot_product


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


class TestKnapsack(unittest.TestCase):
    def test_type(self):
        self.assertTrue(type(get_optimal_value(10, [30], [500])).__name__ == "float")

    def test_single(self):
        self.assertEqual(round(get_optimal_value(10, [30], [500]), 4), 166.6667)

    def test_multiple(self):
        self.assertEqual(round(get_optimal_value(50, [20, 50, 30], [60, 100, 120]), 4), 180.0000)


class TestDotProduct(unittest.TestCase):
    def test_type(self):
        self.assertTrue(type(max_dot_product([23], [39])).__name__ == "int")

    def test_single(self):
        self.assertEqual(max_dot_product([23], [39]), 897)

    def test_multiple(self):
        self.assertEqual(max_dot_product([1, 3, -5], [-2, 4, 1]), 23)

if __name__ == "__main__":
    unittest.main()
