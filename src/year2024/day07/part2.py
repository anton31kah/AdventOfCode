from concurrent.futures import ProcessPoolExecutor
from src.common.common import get_lines
import itertools
import math
from timeit import default_timer as timer


def parse_line(line):
    result, numbers = line.split(':')
    return int(result), [int(x) for x in numbers.split()]


def concat_numbers(a, b):
    return a * 10 ** (math.floor(math.log10(b)) + 1) + b


def find_proper_operators(target, numbers):
    for operators in itertools.product('+*|', repeat=len(numbers) - 1):
        result = numbers[0]

        for i in range(len(numbers) - 1):
            match operators[i]:
                case '*':
                    result *= numbers[i + 1]
                case '+':
                    result += numbers[i + 1]
                case '|':
                    result = concat_numbers(result, numbers[i + 1])

            if result > target:
                break

        if result == target:
            return operators

    return None


def solve_line(line):
    result, numbers = parse_line(line)

    return result if find_proper_operators(result, numbers) is not None else 0


def main():
    lines = get_lines('')

    total = 0

    start = timer()

    with ProcessPoolExecutor() as executor:
        for result in executor.map(solve_line, lines):
            total += result

    end = timer()

    print(total)

    print('took', end - start, 'seconds')


if __name__ == "__main__":
    main()
