#! python3
import sys
from fibonacci_sum_last_digit import fibonacci_sum


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
    return fibonacci_sum(b) - fibonacci_sum(a)

def fibonacci_partial_sum2(a, b):
    pass


def main():
    data = sys.stdin.read()
    from_, to = map(int, data.split())
    print(fibonacci_partial_sum(from_, to))


def testing():
    n_vals = ""
    test_vals = ""
    naive_vals = ""
    a_vals = ""
    b_vals = ""
    for val in range(5, 100):
        n_vals += str(val) + " "
        test_vals += str(fibonacci_partial_sum(5, val)) + " " * len(str(val))
        naive_vals += str(fibonacci_partial_sum_naive(5, val)) + " " * len(str(val))
        a_vals += str(fibonacci_sum(5)) + " " * len(str(val))
        b_vals += str(fibonacci_sum(val)) + " " * len(str(val))

    # Stress test:
    for i in range(0, 100):
        for j in range(0, 100):
            normal = fibonacci_partial_sum(i, j)
            naive = fibonacci_partial_sum_naive(i, j)
            if normal == naive:
                print("match at %s and %s -- %s vs %s" % (i, j, normal, naive))
            else:
                print("-------->%s and %s -- %s vs %s" % (i, j, normal, naive))

    # print(n_vals)
    # print(test_vals)
    # print(a_vals)
    # print(b_vals)
    # print(naive_vals)
    # print(test_vals == naive_vals)

if __name__ == '__main__':
    testing()
