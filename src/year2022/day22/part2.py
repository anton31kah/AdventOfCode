import re
from src.common.common import get_lines


TEST_DATA = ''

DIRECTIONS = '>v<^'

REGIONS = {
    '': {
        'regions': [
            ' 12',
            ' 3 ',
            '45 ',
            '6  '
        ],
        'split': 50
    },
    'S': {
        'regions': [
            '  1 ',
            '234 ',
            '  56'
        ],
        'split': 4
    },
}
REGIONS = REGIONS[TEST_DATA]

WRAPS = {
    '': {
        1: {
            '>': (2, '<', lambda row, col: first_column(row)),
            'v': (3, '^', lambda row, col: first_row(col)),
            '<': (4, '<', lambda row, col: first_column(inverse_value(row))),
            '^': (6, '<', lambda row, col: first_column(col)),
        },
        2: {
            '>': (5, '>', lambda row, col: last_column(inverse_value(row))),
            'v': (3, '>', lambda row, col: last_column(col)),
            '<': (1, '>', lambda row, col: last_column(row)),
            '^': (6, 'v', lambda row, col: last_row(col)),
        },
        3: {
            '>': (2, 'v', lambda row, col: last_row(row)),
            'v': (5, '^', lambda row, col: first_row(col)),
            '<': (4, '^', lambda row, col: first_row(row)),
            '^': (1, 'v', lambda row, col: last_row(col)),
        },
        4: {
            '>': (5, '<', lambda row, col: first_column(row)),
            'v': (6, '^', lambda row, col: first_row(col)),
            '<': (1, '<', lambda row, col: first_column(inverse_value(row))),
            '^': (3, '<', lambda row, col: first_column(col)),
        },
        5: {
            '>': (2, '>', lambda row, col: last_column(inverse_value(row))),
            'v': (6, '>', lambda row, col: last_column(col)),
            '<': (4, '>', lambda row, col: last_column(row)),
            '^': (3, 'v', lambda row, col: last_row(col)),
        },
        6: {
            '>': (5, 'v', lambda row, col: last_row(row)),
            'v': (2, '^', lambda row, col: first_row(col)),
            '<': (1, '^', lambda row, col: first_row(row)),
            '^': (4, 'v', lambda row, col: last_row(col)),
        },
    },
    'S': {
        1: {
            '>': (6, '>', lambda row, col: last_column(inverse_value(row))),
            'v': (4, '^', lambda row, col: first_row(col)),
            '<': (3, '^', lambda row, col: first_row(row)),
            '^': (2, '^', lambda row, col: first_row(inverse_value(col))),
        },
        2: {
            '>': (3, '<', lambda row, col: first_column(row)),
            'v': (5, 'v', lambda row, col: last_row(inverse_value(col))),
            '<': (6, 'v', lambda row, col: last_row(inverse_value(row))),
            '^': (1, '^', lambda row, col: first_row(inverse_value(col))),
        },
        3: {
            '>': (4, '<', lambda row, col: first_column(row)),
            'v': (5, '<', lambda row, col: first_column(inverse_value(col))),
            '<': (2, '>', lambda row, col: last_column(row)),
            '^': (1, '<', lambda row, col: first_column(col)),
        },
        4: {
            '>': (6, '^', lambda row, col: first_row(inverse_value(row))),
            'v': (5, '^', lambda row, col: first_row(col)),
            '<': (3, '>', lambda row, col: last_column(row)),
            '^': (1, 'v', lambda row, col: last_row(col)),
        },
        5: {
            '>': (6, '<', lambda row, col: first_column(row)),
            'v': (2, 'v', lambda row, col: last_row(inverse_value(col))),
            '<': (3, 'v', lambda row, col: last_row(row)),
            '^': (4, 'v', lambda row, col: last_row(inverse_value(col))),
        },
        6: {
            '>': (1, '>', lambda row, col: last_column(inverse_value(row))),
            'v': (2, '<', lambda row, col: first_column(inverse_value(col))),
            '<': (5, '>', lambda row, col: last_column(row)),
            '^': (4, '>', lambda row, col: last_column(inverse_value(col))),
        },
    },
}
WRAPS = WRAPS[TEST_DATA]


def first_column(row):
    return row, 1


def last_column(row):
    return row, REGIONS['split']


def first_row(col):
    return 1, col


def last_row(col):
    return REGIONS['split'], col


def inverse_value(val):
    return REGIONS['split'] - val + 1


def normalize(point):
    row, col = point
    row = ((row - 1) % REGIONS['split']) + 1
    col = ((col - 1) % REGIONS['split']) + 1
    return row, col


def get_region(point):
    row, col = point
    row = ((row - 1) // REGIONS['split'])
    col = ((col - 1) // REGIONS['split'])
    return int(REGIONS['regions'][row][col])


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
    next_region, side, transformer = WRAPS[get_region(point)][direction]

    row, col = normalize(point)
    next_region_point = transformer(row, col)

    new_direction = DIRECTIONS[(DIRECTIONS.index(side) + 2) % len(DIRECTIONS)]

    return next(filter(lambda p: get_region(p) == next_region and normalize(p) == next_region_point, tiles)), new_direction


def main():
    lines = get_lines(TEST_DATA, strip=False)

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
                        togo, direction_change = wrap_point(current, direction, tiles | walls)
                        if togo in walls:
                            break
                        direction = direction_change
                    current = togo
            case 'R':
                direction = DIRECTIONS[(DIRECTIONS.index(direction) + 1) % len(DIRECTIONS)]
            case 'L':
                direction = DIRECTIONS[(DIRECTIONS.index(direction) - 1) % len(DIRECTIONS)]

        # print(step, current, direction, get_region(current))

    # print(current, direction)

    direction_value = DIRECTIONS.index(direction)
    print(1000 * current[0] + 4 * current[1] + direction_value)


if __name__ == "__main__":
    main()
