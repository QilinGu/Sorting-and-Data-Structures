#!python3
import unittest
import binary_search as bs
import majority_element as me


class TestBinSearch(unittest.TestCase):
    def test_small(self):
        n = 5
        a = [1, 5, 8, 12, 13]
        tests = [8, 1, 23, 1, 11]
        results = [2, 0, -1, 0, -1]

        for i, val in enumerate(tests):
            self.assertEqual(bs.binary_search(a, val), results[i])


class TestMajority(unittest.TestCase):
    def test_small(self):
        a1 = [1, 4, 3, 2, 1]
        r1 = -1
        a2 = [7, 5, 4, 7, 7]
        r2 = 1
        self.assertEqual(me.get_majority_element(a1, 0, len(a1)), r1)
        self.assertEqual(me.get_majority_element(a2, 0, len(a2)), r2)


class TestQuickSort(unittest.TestCase):
    def test_small(self):
        pass

if __name__ == "__main__":
    unittest.main()
