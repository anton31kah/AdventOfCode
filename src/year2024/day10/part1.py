from src.common.common import get_lines


def work(grid, current, zero):
    row, col = current
    value = grid[row][col]

    if value == 9:
        return [(zero, current)]
    
    neighbors = [
        (row + 1, col),
        (row - 1, col),
        (row, col + 1),
        (row, col - 1),
    ]

    total = []

    for neighbor in neighbors:
        neighbor_row, neighbor_col = neighbor
        if 0 <= neighbor_row < len(grid) and 0 <= neighbor_col < len(grid[0]):
            neighbor_value = grid[neighbor_row][neighbor_col]
            if neighbor_value == value + 1:
                total.extend(work(grid, neighbor, zero))
    
    return total


def main():
    lines = get_lines('')

    grid = [[None if cell == '.' else int(cell) for cell in line] for line in lines]

    total = set()

    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            pos = (row, col)
            if cell == 0:
                total.update(work(grid, pos, pos))

    print(len(total))


if __name__ == "__main__":
    main()
