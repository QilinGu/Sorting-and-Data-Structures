#! python3

import sys


def max_dot_product(a, b):
    """
    Calculates the maximum dot product of two sequences a and b
    :param a: int list of numbers
    :param b: int list of numbers
    :return: int max dot product of a and b
    """
    res = 0
    # Sort both lists from max to min and pair them together
    pairing = list(zip(sorted(a, reverse=True), sorted(b, reverse=True)))
    # Calculate the sum of the products of each pair
    for item in pairing:
        res += item[0] * item[1]
    return res


def main():
    vals = sys.stdin.read()
    data = list(map(int, vals.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))

if __name__ == '__main__':
    main()
