import string
from src.common.common import get_lines


def batch(lis, n=1):
    l = len(lis)
    for ndx in range(0, l, n):
        yield lis[ndx:min(ndx + n, l)]


def get_priority(letter):
    return string.ascii_letters.index(letter) + 1


def main():
    lines = get_lines()

    total = 0

    for [line1, line2, line3] in batch(lines, 3):
        common = set(line1) & set(line2) & set(line3)
        (common,) = common
        total += get_priority(common)

    print(total)


if __name__ == "__main__":
    main()
