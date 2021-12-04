import re
from src.common.common import get_lines


def try_int(string):
    try:
        return int(string)
    except ValueError:
        return string


def calculate_expression(expression):
    stack = []

    for char in expression:
        stack.append(char)
        if char == ')':
            last = stack.pop()
            inner_expression = []
            while True:
                last = stack.pop()
                if last == '(':
                    break
                inner_expression.append(last)
            inner_expression = ''.join(reversed(inner_expression))
            inner_expression = calculate_expression(inner_expression)
            stack.append(str(inner_expression))

    tokens = [try_int(token) for token in re.split(r'\b', ''.join(stack)) if token != '']

    result = tokens[0]
    operation = None
    for token in tokens[1:]:
        if isinstance(token, int):
            if operation == '*':
                result *= token
            elif operation == '+':
                result += token
        else:
            operation = token

    return result


def main():
    lines = get_lines()

    lines = [line.replace(' ', '') for line in lines]

    total = sum(calculate_expression(line) for line in lines)
    print(total)


if __name__ == "__main__":
    main()
