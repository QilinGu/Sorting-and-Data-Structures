#! python3
import sys
from gcd import gcd_euclid
from decimal import Decimal


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def lcm(a, b):
    """
    Calculates the least common multiple using the greatest common denominator

    :param a: int first value
    :param b: int second value
    :return: the least common multiple of a and b
    """
    return int((Decimal(a) * Decimal(b)) / Decimal(gcd_euclid(a, b)))


def main():
    data = sys.stdin.read()
    a, b = map(int, data.split())
    print(lcm(a, b))

if __name__ == '__main__':
    main()

