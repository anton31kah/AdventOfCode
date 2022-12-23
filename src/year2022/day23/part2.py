from src.common.common import get_lines


def get_neighbors(point, direction):
    row, col = point
    match direction:
        case 'N':
            return [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1)]
        case 'S':
            return [(row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
        case 'W':
            return [(row - 1, col - 1), (row, col - 1), (row + 1, col - 1)]
        case 'E':
            return [(row - 1, col + 1), (row, col + 1), (row + 1, col + 1)]
    return []


def safe_append(dictionary, key, value):
    if key not in dictionary:
        dictionary[key] = []
    dictionary[key].append(value)


def print_grid(rounds, elves):
    max_row = max(max(row for row, col in elves), 20)
    min_row = min(min(row for row, col in elves), -10)
    max_col = max(max(col for row, col in elves), 20)
    min_col = min(min(col for row, col in elves), -10)

    print('Round', rounds)
    for i in range(min_row, max_row + 1):
        for j in range(min_col, max_col + 1):
            if (i, j) in elves:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def main():
    lines = get_lines('')

    elves = set()

    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            if cell == '#':
                elves.add((row, col))

    directions = ['N', 'S', 'W', 'E']
    rounds = 0

    # print_grid(rounds, elves)

    while True:
        moves = {}
        inverse_moves = {}
        to_move = 0

        for elf in elves:
            all_neighbors = set(n for d in directions for n in get_neighbors(elf, d))
            if len(all_neighbors & elves) > 0:
                for direction in directions:
                    proposed = get_neighbors(elf, direction)
                    if len(set(proposed) & elves) == 0:
                        moves[elf] = proposed[1]
                        to_move += 1
                        safe_append(inverse_moves, proposed[1], elf)
                        break
            else:
                moves[elf] = elf
                safe_append(inverse_moves, elf, elf)

        directions.append(directions.pop(0))

        for proposed, elves_to_move in inverse_moves.items():
            if len(elves_to_move) > 1:
                for elf in elves_to_move:
                    moves.pop(elf)

        for elf, new_pos in moves.items():
            elves.remove(elf)
            elves.add(new_pos)

        rounds += 1

        if to_move == 0:
            break

        # print_grid(rounds, elves)

    print(rounds)


if __name__ == "__main__":
    main()
