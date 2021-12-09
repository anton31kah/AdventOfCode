from src.common.common import get_lines


def get_at_safe(array, idx):
    if array is None:
        return None
    if 0 <= idx < len(array):
        return array[idx]
    return None


def adjacent(heightmap, row, col):
    result = []
    if (up := get_at_safe(get_at_safe(heightmap, row - 1), col)) is not None:
        result.append(up)
    if (down := get_at_safe(get_at_safe(heightmap, row + 1), col)) is not None:
        result.append(down)
    if (left := get_at_safe(get_at_safe(heightmap, row), col - 1)) is not None:
        result.append(left)
    if (right := get_at_safe(get_at_safe(heightmap, row), col + 1)) is not None:
        result.append(right)
    return result


def main():
    lines = get_lines()

    heightmap = [[int(c) for c in line] for line in lines]

    total = 0

    for row_idx, row in enumerate(heightmap):
        for col_idx, col in enumerate(row):
            adjacent_values = adjacent(heightmap, row_idx, col_idx)
            if col < min(adjacent_values):
                # print(row_idx, col_idx, col)
                total += col + 1

    print(total)


if __name__ == "__main__":
    main()
