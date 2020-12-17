from src.common.common import get_lines


def prepare_grid(lines, cycles):
    length = len(lines) + cycles * 2

    grid = []
    for z_index in range(length):
        grid.append([])
        for row_index in range(length):
            grid[z_index].append([])
            for col in range(length):
                grid[z_index][row_index].append(False)

    starting_position = len(grid) // 2 - len(lines) // 2
    x, y, z = starting_position, starting_position, starting_position

    lines_i = 0
    lines_j = 0
    for row in range(y, y + len(lines)):
        lines_j = 0
        for col in range(x, x + len(lines)):
            grid[z][row][col] = lines[lines_i][lines_j] == '#'
            lines_j += 1
        lines_i += 1

    return grid


def copy_grid(old_grid):
    new_grid = []
    for z_slice in old_grid:
        new_z_slice = []
        new_grid.append(new_z_slice)
        for row in z_slice:
            new_row = row[:]
            new_z_slice.append(new_row)
    return new_grid


def fetch_neighbors(position, grid):
    neighbors = []

    def handle_row(z_slice, row_idx, skip_middle):
        if y - 1 < 0:
            neighbors.extend([False] * (3 if not skip_middle else 2))
        else:
            row = z_slice[y - 1]
            if x - 1 < 0:
                neighbors.append(False)
            else:
                neighbors.append(row[x - 1])
            
            if not skip_middle:
                neighbors.append(row[x])

            if x + 1 >= len(grid):
                neighbors.append(False)
            else:
                neighbors.append(row[x + 1])

    z, y, x = position

    if z - 1 < 0:
        neighbors.extend([False] * 9)
    else:
        z_slice = grid[z - 1]
        handle_row(z_slice, y - 1, False)
        handle_row(z_slice, y, False)
        handle_row(z_slice, y + 1, False)

    z_slice = grid[z]
    handle_row(z_slice, y - 1, False)
    handle_row(z_slice, y, True)
    handle_row(z_slice, y + 1, False)

    if z + 1 >= len(grid):
        neighbors.extend([False] * 9)
    else:
        z_slice = grid[z + 1]
        handle_row(z_slice, y - 1, False)
        handle_row(z_slice, y, False)
        handle_row(z_slice, y + 1, False)

    return neighbors


def apply_rules(position, grid):
    z, row, col = position
    neighbors = fetch_neighbors((z, row, col), grid)
    active_neighbors = sum(neighbors)
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
            print(f"{z=}")
            for row in z_slice:
                print(''.join(map(charactify, row)))


def main():
    lines = get_lines()
    lines = [
        '.#.',
        '..#',
        '###',
    ]

    cycles = 6
    grid = prepare_grid(lines, cycles)
    print_grid(grid)
    print('=' * 30)

    for cycle in range(1, cycles + 1):
        grid = run_cycle(grid)
        print_grid(grid)
        print('=' * 30)

    active = 0
    for z_slice in grid:
        active += sum(flatten(z_slice))
    
    print(active)


if __name__ == "__main__":
    main()

# src.day17.part1
