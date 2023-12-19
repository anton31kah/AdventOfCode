from src.common.common import get_lines


def read_line(line):
    direction, meters, color = line.split()
    meters = int(meters)
    color = color[2:-1]

    meters = int(color[:5], 16)
    
    direction = 'RDLU'[int(color[5])]

    return direction, meters, color


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


def find_area(instructions):
    points = [(0, 0)]
    current = (0, 0)
    perimeter = 0
    for direction, meters, _ in instructions:
        dx, dy = get_diff(direction)
        x, y = current
        m = meters
        new = m * dx + x, m * dy + y
        current = new
        perimeter += meters
        points.append(new)
    
    area = 0

    for i in range(len(points)):
        point1 = points[i]
        point2 = points[(i + 1) % len(points)]

        x1, y1 = point1
        x2, y2 = point2

        area += (x1 * y2 - x2 * y1)

    return area // 2 + perimeter // 2 + 1


def main():
    lines = get_lines('')
    instructions = [read_line(line) for line in lines]
    print(find_area(instructions))


if __name__ == "__main__":
    main()
