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

            if (row, col) in anti_nodes:
                to_print = '#'

            print(to_print, end='')

        print()

    print()
    print()


def main():
    lines = get_lines('')

    grid = parse_grid(lines)

    anti_nodes = set()

    for antenna_type, nodes in grid.items():
        for (x1, y1), (x2, y2) in combinations(nodes, 2):
            dx = x2 - x1
            dy = y2 - y1
            anti1 = x1 - dx, y1 - dy
            anti2 = x2 + dx, y2 + dy
            # print('for antenna', antenna_type, 'nodes', (x1, y1), (x2, y2), 'dx', dx, 'dy', dy, 'found', anti1, 'in bounds' if in_bounds(lines, anti1) else 'out of bounds', anti2, 'in bounds' if in_bounds(lines, anti2) else 'out of bounds')
            if in_bounds(lines, anti1):
                anti_nodes.add(anti1)
            if in_bounds(lines, anti2):
                anti_nodes.add(anti2)
        
        # print('finished with', antenna_type)
        # print_grid(grid, anti_nodes, lines)

    print(len(anti_nodes))


if __name__ == "__main__":
    main()
