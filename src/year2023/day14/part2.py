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


def string_rocks(solid, round, width, height):
    result = []
    for y in range(height):
        line = []
        for x in range(width):
            if (x, y) in solid:
                line.append('#')
            elif (x, y) in round:
                line.append('O')
            else:
                line.append('.')
        result.append(''.join(line))
    return '\n'.join(result)


def tilt_north(solid, round, width, height):
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
    
    return list(sorted(new_round))


def tilt_south(solid, round, width, height):
    solid = set(solid)
    round = deque(list(reversed(round)))

    columns_upper_boundry = []
    for i in range(width):
        columns_upper_boundry.append(height)

    new_round = []

    while round:
        x, y = round.popleft()
        while y < columns_upper_boundry[x] and (x, y + 1) not in solid and y + 1 < height:
            y += 1
        new_round.append((x, y))
        solid.add((x, y))
        columns_upper_boundry[x] = y
    
    return list(sorted(new_round))


def tilt_west(solid, round, width, height):
    solid = set(solid)
    round = deque(round)

    columns_boundry = []
    for i in range(height):
        columns_boundry.append(-1)

    new_round = []

    while round:
        x, y = round.popleft()
        while x > columns_boundry[y] and (x - 1, y) not in solid and x - 1 >= 0:
            x -= 1
        new_round.append((x, y))
        solid.add((x, y))
        columns_boundry[y] = x
    
    return list(sorted(new_round))


def tilt_east(solid, round, width, height):
    solid = set(solid)
    round = deque(list(reversed(round)))

    columns_boundry = []
    for i in range(height):
        columns_boundry.append(width)

    new_round = []

    while round:
        x, y = round.popleft()
        while x < columns_boundry[y] and (x + 1, y) not in solid and x + 1 < width:
            x += 1
        new_round.append((x, y))
        solid.add((x, y))
        columns_boundry[y] = x
    
    return list(sorted(new_round))


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

    state = {}

    for cycle in range(1000000000):
        round = tilt_north(solid, round, width, height)
        round = tilt_west(solid, round, width, height)
        round = tilt_south(solid, round, width, height)
        round = tilt_east(solid, round, width, height)
        # rocks_state = string_rocks(solid, round, width, height)
        rocks_score = score(round, height)
        if rocks_score not in state:
            state[rocks_score] = []
        state[rocks_score].append(cycle)
        print(cycle, len(state), rocks_score)
        if cycle > 600:
            break

    """
    observation during analysis: after 115 every 14 scores start repeating
    """

    cycle = 116

    pattern = {
        116: 94253,
        117: 94245,
        118: 94255,
        119: 94263,
        120: 94278,
        121: 94295,
        122: 94312,
        123: 94313,
        124: 94315,
        125: 94309,
        126: 94302,
        127: 94283,
        128: 94269,
        129: 94258,
    }

    print(pattern[cycle + 1 + (1000000000%129%14)])


if __name__ == "__main__":
    main()
