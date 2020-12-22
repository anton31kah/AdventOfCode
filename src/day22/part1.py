import itertools
from src.common.common import get_lines


def read_cards(lines):
    player1_cards, player2_cards = [], []

    flag = True

    for line in lines:
        if not line:
            flag = False
            continue
        if line.endswith(':'):
            continue
        if flag:
            player1_cards.append(int(line))
        else:
            player2_cards.append(int(line))

    return player1_cards, player2_cards


def calculate_score(cards):
    score = 0
    for multiply, card in enumerate(reversed(cards), start=1):
        score += multiply * card
    return score


def main():
    lines = get_lines()

    player1_cards, player2_cards = read_cards(lines)

    for round in itertools.count(start=1):
        if not player1_cards or not player2_cards:
            break
        
        c1 = player1_cards.pop(0)
        c2 = player2_cards.pop(0)

        if c1 > c2:
            player1_cards.extend([c1, c2])
        elif c2 > c1:
            player2_cards.extend([c2, c1])
        else:
            raise ValueError(f'ERROR {c1} == {c2}')
    
    if player1_cards:
        print(calculate_score(player1_cards))
    else:
        print(calculate_score(player2_cards))


if __name__ == "__main__":
    main()
