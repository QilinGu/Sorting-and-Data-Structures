#! python3
def calc_fib_naive(n):
    """
    Naive algorithm for computing the fibonacci sequence using recursion

    :param n: int term to compute
    :return: int value of fibonacci sequence at n
    """
    if n <= 1:
        return n
    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fib(n):
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
        fib0, fib1 = fib1, fib0 + fib1
    return fib1


def main():
    n = int(input())
    print(calc_fib(n))

if __name__ == "__main__":
    main()
