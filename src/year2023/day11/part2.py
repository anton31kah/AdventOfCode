from src.common.common import get_lines


def parse_input(lines):
    galaxies = []

    for y, line in enumerate(lines):
        for x, point in enumerate(line):
            if point == '#':
                galaxies.append((x, y))
    
    return galaxies


def find_empty_rows_and_cols(lines):
    empty_rows = []
    empty_cols = []

    for y, line in enumerate(lines):
        if set(line) == {'.'}:
            empty_rows.append(y)

    for x in range(len(lines[0])):
        if {line[x] for line in lines} == {'.'}:
            empty_cols.append(x)

    return empty_rows, empty_cols


def expand_space(galaxies, empty_rows, empty_cols, expansion=2):
    new_galaxies = []

    for x, y in galaxies:
        x_diff = sum(expansion - 1 for col in empty_cols if x > col)
        y_diff = sum(expansion - 1 for row in empty_rows if y > row)
        new_x, new_y = x + x_diff, y + y_diff
        new_galaxies.append((new_x, new_y))

    return new_galaxies


def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return abs(x1 - x2) + abs(y1 - y2)


def main():
    lines = get_lines('')

    galaxies = parse_input(lines)
    empty_rows, empty_cols = find_empty_rows_and_cols(lines)

    galaxies = expand_space(galaxies, empty_rows, empty_cols, expansion=1000000)

    total = 0

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            total += distance(galaxies[i], galaxies[j])
    
    print(total)


if __name__ == "__main__":
    main()
