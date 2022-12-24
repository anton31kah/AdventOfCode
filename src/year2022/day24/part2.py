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
                    position = row, 1
            case '<':
                position = row, col - 1
                if position in walls:
                    position = row, grid_width - 2
            case 'v':
                position = row + 1, col
                if position in walls:
                    position = 1, col
            case '^':
                position = row - 1, col
                if position in walls:
                    position = grid_height - 2, col
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


def main():
    lines = get_lines('')

    height = len(lines)
    width = len(lines[0])

    blizzards, walls = parse_grid(lines)
    start = (0, 1)
    end = (height - 1, width - 2)

    target = end
    end_already_reached_once = False

    minutes = 0

    queue = {start}

    last_distance = distance(start, target)

    while True:
        blizzards = move_blizzards(blizzards, walls, width, height)
        blizzards_positions = set(map(lambda b: (b[0], b[1]), blizzards))

        proposal = set()

        for el in sorted(queue, key=lambda p: distance(p, target)):
            options = get_neighbors(el)
            for option in options:
                if 0 <= option[0] <= height and 0 <= option[1] <= width:
                    proposal.add(option)

        queue = proposal - blizzards_positions - walls

        current_last_distance = min(distance(x, target) for x in queue)
        if current_last_distance < last_distance:
            print('current_last_distance', current_last_distance)
            last_distance = current_last_distance

        if target in queue:
            if target == end:
                if end_already_reached_once:
                    break
                else:
                    target = start
                    queue = {end}
                    last_distance = distance(end, target)
                    print('going to start')
                end_already_reached_once = True
            elif target == start:
                target = end
                queue = {start}
                last_distance = distance(start, target)
                print('going to end')

        minutes += 1

    print(minutes + 1)


if __name__ == "__main__":
    main()
