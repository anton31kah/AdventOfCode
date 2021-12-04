from collections import Counter
from src.common.common import get_lines


def join(delimiter=""):
    def inner_joiner(items):
        return delimiter.join(items)

    return inner_joiner


def transpose(lines):
    return list(map(join(), zip(*lines)))


def bit_not(n, numbits=8):
    return (1 << numbits) - 1 - n


def examine(numbers, search):
    for step in range(len(numbers[0])):
        transposed = transpose(numbers)

        data = Counter(transposed[step])

        if search == 'oxygen':
            bit = data.most_common(1)[0][0]
        else:
            bit = data.most_common()[-1][0]

        if data['1'] == data['0']:
            bit = '1' if search == 'oxygen' else '0'

        numbers = [number for number in numbers if number[step] == bit]

    return numbers


def main():
    lines = get_lines()

    oxygen_numbers = examine(lines[:], 'oxygen')
    co2_numbers = examine(lines[:], 'co2')

    oxygen = int(oxygen_numbers[0], base=2)
    co2 = int(co2_numbers[0], base=2)

    life_support_rating = oxygen * co2

    print(life_support_rating)


if __name__ == "__main__":
    main()
