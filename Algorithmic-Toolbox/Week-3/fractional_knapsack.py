#! python3
import sys


def get_optimal_value(capacity, weights, values):

    if len(weights) != len(values):
        return -1.

    # compute value per weight
    value = 0.
    density = []
    for x in range(len(weights)):
        density.append(values[x] / weights[x])

    pairing = sorted(list(zip(density, weights)), reverse=True)

    # Compute max loot with at most one of each full item
    for item in pairing:
        if item[1] >= capacity:
            value += capacity * item[0]
            break
        value += item[1] * item[0]
        capacity -= item[1]

    return value


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

if __name__ == "__main__":
    main()

