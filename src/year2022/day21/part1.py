import re
from src.common.common import get_lines


def perform(dependencies, func):
    def perform_internal(**kwargs):
        values = [kwargs[key] for key in dependencies]
        result = values[0]
        for v in values[1:]:
            result = func(result, v)
        return result

    return perform_internal


def add(dependencies):
    return perform(dependencies, lambda a, b: a + b)


def sub(dependencies):
    return perform(dependencies, lambda a, b: a - b)


def mul(dependencies):
    return perform(dependencies, lambda a, b: a * b)


def div(dependencies):
    return perform(dependencies, lambda a, b: a / b)


def parse_line(line):
    parts = re.findall(r'\w+|[+\-*\/]', line)
    match parts:
        case [result, number]:
            return result, int(number)
        case [result, dep1, '+', dep2]:
            return result, (add([dep1, dep2]), [dep1, dep2])
        case [result, dep1, '-', dep2]:
            return result, (sub([dep1, dep2]), [dep1, dep2])
        case [result, dep1, '*', dep2]:
            return result, (mul([dep1, dep2]), [dep1, dep2])
        case [result, dep1, '/', dep2]:
            return result, (div([dep1, dep2]), [dep1, dep2])


def solve(expressions, search):
    match expressions[search]:
        case int(res):
            return res
        case func, dependencies:
            return func(**{dep: solve(expressions, dep) for dep in dependencies})


def main():
    lines = get_lines('')

    expressions = {key: value for key, value in map(parse_line, lines)}

    result = solve(expressions, 'root')

    print(int(result))


if __name__ == "__main__":
    main()
