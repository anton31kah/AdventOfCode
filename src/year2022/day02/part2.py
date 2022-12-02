from src.common.common import get_lines


ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'

WINS = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK
}

# faster to have a separate lookup dict
LOSSES = {
    PAPER: ROCK,
    SCISSORS: PAPER,
    ROCK: SCISSORS
}


def get_play(index):
    return [ROCK, PAPER, SCISSORS][index - 1]


def find_win(play):
    return WINS[play]


def find_loss(play):
    return LOSSES[play]


def calculate_score(opponent, myself):
    opponent_val = 'ABC'.index(opponent) + 1
    score = 'XYZ'.index(myself) * 3

    opponent_play = get_play(opponent_val)

    myself_play = None

    if score == 6:
        myself_play = find_win(opponent_play)
    elif score == 3:
        myself_play = opponent_play
    elif score == 0:
        myself_play = find_loss(opponent_play)

    myself_val = [ROCK, PAPER, SCISSORS].index(myself_play) + 1

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
