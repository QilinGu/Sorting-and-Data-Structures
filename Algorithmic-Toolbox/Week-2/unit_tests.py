#! python3

import unittest
from fibonacci import calc_fib
from fibonacci_last_digit import get_fibonacci_last_digit
from gcd import gcd_euclid
from lcm import lcm
import fibonacci_huge as fib_hg


class TestFib(unittest.TestCase):
    def test_small(self):
        self.assertEqual(calc_fib(0), 0)
        self.assertEqual(calc_fib(1), 1)

    def test_normal(self):
        self.assertEqual(calc_fib(6), 8)
        self.assertEqual(calc_fib(15), 610)


class TestFibLastDigit(unittest.TestCase):
    def test_small(self):
        self.assertEqual(get_fibonacci_last_digit(0), 0)
        self.assertEqual(get_fibonacci_last_digit(1), 1)

    def test_normal(self):
        self.assertEqual(get_fibonacci_last_digit(239), 1)

    def test_huge(self):
        self.assertEqual(get_fibonacci_last_digit(331), 9)
        self.assertEqual(get_fibonacci_last_digit(327305), 5)


class TestGCD(unittest.TestCase):
    def test_for_one(self):
        self.assertEqual(gcd_euclid(18, 35), 1)

    def test_normal(self):
        self.assertEqual(gcd_euclid(28851538, 1183019), 17657)


class TestLCM(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(lcm(6, 8), 24)

    def test_large(self):
        self.assertEqual(lcm(28851538, 1183019), 1933053046)


class TestPisano(unittest.TestCase):
    def test_small(self):
        self.assertEqual(fib_hg.get_pisano_period(3), 8)
        self.assertEqual(fib_hg.get_pisano_period(12), 24)

    def test_large(self):
        self.assertEqual(fib_hg.get_pisano_period(130), 420)


class TestFibHuge(unittest.TestCase):
    def test_small(self):
        self.assertEqual(fib_hg.get_fibonacci_huge(0, 10), 0)
        self.assertEqual(fib_hg.get_fibonacci_huge(1, 10), 1)

    def test_big(self):
        self.assertEqual(fib_hg.get_fibonacci_huge(331, 10), 9)
        self.assertEqual(fib_hg.get_fibonacci_huge(327305, 10), 5)

    def test_huge(self):
        self.assertEqual(fib_hg.get_fibonacci_huge(239, 1000), 161)

if __name__ == "__main__":
    unittest.main()
