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

    copies = {} # card_id -> copies

    for line in lines:
        card_id, winning, own = parse_line(line)
        # print('>>>', card_id)
        count = int(len(set(winning).intersection(set(own))))
        copies_for_card = copies.get(card_id, 0) + 1
        # print(count, copies_for_card)
        if count >= 0:
            for x in range(count):
                id = x + card_id + 1
                if id not in copies:
                    copies[id] = copies_for_card
                else:
                    copies[id] += copies_for_card
        # print(copies)
        total += copies_for_card

    print(total)


if __name__ == "__main__":
    main()
