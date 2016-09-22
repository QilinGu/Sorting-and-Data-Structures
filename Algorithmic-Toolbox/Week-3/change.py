#! python3
import sys


def get_change(m):
    """
    Calculates the number of coins needed to issue change

    :param m: int amount of change to issue
    :return: minimum number of coins needed for the change
    """
    count = 0
    coins = (10, 5, 1)
    for coin in coins:
        if m >= coin:
            num_coins = int(m / coin)
            m -= num_coins * coin
            count += num_coins
    return count


def main():
    m = int(sys.stdin.read())
    print(get_change(m))

if __name__ == '__main__':
    main()
