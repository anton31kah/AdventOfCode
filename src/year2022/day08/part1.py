from src.common.common import get_lines


def to_grid(strings):
    return [[int(char) for char in line] for line in strings]


def transpose(matrix):
    return [*zip(*matrix)]


def find_from_top(grid):
    from_top = []

    from_top_max = grid[0][:]
    for row in grid:
        from_top_row = []
        for idx, cell in enumerate(row):
            from_top_max[idx] = max(from_top_max[idx], cell)
            from_top_row.append(from_top_max[idx])
        from_top.append(from_top_row)

    return from_top


def find_from_bottom(grid):
    from_bottom = []

    from_bottom_max = grid[-1][:]
    for row in reversed(grid):
        from_bottom_row = []
        for idx, cell in enumerate(row):
            from_bottom_max[idx] = max(from_bottom_max[idx], cell)
            from_bottom_row.append(from_bottom_max[idx])
        from_bottom.append(from_bottom_row)

    return list(reversed(from_bottom))


def find_from_left_and_right(grid):
    from_left = []
    from_right = []

    for row in grid:
        from_left_row = []
        from_left_max = row[0]
        for cell in row:
            from_left_max = max(from_left_max, cell)
            from_left_row.append(from_left_max)
        from_left.append(from_left_row)

        from_right_row = []
        from_right_max = row[-1]
        for cell in reversed(row):
            from_right_max = max(from_right_max, cell)
            from_right_row.append(from_right_max)
        from_right.append(list(reversed(from_right_row)))

    return from_left, from_right


def main():
    lines = get_lines('')

    grid = to_grid(lines)

    from_top = find_from_top(grid)
    from_bottom = find_from_bottom(grid)
    from_left, from_right = find_from_left_and_right(grid)

    visible = 0

    for row_idx, row in enumerate(grid):
        for cell_idx, cell in enumerate(row):
            if row_idx == 0 or row_idx == len(grid) - 1 or cell_idx == 0 or cell_idx == len(row) - 1:
                visible += 1
                # print(row_idx, cell_idx, cell)
                continue

            if from_top[row_idx - 1][cell_idx] < cell:
                visible += 1
                # print(row_idx, cell_idx, cell)
                continue

            if from_bottom[row_idx + 1][cell_idx] < cell:
                visible += 1
                # print(row_idx, cell_idx, cell)
                continue

            if from_left[row_idx][cell_idx - 1] < cell:
                visible += 1
                # print(row_idx, cell_idx, cell)
                continue

            if from_right[row_idx][cell_idx + 1] < cell:
                visible += 1
                # print(row_idx, cell_idx, cell)
                continue

    print(visible)


if __name__ == "__main__":
    main()
