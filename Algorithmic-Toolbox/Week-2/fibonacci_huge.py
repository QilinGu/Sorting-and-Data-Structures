#! python3
import sys


def get_fibonacci_huge_naive(n):
    if n <= 1:
        return n
    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def get_fibonacci_huge(n):
    return get_fibonacci_huge_naive(n)


def main():
    infile = sys.stdin.read()
    n, m = map(int, infile.split())
    print(get_fibonacci_huge_naive(n))

if __name__ == '__main__':
    main()

