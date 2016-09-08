#! python3
import sys


def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_euclid(a, b):
    """
    Calculates the greatest common denominator using the euclidean method
    :param a: int first vale
    :param b: int second value
    :return: greatest common denominator of a and b
    """
    if b == 0:
        return a
    ap = a % b
    return gcd_euclid(b, ap)


def main():
    data = sys.stdin.read()
    a, b = map(int, data.split())
    print(gcd_euclid(a, b))

if __name__ == "__main__":
    main()
