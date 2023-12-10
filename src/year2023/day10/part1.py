from src.common.common import get_lines


def pretty_print(lines):
    for line in lines:
        new_line = line.replace('|', '│').replace('-', '─').replace('L', '└').replace('.', '.').replace('F', '┌').replace('J', '┘').replace('7', '┐')
        print(new_line)
    print()


def find_start(lines):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == 'S':
                return (x, y)
    return None



horizontally_connected = {
    ('-','-'),
    ('-','J'),
    ('F','J'),
    ('L','J'),
    ('L','J'),
    ('L','7'),
    ('L','-'),
    ('F','7'),
    ('F','J'),
    ('F','-'),
    ('-','7'),
    ('L','7'),
    ('F','7'),
}
vertically_connected = {
    ('|','|'),
    ('F','J'),
    ('7','J'),
    ('|','J'),
    ('7','L'),
    ('F','L'),
    ('|','L'),
    ('F','J'),
    ('F','L'),
    ('F','|'),
    ('7','J'),
    ('7','L'),
    ('7','|'),
}
def are_connected(lines, point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    
    if abs(x1 - x2) + abs(y1 - y2) != 1:
        return False

    c1 = lines[y1][x1]
    c2 = lines[y2][x2]

    diff_y = y1 - y2
    diff_x = x1 - x2

    match (diff_x, diff_y):
        case (1, 0): # p1 is to the right of p2
            return (c2, c1) in horizontally_connected
        case (-1, 0): # p1 is to the left of p2
            return (c1, c2) in horizontally_connected
        case (0, 1): # p1 is below p2
            return (c2, c1) in vertically_connected
        case (0, -1): # p1 is above p2
            return (c1, c2) in vertically_connected

    raise ValueError("Invalid diff " + (diff_x, diff_y))


def find_neighbors(lines, point, visited=None):
    neighbors = []
    x, y = point
    points = [
        (x - 1, y),
        (x, y - 1),
        (x, y + 1),
        (x + 1, y),
        ]
    for x, y in points:
        if y >= 0 and y < len(lines):
            line = lines[y]
            if x >= 0 and x < len(line):
                neighbor = x, y
                if are_connected(lines, point, neighbor) and (visited is None or neighbor not in visited):
                    neighbors.append(neighbor)
    return neighbors


def determine_best_start_pipe(lines, start_point):
    x, y = start_point
    lines_copy = [line[:] for line in lines]
    for pipe in '7FLJ-|':
        lines_copy[y] = lines[y].replace('S', pipe)
        neighbors = find_neighbors(lines_copy, start_point)
        if len(neighbors) == 2:
            return pipe
    return None


def find_distance_in_loop(lines, start_point):
    distance = 0
    visited = {start_point}

    point1, point2 = find_neighbors(lines, start_point)

    visited.add(point1)
    visited.add(point2)
    distance += 1

    while True:
        if point1 == point2 and distance > 0:
            break

        neighbors1 = find_neighbors(lines, point1, visited)
        point1 = neighbors1[0]

        neighbors2 = find_neighbors(lines, point2, visited)
        point2 = neighbors2[0]

        visited.add(point1)
        visited.add(point2)

        distance += 1

        if len(neighbors1) != 1 and len(neighbors2) != 1:
            raise ValueError("Invalid state")

    return distance


def main():
    lines = get_lines('')
    
    # pretty_print(lines)

    start_point = find_start(lines)
    
    start_point_pipe = determine_best_start_pipe(lines, start_point)
    lines[start_point[1]] = lines[start_point[1]].replace('S', start_point_pipe)
    
    distance = find_distance_in_loop(lines, start_point)
    print(distance)


if __name__ == "__main__":
    main()
