#! python3
"""
Unit test suite for

@author Ethan Zimbra
"""
import max_pairwise_product as mp
import unittest

class TestMaxPairwiseProduct(unittest.TestCase):

	def test_two(self):
		self.assertEqual(mp.max_pairwise_product([4, 7]), 28)
		
	def test_multiple(self):
		self.assertEqual(mp.max_pairwise_product([2, 1, 6, 8]), 48)
	
	def test_same(self):
		self.assertEqual(mp.max_pairwise_product([2, 1, 5, 5]), 25)


if __name__ == "__main__":
	unittest.main()
	
