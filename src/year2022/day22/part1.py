import re
from src.common.common import get_lines


def parse_grid(lines):
    tiles = set()
    walls = set()

    steps = []

    for row, line in enumerate(lines, start=1):
        steps = re.findall(r'\d+|[A-Z]+', line)

        for col, cell in enumerate(line, start=1):
            match cell:
                case '.':
                    tiles.add((row, col))
                case '#':
                    walls.add((row, col))

    steps = [int(step) if step.isdigit() else step for step in steps]

    return tiles, walls, steps


def next_point(point, direction):
    row, col = point
    match direction:
        case '>':
            return row, col + 1
        case 'v':
            return row + 1, col
        case '<':
            return row, col - 1
        case '^':
            return row - 1, col


def wrap_point(point, direction, tiles):
    row, col = point
    match direction:
        case '>':
            return min(filter(lambda t: t[0] == row, tiles), key=lambda t: t[1])
        case 'v':
            return min(filter(lambda t: t[1] == col, tiles), key=lambda t: t[0])
        case '<':
            return max(filter(lambda t: t[0] == row, tiles), key=lambda t: t[1])
        case '^':
            return max(filter(lambda t: t[1] == col, tiles), key=lambda t: t[0])


def main():
    lines = get_lines('', strip=False)

    DIRECTIONS = '>v<^'

    tiles, walls, steps = parse_grid(lines)

    current = min(tiles)
    direction = '>'

    for step in steps:
        match step:
            case int(moves):
                for _ in range(moves):
                    togo = next_point(current, direction)
                    if togo in walls:
                        break
                    if togo not in tiles:
                        togo = wrap_point(togo, direction, tiles | walls)
                        if togo in walls:
                            break
                    current = togo
            case 'R':
                direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % len(DIRECTIONS)]
            case 'L':
                direction = DIRECTIONS[(DIRECTIONS.index(direction) - 1) % len(DIRECTIONS)]

        # print(step, current, direction)

    # print(current, direction)

    direction_value = DIRECTIONS.index(direction)
    print(1000 * current[0] + 4 * current[1] + direction_value)


if __name__ == "__main__":
    main()
