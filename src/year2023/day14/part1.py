from src.common.common import get_lines
from collections import deque


def parse_input(lines):
    solid = []
    round = []
    for y, line in enumerate(lines):
        for x, rock in enumerate(line):
            match rock:
                case '#':
                    solid.append((x, y))
                case 'O':
                    round.append((x, y))
    return solid, round


def print_rocks(solid, round, width, height):
    for y in range(height):
        for x in range(width):
            if (x, y) in solid:
                print('#', end='')
            elif (x, y) in round:
                print('O', end='')
            else:
                print('.', end='')
        print()


def tilt_north(solid, round, width):
    solid = set(solid)
    round = deque(round)

    columns_lower_boundry = []
    for i in range(width):
        columns_lower_boundry.append(-1)

    new_round = []

    while round:
        x, y = round.popleft()
        while y > columns_lower_boundry[x] and (x, y - 1) not in solid and y - 1 >= 0:
            y -= 1
        new_round.append((x, y))
        solid.add((x, y))
        columns_lower_boundry[x] = y
    
    return new_round


def score(round, height):
    score = 0
    for h in range(height - 1, -1, -1):
        for x, y in round:
            if y == h:
                score += height - h
    return score


def main():
    lines = get_lines('')
    width, height = len(lines[0]), len(lines)
    solid, round = parse_input(lines)
    new_round = tilt_north(solid, round, width)
    print(score(new_round, height))


if __name__ == "__main__":
    main()
