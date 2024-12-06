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
        case (-1, 0): # up
            return (0, 1)
        case (0, 1): # right
            return (1, 0)
        case (1, 0): # down
            return (0, -1)
        case (0, -1): # left
            return (-1, 0)

    raise ValueError(f"Invalid direction {direction}")


def direction_symbol(direction):
    match direction:
        case (-1, 0): # up
            return '^'
        case (0, 1): # right
            return '>'
        case (1, 0): # down
            return 'v'
        case (0, -1): # left
            return '<'

    raise ValueError(f"Invalid direction {direction}")


def move_to_direction(position, direction):
    x, y = position
    dx, dy = direction
    return x + dx, y + dy


def in_grid(lines, position):
    x, y = position
    return 0 <= x < len(lines) and 0 <= y < len(lines[0])


def print_grid(lines, obstacles, visited, guard, direction):
    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            position = row, col
            thing = ['.']
            if position in obstacles:
                thing.append('#')
            if position in visited:
                thing.append('X')
            if position == guard:
                thing.append(direction_symbol(direction))
            # if len(thing) >= 3:
                # raise ValueError(f"Multiple things at place {position}: {thing}")
            print(thing[-1], end='')
        print()
    
    print()
    print()


def main():
    lines = get_lines('')

    obstacles, guard = parse_grid(lines)

    direction = (-1, 0)

    visited = {}

    while in_grid(lines, guard):
        # print_grid(lines, obstacles, visited, guard, direction)

        if guard not in visited:
            visited[guard] = set()
        visited[guard].add(direction_symbol(direction))
        
        new_guard = move_to_direction(guard, direction)

        while new_guard in obstacles:
            direction = rotate_direction(direction)
            new_guard = move_to_direction(guard, direction)
        
        guard = new_guard
    
    for obstacle in obstacles:
        neighbors = [
            move_to_direction(obstacle, (-1, 0)),
            move_to_direction(obstacle, (+1, 0)),
            move_to_direction(obstacle, (0, -1)),
            move_to_direction(obstacle, (0, +1)),
        ]

        # idea is, for each neighbor try to draw a square within the visited
        # this will only work if the current obstacle is the middle of the 3 existing
        # when the 3rd & 4th line meet, that's the position of our new obstacle -> 1 loop

        for neighbor in neighbors:
            if neighbor in visited:
                pass

    print(len(visited))


if __name__ == "__main__":
    main()
