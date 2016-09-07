#! python3

import unittest
import fibonacci as fib


class TestFib(unittest.TestCase):
    def test_small(self):
        self.assertEqual(fib.calc_fib(0), 0)
        self.assertEqual(fib.calc_fib(1), 1)

    def test_normal(self):
        self.assertEqual(fib.calc_fib(6), 8)
        self.assertEqual(fib.calc_fib(15), 610)

if __name__ == "__main__":
    unittest.main()
