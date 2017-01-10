#!python3
import sys
import random


def partition3(a, left, right):
    #write your code here
    pivot_1 = a[left]
    pivot_2 = a[right]
    idx_1, idx_2 = left, right

    for idx in range(left + 1, right + 1):
        if a[idx] <= pivot_1:
            idx_1 += 1
            a[idx], a[idx_1] = a[idx_1], a[idx]

        if a[idx] >= pivot_2:
            idx_2 -= 1
            a[idx], a[idx_2] = a[idx_2], a[idx]

    if a[idx_1] < a[idx_2]:
        a[left], a[idx_1] = a[idx_1], a[left]
        a[left + 1], a[idx_2] = a[idx_2], a[left + 1]
        return idx_1, idx_2
    else:
        a[left], a[idx_2] = a[idx_2], a[left]
        a[left + 1], a[idx_1] = a[idx_1], a[left + 1]
        return idx_2, idx_1


def partition2(a, left, right):
    pivot = a[left]
    pivot_idx = left

    for idx in range(left + 1, right + 1):
        if a[idx] <= pivot:
            pivot_idx += 1
            a[idx], a[pivot_idx] = a[pivot_idx], a[idx]

    a[left], a[pivot_idx] = a[pivot_idx], a[left]
    return pivot_idx


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1)
    randomized_quick_sort(a, m + 1, r)


def quick_sort(a, left, right):
    if left >= right:
        return
    idx_left, idx_right = partition3(a, left, right)
    quick_sort(a, left, idx_left - 1)
    quick_sort(a, idx_left + 1, idx_right - 1)
    quick_sort(a, idx_right + 1, right)


def main():
    in_data = sys.stdin.read()
    n, *a = list(map(int, in_data.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

if __name__ == '__main__':
    #main()
    test = [5,4,3,6,2,1,3,8]
    test2 = [5,4,3,6,2,1,3,8]
    # print(test)
    # partition2(test, 0, len(test) - 1)
    # print(test)
    # partition2math(test2, 0, len(test2) - 1)
    # print(test2)
    print(test)
    quick_sort(test, 0, len(test) - 1)
    randomized_quick_sort(test2, 0, len(test2) - 1)
    print(test)
    print(test2)
