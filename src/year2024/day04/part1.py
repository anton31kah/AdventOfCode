from src.common.common import get_lines


def find_all_of(grid, letter):
    result = []

    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            if cell == letter:
                result.append((row, col))

    return result


def is_valid_position(grid, position, value):
    x, y = position
    # if (0, 0) <= position < (len(grid), len(grid[0])):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        return grid[x][y] == value
    return False


def main():
    lines = get_lines('')

    x_positions = find_all_of(lines, 'X')

    total = 0

    for row, col in x_positions:
        to_check = [
            [(row-1, col-1),(row-2, col-2),(row-3, col-3)],
            [(row-1, col  ),(row-2, col  ),(row-3, col  )],
            [(row-1, col+1),(row-2, col+2),(row-3, col+3)],
            [(row  , col-1),(row  , col-2),(row  , col-3)],
            [(row  , col+1),(row  , col+2),(row  , col+3)],
            [(row+1, col-1),(row+2, col-2),(row+3, col-3)],
            [(row+1, col  ),(row+2, col  ),(row+3, col  )],
            [(row+1, col+1),(row+2, col+2),(row+3, col+3)],
        ]

        for m_pos, a_pos, s_pos in to_check:
            if is_valid_position(lines, m_pos, 'M') and is_valid_position(lines, a_pos, 'A') and is_valid_position(lines, s_pos, 'S'):
                total += 1
    
    print(total)



if __name__ == "__main__":
    main()
