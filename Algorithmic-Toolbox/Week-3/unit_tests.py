import unittest
from collections import namedtuple

from change import get_change
from fractional_knapsack import get_optimal_value
from dot_product import max_dot_product
from covering_segments import optimal_points
from different_summands import optimal_summands


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


class TestOptimalPoints(unittest.TestCase):
    def test_type(self):
        segment = namedtuple('Segment', 'start end')
        segments = [segment(23, 39)]
        self.assertTrue(type(optimal_points(segments)).__name__ == "list")

    def test_single(self):
        segment = namedtuple('Segment', 'start end')
        segments = [segment(23, 39)]
        points = optimal_points(segments)
        self.assertEqual(len(points), 1)
        self.assertTrue(39 >= points[0] >= 23)

    def test_multiple(self):
        segment = namedtuple('Segment', 'start end')
        segments = [segment(4, 7), segment(1, 3), segment(2, 5), segment(5, 6)]
        points = optimal_points(segments)
        self.assertEqual(len(points), 2)
        self.assertTrue(2 <= points[0] <= 3)
        self.assertTrue(5 <= points[1] <= 6)


class TestOptimalSummands(unittest.TestCase):
    def test_type(self):
        self.assertTrue(type(optimal_summands(5)).__name__ == "list")

    def test_one(self):
        self.assertEqual(optimal_summands(1)[0], 1)
        self.assertEqual(optimal_summands(2)[0], 2)

    def test_multiple(self):
        self.assertEqual(optimal_summands(8), [1, 2, 5])
        self.assertEqual(optimal_summands(6), [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
