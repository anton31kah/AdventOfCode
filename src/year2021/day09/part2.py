from functools import reduce
from src.common.common import get_lines


def get_at_safe(heightmap, row, col):
    if 0 <= row < len(heightmap) and 0 <= col < len(heightmap[row]):
        return heightmap[row][col]
    return None


def adjacent(heightmap, row, col):
    result = []
    if (up := get_at_safe(heightmap, row - 1, col)) is not None:
        result.append(((row - 1, col), up))
    if (down := get_at_safe(heightmap, row + 1, col)) is not None:
        result.append(((row + 1, col), down))
    if (left := get_at_safe(heightmap, row, col - 1)) is not None:
        result.append(((row, col - 1), left))
    if (right := get_at_safe(heightmap, row, col + 1)) is not None:
        result.append(((row, col + 1), right))
    return result


def find_basin(heightmap, row, col):
    result = set()

    queue = {(row, col)}

    while queue:
        position = queue.pop()

        if position in result:
            continue

        adjacent_list = adjacent(heightmap, *position)

        for adj_position, value in adjacent_list:
            if value < 9:
                queue.add(adj_position)

        result.add(position)

    return result


def main():
    lines = get_lines()

    heightmap = [[int(c) for c in line] for line in lines]

    basins = []

    for row_idx, row in enumerate(heightmap):
        for col_idx, col in enumerate(row):
            adjacent_list = adjacent(heightmap, row_idx, col_idx)
            if col < min(value for position, value in adjacent_list):
                basin = find_basin(heightmap, row_idx, col_idx)
                basins.append(len(basin))

    print(reduce(lambda a, b: a * b, sorted(basins, reverse=True)[:3], 1))


if __name__ == "__main__":
    main()
