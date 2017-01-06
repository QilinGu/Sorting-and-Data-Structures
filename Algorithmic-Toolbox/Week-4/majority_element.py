#!python3
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    count = 0
    common = 0
    for val in a:
        if count == 0:
            common = val

        if val == common:
            count += 1
        else:
            count -= 1

    count = 0
    for val in a:
        if val == common:
            count += 1

        if count > int(len(a) / 2):
            return 1

    return -1


def main():
    in_data = sys.stdin.read()
    n, *a = list(map(int, in_data.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

if __name__ == '__main__':
    main()