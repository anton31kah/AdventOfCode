from src.common.common import get_lines
from collections import Counter, defaultdict


def find_all_of(grid, letter):
    result = []

    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            if cell == letter:
                result.append((row, col))

    return result


def is_valid_position(grid, position, value=None):
    x, y = position
    # if (0, 0) <= position < (len(grid), len(grid[0])):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        return grid[x][y] == value if value is not None else True
    return False


def reverse_dict(orig):
    d = defaultdict(list)
    for k, v in orig.items():
        d[v].append(k)
    return d


def main():
    lines = get_lines('')

    a_positions = find_all_of(lines, 'A')

    total = 0

    for row, col in a_positions:
        to_check = [
            (row-1, col-1),
            (row-1, col+1),
            (row+1, col-1),
            (row+1, col+1),
        ]

        diagonal_values = {}

        # check if all diagonal positions are valid (within grid)
        valid = True
        for diagonal_pos in to_check:
            if not is_valid_position(lines, diagonal_pos):
                valid = False
                break
            x, y = diagonal_pos
            diagonal_values[diagonal_pos] = lines[x][y]
        if not valid:
            continue
        
        # check if M & S appear exactly twice each
        diagonal_values_counter = Counter(diagonal_values.values())
        if diagonal_values_counter['M'] != 2 or diagonal_values_counter['S'] != 2:
            continue
        
        # check if M & S positions are from same side each
        diagonal_positions = reverse_dict(diagonal_values)
        first_m_pos = diagonal_positions['M'][0]
        second_m_pos = diagonal_positions['M'][1]
        if first_m_pos[0] == second_m_pos[0] or first_m_pos[1] == second_m_pos[1]:
            total += 1
    
    print(total)



if __name__ == "__main__":
    main()
