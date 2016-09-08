#! python3
import sys
from fibonacci import calc_fib


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fibonacci_huge_improved(n, m):
    if n <= 1:
        return n
    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current % m, previous % m + current % m

    return current % m


def get_pisano_period(m):
    sequence = [0, 1]
    index = 1
    while True:
        sequence.append((sequence[index] + sequence[index - 1]) % m)
        index += 1

        if not (index + 1) % 2 and sequence[int(index / 2)] == sequence[index]:
            if sequence[:int((index + 1) / 2)] == sequence[int((index + 1) / 2):]:
                return int((index + 1) / 2)

    return -1


def get_fibonacci_huge(n, m):
    """
    Algorithm for computing the remainder of term n of the fibonacci sequence when divided by m

    :param n: int term to compute
    :param m: int divisor
    :return: int remainder of fibonacci sequence at n divided by m
    """
    if n <= 1:
        return n

    return calc_fib(n % get_pisano_period(m)) % m


def main():
    infile = sys.stdin.read()
    n, m = map(int, infile.split())
    print(get_fibonacci_huge(n, m))

if __name__ == '__main__':
    main()

