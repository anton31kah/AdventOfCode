from src.common.common import get_lines


def parse_line(line):
    parts = line.split(' -> ')
    pairs = []
    for i in range(len(parts) - 1):
        x1, y1 = list(map(int, parts[i].split(',')))
        x2, y2 = list(map(int, parts[i + 1].split(',')))
        pairs.append(((x1, y1), (x2, y2)))
    return pairs


def to_points(start, end):
    points = []

    x1, y1 = start
    x2, y2 = end

    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            points.append((x1, y))
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            points.append((x, y1))

    return points


def main():
    lines = get_lines('')

    blockers = set()

    max_y = 0

    for line in lines:
        segments = parse_line(line)
        for start, end in segments:
            points = to_points(start, end)
            for point in points:
                blockers.add(point)
                max_y = max(max_y, point[1])

    for x in range(-1500, 1500 + 1):
        blockers.add((x, max_y + 2))

    sands = 0
    current_sand = None

    while True:
        if current_sand is None:
            current_sand = (500, 0)

            if current_sand in blockers:
                break

            # print('new sand', sands)

        x, y = current_sand

        if (x, y + 1) not in blockers:
            current_sand = x, y + 1
        elif (x - 1, y + 1) not in blockers:
            current_sand = x - 1, y + 1
        elif (x + 1, y + 1) not in blockers:
            current_sand = x + 1, y + 1
        else:
            blockers.add(current_sand)
            current_sand = None
            sands += 1

    print(sands)


if __name__ == "__main__":
    main()
