from src.common.common import get_lines


def read_grid(lines):
    return [[int(col) for col in line] for line in lines]


def get_at_safe(grid, row, col):
    if 0 <= row < len(grid) and 0 <= col < len(grid[row]):
        return grid[row][col]
    return None


def adjacent(grid, row, col):
    adjacent_points = [
        (row - 1, col - 1),
        (row - 1, col),
        (row - 1, col + 1),
        (row, col - 1),
        (row, col + 1),
        (row + 1, col - 1),
        (row + 1, col),
        (row + 1, col + 1),
    ]

    result = []

    for point in adjacent_points:
        if (value := get_at_safe(grid, *point)) is not None:
            result.append((point, value))

    return result


def simulate_step(grid):
    initial_ready_to_flash = []

    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            row[col_idx] += 1
            if row[col_idx] > 9:
                initial_ready_to_flash.append((row_idx, col_idx))

    flashed = []
    ready_to_flash = [*initial_ready_to_flash]

    while ready_to_flash:
        position = ready_to_flash.pop(0)

        if position in flashed:
            continue

        adjacent_list = adjacent(grid, *position)

        for (row_idx, col_idx), value in adjacent_list:
            grid[row_idx][col_idx] += 1
            new_value = grid[row_idx][col_idx]
            if new_value > 9:
                ready_to_flash.append((row_idx, col_idx))

        flashed.append(position)

    for (row_idx, col_idx) in flashed:
        grid[row_idx][col_idx] = 0

    return grid, len(flashed)


def print_grid(grid, step):
    print(f"After step {step + 1}:" if step is not None else "Before any steps:")

    for row in grid:
        print(''.join((map(str, row))))

    print()


def main():
    lines = get_lines()
    # lines = [
    #     "11111",
    #     "19991",
    #     "19191",
    #     "19991",
    #     "11111",
    # ]

    grid = read_grid(lines)

    # print_grid(grid, step=None)

    total_flashed = 0

    for step in range(100):
        grid, flashed_count = simulate_step(grid)
        total_flashed += flashed_count

        # if step < 10 or step % 10 == 0:
        #     print_grid(grid, step)

    print(total_flashed)


if __name__ == "__main__":
    main()
