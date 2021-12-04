from src.common.common import get_lines


def prepare_grid(lines):
    length = len(lines)

    grid = []
    for z_index in range(length):
        grid.append([])
        for row_index in range(length):
            grid[z_index].append([])
            for col in range(length):
                grid[z_index][row_index].append(False)

    middle = length // 2
    middle = grid[middle]

    for row_index, row in enumerate(lines):
        for col_index, col in enumerate(row):
            middle[row_index][col_index] = col == '#'

    return grid


def pad_grid(grid, padding):
    length = len(grid) + padding * 2

    new_grid = []

    new_grid.append([[False] * length] * length)

    for z_index in range(padding, length - padding):
        new_grid.append([])
        new_grid[z_index].append([False] * length)
        for row_index in range(padding, length - padding):
            new_grid[z_index].append([False])
            for col in range(padding, length - padding):
                new_grid[z_index][row_index].append(grid[z_index - padding][row_index - padding][col - padding])
            new_grid[z_index][row_index].append(False)
        new_grid[z_index].append([False] * length)

    new_grid.append([[False] * length] * length)

    return new_grid


def copy_grid(old_grid):
    new_grid = []
    for z_slice in old_grid:
        new_z_slice = []
        new_grid.append(new_z_slice)
        for row in z_slice:
            new_row = row[:]
            new_z_slice.append(new_row)
    return new_grid


def fetch_neighbors_new(position, grid):
    active_neighbors = 0

    def handle_row(z_slice, row_idx, skip_middle):
        active_neighbors = 0

        if 0 <= row_idx < len(grid):
            row = z_slice[row_idx]
            if x - 1 >= 0:
                active_neighbors += int(row[x - 1])

            if not skip_middle:
                active_neighbors += int(row[x])

            if x + 1 < len(grid):
                active_neighbors += int(row[x + 1])

        return active_neighbors

    z, y, x = position

    if z - 1 >= 0:
        z_slice = grid[z - 1]
        active_neighbors += handle_row(z_slice, y - 1, False)
        active_neighbors += handle_row(z_slice, y, False)
        active_neighbors += handle_row(z_slice, y + 1, False)

    z_slice = grid[z]
    active_neighbors += handle_row(z_slice, y - 1, False)
    active_neighbors += handle_row(z_slice, y, True)
    active_neighbors += handle_row(z_slice, y + 1, False)

    if z + 1 < len(grid):
        z_slice = grid[z + 1]
        active_neighbors += handle_row(z_slice, y - 1, False)
        active_neighbors += handle_row(z_slice, y, False)
        active_neighbors += handle_row(z_slice, y + 1, False)

    return active_neighbors


def apply_rules(position, grid):
    z, row, col = position
    active_neighbors = fetch_neighbors_new((z, row, col), grid)
    if grid[z][row][col]:
        return active_neighbors in (2, 3)
    else:
        return active_neighbors == 3


def run_cycle(grid):
    new_grid = copy_grid(grid)
    for z_index, z_slice in enumerate(grid):
        for row_index, row in enumerate(z_slice):
            for col_index, col in enumerate(row):
                new_grid[z_index][row_index][col_index] = apply_rules((z_index, row_index, col_index), grid)
    return new_grid


def flatten(matrix):
    return [item for row in matrix for item in row]


def print_grid(grid):
    def charactify(boolean):
        if boolean:
            return '#'
        else:
            return '.'

    for z, z_slice in enumerate(grid):
        if any(flatten(z_slice)):
            print()
            print(f"{z=}")
            for row in z_slice:
                print(''.join(map(charactify, row)))


def main():
    lines = get_lines()
    # lines = [
    #     '.#.',
    #     '..#',
    #     '###',
    # ]

    grid = prepare_grid(lines)
    # print('=' * 30, 'INITIAL')
    # print_grid(grid)

    cycles = 6
    for cycle in range(1, cycles + 1):
        grid = pad_grid(grid, 1)
        # print('=' * 30, 'AFTER PADDING', cycle)
        # print_grid(grid)
        grid = run_cycle(grid)
        # print('=' * 30, 'AFTER CYCLE', cycle)
        # print_grid(grid)

    active = 0
    for z_slice in grid:
        active += sum(flatten(z_slice))

    print(active)


if __name__ == "__main__":
    main()
