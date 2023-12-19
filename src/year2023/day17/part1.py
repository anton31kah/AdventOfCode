from src.common.common import get_lines
import math


def print_path(grid, path):
    text = '𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗'
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            point = (x, y)
            if point in (p for p, d in path):
                print(text[col], end='')
            else:
                print(col, end='')
        print()
    print()


def try_get(grid, point):
    x, y = point
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        return (x, y), grid[y][x]
    return None


def apply_diff(point, change):
    x, y = point
    dx, dy = change
    return x + dx, y + dy


def find_path(previous, direction, point):
    path = [point]
    curr = point
    while curr in previous and previous[curr]:
        path[-1] = path[-1], direction[curr]
        path.append(previous[curr])
        curr = previous[curr]
    return list(reversed(path))
    

def last_three_same_direction(previous, direction, point):
    N = 3

    path = find_path(previous, direction, point)
    last_three = path[-N:]

    if len(last_three) >= N:
        last_three_directions = set([d for p, d in last_three])
        all_are_directions = all(type(x) is str for x in last_three_directions)
        all_are_same_direction = len(last_three_directions) == 1
        if all_are_directions:
            return all_are_same_direction

    return False


def get_direction_between(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    dx = x2 - x1
    dy = y2 - y1
    if abs(dx) + abs(dy) != 1:
        raise ValueError(f"Points {point1} {point2} are too far apart!")
    match (dx, dy):
        case (1, 0):
            return '>'
        case (-1, 0):
            return '<'
        case (0, 1):
            return 'v'
        case (0, -1):
            return '^'


def dijkstra(grid, start, end):
    distance = {}
    previous = {}
    direction = {}
    
    queue = []
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            point = (x, y)
            queue.append(point)
            distance[point] = math.inf
            previous[point] = None
            direction[point] = None
    
    distance[start] = 0

    while queue:
        current = min(filter(lambda x: x in queue, distance), key=distance.get)
        queue.remove(current)

        for diff in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neighbor = try_get(grid, apply_diff(current, diff))
            if neighbor is not None:
                neighbor_point, neighbor_value = neighbor
                alt = distance[current] + neighbor_value
                # print(last_three_same_direction(previous, direction, current), current, neighbor_point)
                if alt < distance[neighbor_point] and not last_three_same_direction(previous, direction, current):
                    distance[neighbor_point] = alt
                    previous[neighbor_point] = current
                    direction[neighbor_point] = get_direction_between(current, neighbor_point)

    path = find_path(previous, direction, end)

    return distance[end], path


def main():
    lines = get_lines('S')
    grid = [[int(x) for x in line] for line in lines]

    distance, path = dijkstra(grid, (0, 0), (len(lines[0]) - 1, len(lines) - 1))

    print_path(grid, path)

    print(distance)
    for p in path:
        print(p)


if __name__ == "__main__":
    main()
