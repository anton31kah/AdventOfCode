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
                match direction:
                    case (-1, 0): # up
                        thing.append('^')
                    case (0, 1): # right
                        thing.append('>')
                    case (1, 0): # down
                        thing.append('v')
                    case (0, -1): # left
                        thing.append('<')
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

    visited = set()

    while in_grid(lines, guard):
        # print_grid(lines, obstacles, visited, guard, direction)

        visited.add(guard)
        
        new_guard = move_to_direction(guard, direction)

        while new_guard in obstacles:
            direction = rotate_direction(direction)
            new_guard = move_to_direction(guard, direction)
        
        guard = new_guard
    
    print(len(visited))


if __name__ == "__main__":
    main()
