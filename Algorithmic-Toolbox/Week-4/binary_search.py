#!python3
import sys


def binary_search(a, x):

    if x > a[len(a) - 1] or x < a[0]:
        return -1

    left, right = 0, len(a)
    while left <= right:
        mid = left + int((right - left) / 2)
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def linear_search(a, x):
    for i in a:
        if i == x:
            return i
    return -1


def main():
    in_data = sys.stdin.read()
    data = list(map(int, in_data.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x), end=' ')

if __name__ == '__main__':
    main()
