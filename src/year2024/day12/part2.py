from src.common.common import get_lines
from collections import deque


class Node:
    def __init__(self, position: tuple[float, float]):
        self.position = position
        self.neighbors: set[Node] = set()
    
    def __eq__(self, other):
        return self.position == other.position
    
    def __hash__(self):
        return hash(self.position)


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


def direct_neighbors(point, diff=1):
    x, y = point
    return [
        ((x + diff, y), 'down'),
        ((x - diff, y), 'up'),
        ((x, y + diff), 'right'),
        ((x, y - diff), 'left'),
    ]


def group_regions(regions, all_points):
    grouped = []

    visited = set()

    for label, points in regions.items():
        for point in points:
            if point in visited:
                continue

            group_points = set()
            grouped.append((label, group_points))

            queue = deque([point])

            while len(queue) >= 1:
                current = queue.popleft()
                if current in visited:
                    continue
                group_points.add(current)
                visited.add(current)

                for neighbor, _ in direct_neighbors(current):
                    if neighbor in all_points and all_points[neighbor] == label:
                        queue.append(neighbor)
    
    return grouped


def build_walls(points):
    walls: set[Node] = set()

    for point in points:
        walls_to_build = {'down', 'up', 'right', 'left'}
        for neighbor, direction in direct_neighbors(point):
            if neighbor in points:
                walls_to_build.remove(direction)
        for wall in walls_to_build:
            x, y = point
            match wall:
                case 'down':
                    walls.add(Node((x + 0.5, y - 0.5)))
                    walls.add(Node((x + 0.5, y      )))
                    walls.add(Node((x + 0.5, y + 0.5)))
                case 'up':
                    walls.add(Node((x - 0.5, y - 0.5)))
                    walls.add(Node((x - 0.5, y      )))
                    walls.add(Node((x - 0.5, y + 0.5)))
                case 'right':
                    walls.add(Node((x - 0.5, y + 0.5)))
                    walls.add(Node((x      , y + 0.5)))
                    walls.add(Node((x + 0.5, y + 0.5)))
                case 'left':
                    walls.add(Node((x - 0.5, y - 0.5)))
                    walls.add(Node((x      , y - 0.5)))
                    walls.add(Node((x + 0.5, y - 0.5)))
    
    return walls


def connect_walls(walls: set[Node]):
    for wall1 in walls:
        for wall2 in walls:
            if wall1 != wall2:
                if round(distance(wall1.position, wall2.position), 1) == 0.5:
                    wall1.neighbors.add(wall2)
                    wall2.neighbors.add(wall1)



def count_corners(walls: set[Node]):
    # new_walls: set[Node] = set()
    total_count = 0

    for wall in walls:
        match len(wall.neighbors):
            case 1:
                raise ValueError(f'Wall {wall.position} has a single neighbor!')
            case 2:
                neighbor1, neighbor2 = wall.neighbors
                x1, y1 = neighbor1.position
                x2, y2 = neighbor2.position
                if x1 == x2 or y1 == y2:
                    # horizontal || vertical
                    neighbor1.neighbors.remove(wall)
                    neighbor2.neighbors.remove(wall)
                    neighbor1.neighbors.add(neighbor2)
                    neighbor2.neighbors.add(neighbor1)
                else:
                    # corner
                    # new_walls.add(wall)
                    total_count += 1
            case 3:
                raise ValueError(f'Wall {wall.position} has three neighbors!')
            case 4:
                # 4-way corner in S5
                # new_walls.add(wall)
                total_count += 2
            case _:
                raise ValueError(f'Wall {wall.position} has {len(wall.neighbors)} neighbors!')

    return total_count


def count_sides(points):
    walls: set[Node] = build_walls(points)

    connect_walls(walls)

    corners = count_corners(walls)

    return corners


def main():
    lines = get_lines('')

    regions, all_points = parse_grid(lines)

    groups = group_regions(regions, all_points)

    result = 0

    for group in groups:
        area = len(group[1])
        sides = count_sides(group[1])
        result += sides * area
        # print(group, sides)

    print(result)


if __name__ == "__main__":
    main()
