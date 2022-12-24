from src.common.common import get_lines


def parse_grid(lines):
    blizzards = set()
    walls = set()

    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            match cell:
                case '>' | '<' | 'v' | '^' as direction:
                    blizzards.add((row, col, direction))
                case '#':
                    walls.add((row, col))
                case '.':
                    pass

    return blizzards, walls


def move_blizzards(blizzards, walls, grid_width, grid_height):
    new_blizzards = set()
    for row, col, direction in blizzards:
        position = None
        match direction:
            case '>':
                position = row, col + 1
                if position in walls:
                    # position = next(filter(lambda w: w[0] == row and w[1] != col + 1, walls))
                    position = row, 1
            case '<':
                position = row, col - 1
                if position in walls:
                    # position = next(filter(lambda w: w[0] == row and w[1] != col - 1, walls))
                    position = row, grid_width - 2
            case 'v':
                position = row + 1, col
                if position in walls:
                    # position = next(filter(lambda w: w[1] == col and w[0] != row + 1, walls))
                    position = row, 1
            case '^':
                position = row - 1, grid_height - 2
                if position in walls:
                    # position = next(filter(lambda w: w[1] == col and w[0] != row - 1, walls))
                    position = row, col
        new_blizzards.add((position[0], position[1], direction))
    return new_blizzards


def get_neighbors(point):
    row, col = point
    return [
        (row - 1, col),
        (row, col + 1),
        (row + 1, col),
        (row, col - 1),
        (row, col)
    ]


def distance(a, b):
    row_a, col_a = a
    row_b, col_b = b
    return abs(row_b - row_a) + abs(col_b - col_a)


def print_grid(blizzards, walls, current, grid_width, grid_height):
    for row in range(grid_height):
        for col in range(grid_width):
            point = row, col

            blizzards_in_point = list(filter(lambda b: (b[0], b[1]) == point, blizzards))

            if len(blizzards_in_point) > 0:
                if len(blizzards_in_point) > 1:
                    print(len(blizzards_in_point), end='')
                else:
                    print(blizzards_in_point[0][2], end='')
            elif point in walls:
                print('#', end='')
            elif point == current:
                print('E', end='')
            else:
                print('.', end='')
        print()


def find_shortest(minutes, blizzards, walls, current, waiting_time, initial_distance_to_target, target, width, height):
    if current == target or minutes > 50:
        return minutes

    covered_distance = initial_distance_to_target - distance(current, target)
    distance_should_have_covered = minutes // 5
    # every 5 minutes, at least 1 distance covered
    if covered_distance < distance_should_have_covered:
        return -1

    blizzards = move_blizzards(blizzards, walls, width, height)
    blizzards_positions = set(map(lambda b: (b[0], b[1]), blizzards))

    options = get_neighbors(current)

    proposal = {}

    for option in options:
        if option not in blizzards_positions and option not in walls and 0 <= option[0] <= height and 0 <= option[1] <= width:
            if current != option or waiting_time < 5:
                proposal[option] = distance(option, target)

    if len(proposal) == 0:
        return -1

    times = []

    for position, _ in sorted(proposal.items(), key=lambda t: t[1]):
        new_waiting_time = waiting_time + 1 if current == position else 0
        time = find_shortest(minutes + 1, blizzards, walls, position, new_waiting_time, initial_distance_to_target, target, width, height)
        if time >= 0:
            times.append(time)

    if len(times) == 0:
        return -1

    return min(times)


def main():
    lines = get_lines('S')

    height = len(lines)
    width = len(lines[0])

    blizzards, walls = parse_grid(lines)
    current = (0, 1)
    target = (height - 1, width - 2)

    minutes = find_shortest(0, blizzards, walls, current, 0, distance(current, target), target, width, height)

    # while True:
    #     if current == target or minutes > 50:
    #         break

    #     blizzards = move_blizzards(blizzards, walls, width, height)
    #     blizzards_positions = set(map(lambda b: (b[0], b[1]), blizzards))

    #     options = get_neighbors(current)

    #     proposal = {}

    #     for option in options:
    #         if option not in blizzards_positions and option not in walls:
    #             proposal[option] = distance(option, target)

    #     # if len(proposal) == 0:
    #     #     print(current)
    #     #     print(minutes)
    #     #     print_grid(blizzards, walls, current, width, height)
    #     #     print()

    #     current = min(proposal.items(), key=lambda t: t[1])[0]

    #     # print(current)
    #     # print(minutes)
    #     # print_grid(blizzards, walls, current, width, height)
    #     # print()

    #     minutes += 1

    print(minutes)


if __name__ == "__main__":
    main()
