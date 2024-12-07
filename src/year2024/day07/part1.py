from src.common.common import get_lines
from itertools import product


def parse_line(line):
    result, numbers = line.split(':')
    return int(result), [int(x) for x in numbers.split()]


def main():
    lines = get_lines('')

    total = 0

    for line in lines:
        result, numbers = parse_line(line)

        for operators in product('+*', repeat=len(numbers) - 1):
            current_result = numbers[0]

            for i in range(len(numbers) - 1):
                match operators[i]:
                    case '*':
                        current_result *= numbers[i + 1]
                    case '+':
                        current_result += numbers[i + 1]

                if current_result > result:
                    break

            if current_result == result:
                # print('found', result, numbers, operators)
                total += result
                break

    print(total)


if __name__ == "__main__":
    main()
