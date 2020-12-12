from src.common.common import get_lines


def move(position, direction, distance):
    x, y = position
    if direction == 'N':
        return x + distance, y
    elif direction == 'E':
        return x, y + distance
    elif direction == 'W':
        return x, y - distance
    elif direction == 'S':
        return x - distance, y


def rotate(direction, rotation, degrees):
    degrees //= 90
    if rotation == 'L':
        degrees = -degrees

    directions = 'NESW'
    current = directions.index(direction)
    new = current + degrees

    if new >= len(directions):
        new %= len(directions)

    return directions[new]


def distance(start, end):
    x1, y1 = start
    x2, y2 = end
    return abs(x1 - x2) + abs(y1 - y2)


def parse_instruction(instruction):
    return instruction[0], int(instruction[1:])


lines = get_lines()

instructions = list(map(parse_instruction, lines))

position = 0, 0
direction = 'E'

for action, value in instructions:
    if action in 'NEWS':
        position = move(position, action, value)
    elif action in 'LR':
        direction = rotate(direction, action, value)
    elif action == 'F':
        position = move(position, direction, value)

print(distance((0, 0), position))
