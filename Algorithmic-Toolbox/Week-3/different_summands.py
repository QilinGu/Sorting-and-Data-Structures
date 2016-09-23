#! python3
import sys


def optimal_summands(n):
    summands = []
    if n <= 2:
        summands.append(n)
        return summands

    val = 1
    while n > 0:
        # Make last summand the remainder of the pool
        if n - val <= val:
            summands.append(n)
            n = 0
        else:
            summands.append(val)
            n -= val
            val += 1

    return summands


def main():
    val = sys.stdin.read()
    n = int(val)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

if __name__ == '__main__':
    main()
