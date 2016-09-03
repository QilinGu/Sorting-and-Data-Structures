#! python3

import sys


def check_syntax(text):
    class Bracket:
        def __init__(self, bracket_type, position):
            self.bracket_type = bracket_type
            self.position = position

        def match(self, c):
            if self.bracket_type == '[' and c == ']':
                return True
            if self.bracket_type == '{' and c == '}':
                return True
            if self.bracket_type == '(' and c == ')':
                return True
            return False

    opening_brackets_stack = []
    for i, val in enumerate(text):
        if val == '(' or val == '[' or val == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(val, i))

        if val == ')' or val == ']' or val == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) > 0:
                bracket = opening_brackets_stack.pop()
                if not bracket.match(val):
                    return i + 1
            else:
                return i + 1

    if len(opening_brackets_stack) > 0:
        return opening_brackets_stack[0].position + 1

    return "Success"


def main():
    text = sys.stdin.read()

    print(check_syntax(text))


if __name__ == "__main__":
    main()