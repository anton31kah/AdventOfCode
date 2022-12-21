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


def eq(dependencies):
    def complex_solve(a, b):
        return round((b - a.real) / a.imag)

    def complex_solve_wrapper(a, b):
        return complex_solve(a, b) if type(a) is complex else complex_solve(b, a)

    return perform(dependencies, lambda a, b: complex_solve_wrapper(a, b))


def parse_line(line):
    parts = re.findall(r'\w+|[+\-*\/]', line)
    match parts:
        case ['root' as result, dep1, _, dep2]:
            return result, (eq([dep1, dep2]), [dep1, dep2])
        case ['humn' as result, _]:
            return result, 1j
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
        case x:
            return x


def main():
    lines = get_lines('')

    expressions = {key: value for key, value in map(parse_line, lines)}

    result = solve(expressions, 'root')

    print(result)


if __name__ == "__main__":
    main()
