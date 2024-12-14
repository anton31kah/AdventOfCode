from src.common.common import get_lines
from collections import deque


def parse_grid(lines):
    regions = {}
    points = {}

    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            pos = row, col
            if cell not in regions:
                regions[cell] = []
            regions[cell].append(pos)
            points[pos] = cell
    
    return regions, points


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def direct_neighbors(point):
    x, y = point
    return [
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
    ]


def group_regions(regions, all_points):
    grouped = []

    visited = set()

    for label, points in regions.items():
        for point in points:
            if point in visited:
                continue

            group_points = []
            grouped.append((label, group_points))

            queue = deque([point])

            while len(queue) >= 1:
                current = queue.popleft()
                if current in visited:
                    continue
                group_points.append(current)
                visited.add(current)

                for neighbor in direct_neighbors(current):
                    if neighbor in all_points and all_points[neighbor] == label:
                        queue.append(neighbor)
    
    return grouped


def calculate_perimeter(points):
    result = 0

    for point in points:
        neighbors = 0
        for neighbor in direct_neighbors(point):
            if neighbor in points:
                neighbors += 1
        result += 4 - neighbors

    return result


def main():
    lines = get_lines('')

    regions, all_points = parse_grid(lines)

    groups = group_regions(regions, all_points)

    result = 0

    for group in groups:
        area = len(group[1])
        perimeter = calculate_perimeter(group[1])
        result += perimeter * area

    print(result)


if __name__ == "__main__":
    main()
