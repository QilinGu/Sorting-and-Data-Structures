import unittest
from collections import namedtuple

from change import get_change
from fractional_knapsack import get_optimal_value
from dot_product import max_dot_product
from covering_segments import optimal_points
from different_summands import optimal_summands
from largest_number import largest_number, greater_or_equal


class TestChange(unittest.TestCase):
    def test_number(self):
        self.assertEqual(type(get_change(5)).__name__,'int')

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
        self.assertEqual(type(get_optimal_value(10, [30], [500])).__name__, "float")

    def test_single(self):
        self.assertEqual(round(get_optimal_value(10, [30], [500]), 4), 166.6667)

    def test_multiple(self):
        self.assertEqual(round(get_optimal_value(50, [20, 50, 30], [60, 100, 120]), 4), 180.0000)


class TestDotProduct(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(max_dot_product([23], [39])).__name__, "int")

    def test_single(self):
        self.assertEqual(max_dot_product([23], [39]), 897)

    def test_multiple(self):
        self.assertEqual(max_dot_product([1, 3, -5], [-2, 4, 1]), 23)


class TestOptimalPoints(unittest.TestCase):
    def test_type(self):
        segment = namedtuple('Segment', 'start end')
        segments = [segment(23, 39)]
        self.assertEqual(type(optimal_points(segments)).__name__, "list")

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
        self.assertEqual(type(optimal_summands(5)).__name__, "list")

    def test_one(self):
        self.assertEqual(optimal_summands(1), [1])
        self.assertEqual(optimal_summands(2), [2])

    def test_two(self):
        self.assertEqual(optimal_summands(3), [1, 2])
        self.assertEqual(optimal_summands(4), [1, 3])
        self.assertEqual(optimal_summands(5), [1, 4])

    def test_multiple(self):
        self.assertEqual(optimal_summands(8), [1, 2, 5])
        self.assertEqual(optimal_summands(6), [1, 2, 3])


class TestLargestNumber(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(largest_number(["5"])).__name__, "str")

    def test_one(self):
        self.assertEqual(largest_number(["5"]), "5")
        self.assertEqual(largest_number(["75"]), "75")
        self.assertEqual(largest_number(["912"]), "912")

    def test_single_digits(self):
        self.assertEqual(largest_number(["4", "9"]), "94")
        self.assertEqual(largest_number(["5", "7", "1"]), "751")

    def test_multiple_digits(self):
        self.assertEqual(largest_number(["23", "39", "92"]), "923923")

    def test_mixed_digits(self):
        self.assertEqual(largest_number(["23", "39", "9", "222"]), "93923222")
        self.assertEqual(largest_number(["21", "2"]), "221")


class TestGreaterOrEqual(unittest.TestCase):
    def test_type(self):
        self.assertEqual(type(greater_or_equal("5", "3")).__name__, "bool")

    def test_one(self):
        self.assertTrue(greater_or_equal("5", "3"))
        self.assertFalse(greater_or_equal("3", "5"))

    def test_two(self):
        self.assertFalse(greater_or_equal("51", "5"))
        self.assertTrue(greater_or_equal("5", "51"))

        self.assertTrue(greater_or_equal("13", "12"))
        self.assertFalse(greater_or_equal("12", "13"))

        self.assertTrue(greater_or_equal("32", "31"))
        self.assertFalse(greater_or_equal("31", "32"))

    def test_multiple(self):
        self.assertTrue(greater_or_equal("23", "222"))
        self.assertFalse(greater_or_equal("222", "23"))

        self.assertTrue(greater_or_equal("2442", "222"))
        self.assertFalse(greater_or_equal("222", "2442"))

    def test_same_endpoints(self):
        self.assertTrue(greater_or_equal("304", "30004"))
        self.assertFalse(greater_or_equal("30004", "304"))

    def test_equal(self):
        self.assertTrue(greater_or_equal("23", "23"))
        self.assertTrue(greater_or_equal("11", "11"))
        self.assertTrue(greater_or_equal("12", "12"))

if __name__ == "__main__":
    unittest.main()
