from concurrent.futures import ProcessPoolExecutor
from collections import defaultdict
from timeit import default_timer as timer
from src.common.common import get_lines


def parse_grid(lines):
    obstacles = []
    guard = None

    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            if cell == '#':
                obstacles.append((row, col))
            if cell == '^':
                guard = (row, col)

    return obstacles, guard


def rotate_direction(direction):
    match direction:
        case (-1, 0):  # up
            return (0, 1)
        case (0, 1):  # right
            return (1, 0)
        case (1, 0):  # down
            return (0, -1)
        case (0, -1):  # left
            return (-1, 0)

    raise ValueError(f"Invalid direction {direction}")


def direction_symbol(direction):
    match direction:
        case (-1, 0):  # up
            return '^'
        case (0, 1):  # right
            return '>'
        case (1, 0):  # down
            return 'v'
        case (0, -1):  # left
            return '<'

    raise ValueError(f"Invalid direction {direction}")


def move_to_direction(position, direction):
    x, y = position
    dx, dy = direction
    return x + dx, y + dy


def in_grid(lines, position):
    x, y = position
    return 0 <= x < len(lines) and 0 <= y < len(lines[0])


def print_grid(lines, obstacles, visited, guard, direction, new_obstacle):
    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            position = row, col
            thing = ['.']
            if position in obstacles:
                thing.append('#')
            if position in visited:
                thing.append(next(iter(visited[position])))
            if position == guard:
                thing.append(direction_symbol(direction))
            if position == new_obstacle:
                thing.append('O')
            # if len(thing) >= 3:
            # raise ValueError(f"Multiple things at place {position}: {thing}")
            print(thing[-1], end='')
        print()

    print()
    print()


def contains_sequence(big_list, small_list):
    for i in range(len(big_list)):
        if big_list[i:i + len(small_list)] == small_list:
            return True
    return False


def run_guard_run(lines, obstacles, initial_guard, new_obstacle):
    guard = initial_guard
    direction = (-1, 0)
    visited = defaultdict(set)
    path = []

    last_n = 3

    try:
        while in_grid(lines, guard):
            visited[guard].add(direction_symbol(direction))

            path.append(guard)
            if len(path) % 3 == 0 and contains_sequence(path[:-last_n], path[-last_n:]):
                return 'hit', visited

            new_guard = move_to_direction(guard, direction)

            while new_guard in obstacles:
                direction = rotate_direction(direction)
                visited[guard].add(direction_symbol(direction))
                new_guard = move_to_direction(guard, direction)

            guard = new_guard

        return 'left_grid', visited
    except KeyboardInterrupt as e:
        print_grid(lines, obstacles, visited, guard, direction, new_obstacle)
        raise e


def run_guard_run_wrapper(args):
    return run_guard_run(args[0], args[1], args[2], args[3])


def main():
    lines = get_lines('')

    obstacles, guard = parse_grid(lines)

    _, visited = run_guard_run(lines, obstacles, guard, None)

    total = 0

    start = timer()

    with ProcessPoolExecutor() as executor:
        args_list = [[lines, obstacles + [position], guard, position] for position in visited]
        for position, result in zip(visited, executor.map(run_guard_run_wrapper, args_list)):
            if result[0] == 'hit':
                total += 1
                print('found', position, result[0], total)

    end = timer()

    print(total)

    print('took', end - start, 'seconds')


if __name__ == "__main__":
    main()
