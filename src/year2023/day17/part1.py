from src.common.common import get_lines
import math


def print_path(grid, path):
    text = '𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗'
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            point = (x, y)
            if point in path:
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


def find_path(previous, point):
    path = [point]
    curr = point
    while curr in previous and previous[curr]:
        path.append(previous[curr])
        curr = previous[curr]
    return path
    

def check_last_three(previous, point):
    path = find_path(previous, point)

    if len(path) >= 3:
        ys = {y for x, y in path[:3]}
        xs = {x for x, y in path[:3]}
        if len(xs) == 1 or len(ys) == 1:
            return False

    return True


def dijkstra(grid, start, end):
    distance = {}
    previous = {}
    
    queue = []
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            point = (x, y)
            queue.append(point)
            distance[point] = math.inf
            previous[point] = None
    
    distance[start] = 0

    while queue:
        current = min(filter(lambda x: x in queue, distance), key=distance.get)
        queue.remove(current)

        for diff in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            neighbor = try_get(grid, apply_diff(current, diff))
            if neighbor is not None:
                neighbor_point, neighbor_value = neighbor
                alt = distance[current] + neighbor_value
                if alt < distance[neighbor_point] and check_last_three(previous, current):
                    distance[neighbor_point] = alt
                    previous[neighbor_point] = current

    path = find_path(previous, end)

    return distance[end], list(reversed(path))


def main():
    lines = get_lines('S')
    grid = [[int(x) for x in line] for line in lines]

    distance, path = dijkstra(grid, (0, 0), (len(lines[0]) - 1, len(lines) - 1))

    print_path(grid, path)

    print(distance, path)


if __name__ == "__main__":
    main()
