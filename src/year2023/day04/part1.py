from src.common.common import get_lines
import re


def parse_line(line):
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    id_part, numbers_part = line.split(': ')

    card_id = int(re.split(r'\s+', id_part)[1])

    winning_part, own_part = numbers_part.split(' | ')

    winning = [int(x) for x in re.split(r'\s+', winning_part.strip())]
    own = [int(x) for x in re.split(r'\s+', own_part.strip())]

    return card_id, winning, own


def main():
    lines = get_lines('')

    total = 0

    for line in lines:
        card_id, winning, own = parse_line(line)
        count = len(set(winning).intersection(set(own)))
        if count > 0:
            total += (2 ** (count - 1))

    print(total)


if __name__ == "__main__":
    main()
