from src.common.common import get_lines


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.position = (x, y, z)
        self.neighbors = set()


    def adjacent(self, other):
        return (abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)) == 1


def main():
    lines = get_lines('')

    points = []

    for line in lines:
        x, y, z = list(map(int, line.split(',')))
        points.append(Point(x, y, z))

    for point1 in points:
        for point2 in points:
            if point1.adjacent(point2):
                point1.neighbors.add(point2)
                point2.neighbors.add(point1)

    total = 0

    for point in points:
        total += 6 - len(point.neighbors)
        # print(point.position, 6 - len(point.neighbors), len(point.neighbors))

    print(total)


if __name__ == "__main__":
    main()
