from src.common.common import get_lines


def adjacent(a, b):
    ax, ay, az = a
    bx, by, bz = b
    return (abs(ax - bx) + abs(ay - by) + abs(az - bz)) == 1


def neighbors(point):
    x, y, z = point
    return [
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    ]


def main():
    lines = get_lines('')

    points = set(tuple(map(int, line.split(','))) for line in lines)

    visited = set()
    to_visit = [(25,25,25)]
    is_adjacent_with_point = set()

    while len(to_visit) > 0:
        current = to_visit.pop()

        if current in visited:
            continue

        for neighbor in neighbors(current):
            x, y, z = neighbor

            if neighbor in points:
                is_adjacent_with_point.add(current)
            elif -5 <= x <= 25 and -5 <= y <= 25 and -5 <= z <= 25:
                # x{1-20}, y{0-21}, z{0-21}
                to_visit.append(neighbor)

        visited.add(current)

    total = 0

    for point in is_adjacent_with_point:
        for neighbor in neighbors(point):
            if neighbor in points:
                total += 1

    print(total)


if __name__ == "__main__":
    main()
