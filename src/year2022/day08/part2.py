from src.common.common import get_lines


def to_grid(strings):
    return [[int(char) for char in line] for line in strings]


def transpose(matrix):
    return [*zip(*matrix)]


def main():
    lines = get_lines('')

    grid = to_grid(lines)

    max_score = -1

    for row_idx, row in enumerate(grid):
        for cell_idx, cell in enumerate(row):
            # print(f"{row_idx},{cell_idx} @ {cell}")

            visible_up = 0
            visible_down = 0
            visible_left = 0
            visible_right = 0

            for i in reversed(range(row_idx)):
                visible_up += 1
                # print(f"  up [{i},{cell_idx}] @ {grid[i][cell_idx]}")
                if grid[i][cell_idx] >= cell:
                    break

            for i in range(row_idx + 1, len(grid)):
                visible_down += 1
                # print(f"  down [{i},{cell_idx}] @ {grid[i][cell_idx]}")
                if grid[i][cell_idx] >= cell:
                    break

            for i in reversed(range(cell_idx)):
                visible_left += 1
                # print(f"  left [{row_idx},{i}] @ {grid[row_idx][i]}")
                if grid[row_idx][i] >= cell:
                    break

            for i in range(cell_idx + 1, len(row)):
                visible_right += 1
                # print(f"  right [{row_idx},{i}] @ {grid[row_idx][i]}")
                if grid[row_idx][i] >= cell:
                    break
            
            score = visible_up * visible_down * visible_left * visible_right
            # print(f" {score} [[{[visible_up, visible_down, visible_left, visible_right]}]]")

            max_score = max(max_score, score)

    print(max_score)


if __name__ == "__main__":
    main()
