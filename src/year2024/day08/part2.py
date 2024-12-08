from src.common.common import get_lines
from collections import defaultdict
from itertools import combinations


def parse_grid(lines):
    result = defaultdict(list)
    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            if cell != '.':
                result[cell].append((row, col))
    return result


def in_bounds(lines, position):
    x, y = position
    return 0 <= x < len(lines) and 0 <= y < len(lines[0])


def print_grid(grid, anti_nodes, lines):
    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            to_print = cell

            if (row, col) in anti_nodes and cell == '.':
                to_print = '#'

            print(to_print, end='')

        print()

    print()
    print()


def calculate_anti_position(position, delta, sign):
    x, y = position
    dx, dy = delta
    match sign:
        case '-':
            return x - dx, y - dy
        case '+':
            return x + dx, y + dy
    raise ValueError(f'invalid sign {sign}')


def main():
    lines = get_lines('')

    grid = parse_grid(lines)

    anti_nodes = set()

    for antenna_type, nodes in grid.items():
        for (x1, y1), (x2, y2) in combinations(nodes, 2):
            dx = x2 - x1
            dy = y2 - y1

            added = 0

            anti1 = calculate_anti_position((x1, y1), (dx, dy), '-')
            while in_bounds(lines, anti1):
                anti_nodes.add(anti1)
                anti1 = calculate_anti_position(anti1, (dx, dy), '-')
                added += 1

            anti2 = calculate_anti_position((x2, y2), (dx, dy), '+')
            while in_bounds(lines, anti2):
                anti_nodes.add(anti2)
                anti2 = calculate_anti_position(anti2, (dx, dy), '+')
                added += 1
            
            if added >= 1:
                anti_nodes.add((x1, y1))
                anti_nodes.add((x2, y2))
    
        print('finished with', antenna_type)
        print_grid(grid, anti_nodes, lines)

    # print_grid(grid, anti_nodes, lines)

    print(len(anti_nodes))


if __name__ == "__main__":
    main()
