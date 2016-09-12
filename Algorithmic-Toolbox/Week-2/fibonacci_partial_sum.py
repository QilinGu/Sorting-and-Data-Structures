#! python3
import sys
from fibonacci_huge import get_fibonacci_huge


def fibonacci_partial_sum_naive(from_, to):
    if to <= 1:
        return to

    previous = 0
    current = 1

    for _ in range(from_ - 1):
        previous, current = current, previous + current

    last = current

    for _ in range(to - from_):
        previous, current = current, previous + current
        last += current

    return last % 10


def fibonacci_partial_sum(a, b):
    """
    Returns the last digit of the partial sum of the fibonacci sequence between a and b

    :param a: int starting fibonacci index
    :param b: int ending fibonacci index
    :return: the partial sum of fibonacci terms between a and b
    """
    if b <= 1:
        return b

    return (get_fibonacci_huge(b + 2, 10) - get_fibonacci_huge(a + 1, 10)) % 10


def main():
    data = sys.stdin.read()
    from_, to = map(int, data.split())
    print(fibonacci_partial_sum(from_, to))

if __name__ == '__main__':
    main()

