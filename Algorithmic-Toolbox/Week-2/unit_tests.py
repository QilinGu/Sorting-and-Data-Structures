#! python3

import unittest
from fibonacci import calc_fib
from fibonacci_last_digit import get_fibonacci_last_digit
from gcd import gcd_euclid
from lcm import lcm
import fibonacci_huge as fib_hg
from fibonacci_sum_last_digit import fibonacci_sum
from fibonacci_partial_sum import fibonacci_partial_sum


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
        self.assertEqual(gcd_euclid(1023473145, 226553150), 5)


class TestLCM(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(lcm(6, 8), 24)

    def test_large(self):
        self.assertEqual(lcm(28851538, 1183019), 1933053046)
        self.assertEqual(lcm(1023473145, 226553150), 46374212988031350)


class TestPisano(unittest.TestCase):
    def test_small(self):
        self.assertEqual(fib_hg.get_pisano_period(3), 8)
        self.assertEqual(fib_hg.get_pisano_period(12), 24)

    def test_large(self):
        self.assertEqual(fib_hg.get_pisano_period(130), 420)

    def test_huge(self):
        self.assertEqual(fib_hg.get_pisano_period(10000), 15000)


class TestFibHuge(unittest.TestCase):
    def test_small(self):
        self.assertEqual(fib_hg.get_fibonacci_huge(0, 10), 0)
        self.assertEqual(fib_hg.get_fibonacci_huge(1, 10), 1)

    def test_big(self):
        self.assertEqual(fib_hg.get_fibonacci_huge(331, 10), 9)
        self.assertEqual(fib_hg.get_fibonacci_huge(327305, 10), 5)

    def test_huge(self):
        self.assertEqual(fib_hg.get_fibonacci_huge(239, 1000), 161)
        self.assertEqual(fib_hg.get_fibonacci_huge(100, 100000), 15075)
        self.assertEqual(fib_hg.get_fibonacci_huge(100000, 100000), 46875)


class TestSumLasDigit(unittest.TestCase):
    def test_small(self):
        self.assertEqual(fibonacci_sum(3), 4)

    def test_normal(self):
        self.assertEqual(fibonacci_sum(100), 5)


class TestPartialSumLasDigit(unittest.TestCase):
    def test_small(self):
        self.assertEqual(fibonacci_partial_sum(3, 7), 1)
        self.assertEqual(fibonacci_partial_sum(10, 10), 5)

    def test_normal(self):
        self.assertEqual(fibonacci_partial_sum(10, 200), 2)

if __name__ == "__main__":
    unittest.main()
