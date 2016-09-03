#! python3
"""
Unit test suite for

@author Ethan Zimbra
"""
import check_brackets as cb
import unittest


class TestCheckBrackets(unittest.TestCase):

    def test_balanced(self):
        self.assertEqual(cb.check_syntax(['(', ')', '[', ']']), "Success")

    def test_one_left(self):
        self.assertEqual(cb.check_syntax(['[']), 1)

    def test_one_right(self):
        self.assertEqual(cb.check_syntax([')']), 1)

    def test_bad(self):
        self.assertEqual(cb.check_syntax(['(', ')', '[']), 3)


if __name__ == "__main__":
    unittest.main()
