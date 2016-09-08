#! python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_last_digit(n):
    """
    Algorithm for computing the fibonacci sequence

    :param n: int term to compute
    :return: int value of fibonacci sequence at n
    """
    if n <= 1:
        return n
    fib0 = 0
    fib1 = 1
    for term in range(n - 1):
        fib0, fib1 = fib1 % 10, fib0 % 10 + fib1 % 10
    return fib1 % 10


def main():
    data = sys.stdin.read()
    n = int(data)
    print(get_fibonacci_last_digit(n))

if __name__ == '__main__':
    main()
