import string
from src.common.common import get_lines


def get_priority(letter):
    return string.ascii_letters.index(letter) + 1


def main():
    lines = get_lines()

    total = 0

    for line in lines:
        part1, part2 = line[:len(line)//2], line[len(line)//2:]
        common = set(part1) & set(part2)
        (common,) = common
        total += get_priority(common)

    print(total)


if __name__ == "__main__":
    main()
