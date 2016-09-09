#! python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    total = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        total += current

    return total % 10


def generate_lookup():
    """
    Generate set of 60 fibonacci sums to be used as a lookup table.
    The pisano period of 10 is 60 so the sums repeat every 60 terms.
    This means that a table can be pre-computed and then used for
    any value of n making no further computation required.

    :return: list of the fibonacci last digit sums to n = 60.
    """
    return [fibonacci_sum_naive(x) for x in range(60)]


def fibonacci_sum(n):
    """
    Use lookup table of 60 terms to determine the last digit of the
    fibonacci_sum of any term n.

    :param n: int term to compute
    :return: int last digit of the sum of fibonacci numbers up to the nth term
    """
    if n <= 1:
        return n
    sum_lookup = [0, 1, 2, 4, 7, 2, 0, 3, 4, 8, 3, 2, 6, 9, 6, 6,
                  3, 0, 4, 5, 0, 6, 7, 4, 2, 7, 0, 8, 9, 8, 8, 7,
                  6, 4, 1, 6, 8, 5, 4, 0, 5, 6, 2, 9, 2, 2, 5, 8,
                  4, 3, 8, 2, 1, 4, 6, 1, 8, 0, 9, 0]

    return sum_lookup[n % 60]


def main():
    data = sys.stdin.read()
    n = int(data)
    print(fibonacci_sum(n))


if __name__ == '__main__':
    main()
