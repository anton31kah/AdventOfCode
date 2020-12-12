from src.common.common import get_lines


def move(position, direction, distance):
    x, y = position
    if direction == 'N':
        return x, y - distance
    elif direction == 'E':
        return x + distance, y
    elif direction == 'W':
        return x - distance, y
    elif direction == 'S':
        return x, y + distance


def rotate(position, rotation, degrees):
    x, y = position
    if degrees == 180:
        return -x, -y

    clockwise = rotation == 'R' and degrees == 90 \
             or rotation == 'L' and degrees == 270

    if clockwise:
        return -y, x
    else:
        return y, -x


def forward(position, dxdy, multiple):
    x, y = position

    dx, dy = dxdy
    dx, dy = dx * multiple, dy * multiple

    return x + dx, y + dy


def distance(start, end):
    x1, y1 = start
    x2, y2 = end
    return abs(x1 - x2) + abs(y1 - y2)


def parse_instruction(instruction):
    return instruction[0], int(instruction[1:])


lines = get_lines()

instructions = list(map(parse_instruction, lines))

ship = 0, 0
waypoint = 10, -1

for action, value in instructions:
    if action in 'NEWS':
        waypoint = move(waypoint, action, value)
    elif action in 'LR':
        waypoint = rotate(waypoint, action, value)
    elif action == 'F':
        ship = forward(ship, waypoint, value)

print(distance((0, 0), ship))
