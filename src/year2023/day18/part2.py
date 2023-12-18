from src.common.common import get_lines
import math
from collections import deque


def read_line(line):
    direction, meters, color = line.split()
    meters = int(meters)
    color = color[2:-1]

    meters = int(color[:5], 16)
    
    direction = 'RDLU'[int(color[5])]

    return direction, meters, color


def print_grid(wall, boundaries):
    top, bottom, left, right = boundaries
    for y in range(top, bottom + 1):
        for x in range(left, right + 1):
            if (x, y) in wall:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


def get_diff(direction):
    match direction:
        case 'D':
            return (0, 1)
        case 'U':
            return (0, -1)
        case 'L':
            return (-1, 0)
        case 'R':
            return (1, 0)
    raise ValueError("invalid direction " + direction)


def get_boundaries(wall):
    top, bottom, left, right = math.inf, -math.inf, math.inf, -math.inf
    for x, y in wall:
        top = min(top, y)
        bottom = max(bottom, y)
        left = min(left, x)
        right = max(right, x)
    top, bottom, left, right = int(top), int(bottom), int(left), int(right)
    return top, bottom, left, right


def create_wall(instructions):
    wall = [(0,0)]
    current = (0,0)

    for instruction in instructions:
        direction, meters, color = instruction
        dx, dy = get_diff(direction)
        for i in range(meters):
            x, y = current
            new = x + dx, y + dy
            wall.append(new)
            current = new

    return wall


def flood_fill(wall, start):
    visited = set()
    visited.update(wall)

    visited.add(start)

    queue = deque([start])

    while queue:
        current = queue.popleft()
        x, y = current

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            xx, yy = x + dx, y + dy
            new = xx, yy
            if new not in visited:
                visited.add(new)
                queue.append(new)
    
    return visited


def main():
    lines = get_lines('S')
    instructions = [read_line(line) for line in lines]
    wall = create_wall(instructions)
    boundaries = get_boundaries(wall)
    inner = flood_fill(wall, (1, 1))
    print(len(inner))
    # print_grid(wall, (-10, 10, -10, 10))


if __name__ == "__main__":
    main()
