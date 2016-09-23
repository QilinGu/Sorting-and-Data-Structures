#! python3

import sys


def largest_number(a):
    """
    Assemble list of string numbers such that the resulting number is maximized

    :param a: list of string integers
    :return: str representing maximum number
    """
    answer = ""
    while len(a) > 0:
        max_digit = a[0]
        for val in a[1:]:
            if greater_or_equal(val, max_digit):
                max_digit = val

        answer += max_digit
        a.remove(max_digit)

    return answer


def greater_or_equal(a, b):
    """
    Return True if a should come before b and false otherwise
    :param a:
    :param b:
    :return:
    """
    if a == b:
        return True
    elif a[0] > b[0]:
        return True
    elif a[0] < b[0]:
        return False
    elif a[len(a) - 1] >= b[len(b) - 1] and len(a) <= len(b):
        return True
    else:
        return False


def greater_or_equal2(a, b):
    """
    Return True if a should come before b and false otherwise
    :param a:
    :param b:
    :return:
    """
    if a == b:
        return True
    elif a[0] > b[0]:
        return True
    elif a[0] < b[0]:
        return False
    else:
        return False


def test_by_stress(start, limit):
    for i in range(start, limit):
        for j in range(start, limit):
            for k in range(start, limit):
                for l in range(start, limit):
                    if i == k:
                        a = str(i) + str(j)
                        b = str(k) + str(l)
                        print("a: %s, b: %s, res: %s" % (a, b, greater_or_equal(a, b)))

def main():
    vals = sys.stdin.read()
    data = vals.split()
    a = data[1:]
    print(largest_number(a))

if __name__ == '__main__':
    # main()
    test_by_stress(7, 10)

