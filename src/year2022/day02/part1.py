from src.common.common import get_lines


ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'


def get_play(index):
    return [ROCK, PAPER, SCISSORS][index - 1]


def calculate_score(opponent, myself):
    opponent_val = 'ABC'.index(opponent) + 1
    myself_val = 'XYZ'.index(myself) + 1

    opponent_play = get_play(opponent_val)
    myself_play = get_play(myself_val)

    score = 0

    if opponent_play == myself_play:
        score = 3
    elif opponent_play == ROCK and myself_play == PAPER:
        score = 6
    elif opponent_play == SCISSORS and myself_play == ROCK:
        score = 6
    elif opponent_play == PAPER and myself_play == SCISSORS:
        score = 6

    return myself_val + score


def main():
    lines = get_lines()

    total = 0

    for line in lines:
        opponent, myself = line.split()
        total += calculate_score(opponent, myself)

    print(total)


if __name__ == "__main__":
    main()
