from src.common.common import get_lines


def prepare_grid(lines):
    length = len(lines)

    grid = []
    for w_index in range(length):
        grid.append([])
        for z_index in range(length):
            grid[w_index].append([])
            for row_index in range(length):
                grid[w_index][z_index].append([])
                for col in range(length):
                    grid[w_index][z_index][row_index].append(False)

    middle = length // 2
    middle = grid[middle][middle]

    for row_index, row in enumerate(lines):
        for col_index, col in enumerate(row):
            middle[row_index][col_index] = col == '#'

    return grid


def pad_grid(grid, padding):
    length = len(grid) + padding * 2

    new_grid = []

    new_grid.append([[[False] * length] * length] * length)

    for w_index in range(padding, length - padding):
        new_grid.append([])

        new_grid[w_index].append([[False] * length] * length)

        for z_index in range(padding, length - padding):
            new_grid[w_index].append([])

            new_grid[w_index][z_index].append([False] * length)

            for y_index in range(padding, length - padding):
                new_grid[w_index][z_index].append([False])

                for x_index in range(padding, length - padding):
                    old_value = grid[w_index - padding][z_index - padding][y_index - padding][x_index - padding]
                    new_grid[w_index][z_index][y_index].append(old_value)

                new_grid[w_index][z_index][y_index].append(False)

            new_grid[w_index][z_index].append([False] * length)

        new_grid[w_index].append([[False] * length] * length)

    new_grid.append([[[False] * length] * length] * length)

    return new_grid


def copy_grid(old_grid):
    new_grid = []
    for w_slice in old_grid:
        new_w_slice = []
        new_grid.append(new_w_slice)
        for z_slice in w_slice:
            new_z_slice = []
            new_w_slice.append(new_z_slice)
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

    def handle_z_slice(w_slice, z_index, skip_middle):
        active_neighbors = 0

        if 0 <= z_index < len(w_slice):
            z_slice = w_slice[z_index]
            active_neighbors += handle_row(z_slice, y - 1, False)
            active_neighbors += handle_row(z_slice, y, skip_middle)
            active_neighbors += handle_row(z_slice, y + 1, False)

        return active_neighbors

    w, z, y, x = position

    if w - 1 >= 0:
        w_slice = grid[w - 1]
        active_neighbors += handle_z_slice(w_slice, z - 1, False)
        active_neighbors += handle_z_slice(w_slice, z, False)
        active_neighbors += handle_z_slice(w_slice, z + 1, False)

    w_slice = grid[w]
    active_neighbors += handle_z_slice(w_slice, z - 1, False)
    active_neighbors += handle_z_slice(w_slice, z, True)
    active_neighbors += handle_z_slice(w_slice, z + 1, False)

    if w + 1 < len(grid):
        w_slice = grid[w + 1]
        active_neighbors += handle_z_slice(w_slice, z - 1, False)
        active_neighbors += handle_z_slice(w_slice, z, False)
        active_neighbors += handle_z_slice(w_slice, z + 1, False)

    return active_neighbors


def apply_rules(position, grid):
    w, z, y, x = position
    active_neighbors = fetch_neighbors_new((w, z, y, x), grid)
    if grid[w][z][y][x]:
        return active_neighbors in (2, 3)
    else:
        return active_neighbors == 3


def run_cycle(grid):
    new_grid = copy_grid(grid)
    for w_index, w_slice in enumerate(grid):
        for z_index, z_slice in enumerate(w_slice):
            for y_index, row in enumerate(z_slice):
                for x_index, col in enumerate(row):
                    new_grid[w_index][z_index][y_index][x_index] = apply_rules((w_index, z_index, y_index, x_index), grid)
    return new_grid


def flatten(matrix):
    return [item for row in matrix for item in row]


def print_grid(grid):
    def charactify(boolean):
        if boolean:
            return '#'
        else:
            return '.'

    for w, w_slice in enumerate(grid):
        for z, z_slice in enumerate(w_slice):
            if any(flatten(z_slice)):
                print()
                print(f"{z=}, {w=}")
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
    for w_slice in grid:
        for z_slice in w_slice:
            active += sum(flatten(z_slice))

    print(active)


if __name__ == "__main__":
    main()
