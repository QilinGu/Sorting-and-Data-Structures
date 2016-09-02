#! python3
"""
Find the max pairwise product

@author Ethan Zimbra
"""
import sys

def main():
	"""
	Main entry point for the script if file is executed directly
	"""
	lines = sys.stdin.read().splitlines()
	for line in lines:
		tokens = line.split()
		tokens = [int(x) for x in tokens]
		if len(tokens) > 1:
			print(max_pairwise_product(tokens))

def max_pairwise_product(nums):
	"""
	Calculate the max product of two numbers in the provided list nums,

	Args:
		num (list): list of integers

	Returns:
		integer: the computed max pair product from the provided list num
	"""
	if len(nums) < 2:
		return int(nums[0])
	
	max1 = max(nums)
	nums.remove(max1)
	max2 = max(nums)
	
	return max1 * max2

def stress_test(good_funct, test_funct):
	pass

if __name__ == "__main__":
	main()
	
