import re
from src.common.common import get_lines


def parse_line(line):
    sx, sy, bx, by = [int(x) for x in re.findall(r'(-?\d+)', line)]
    return (sx, sy), (bx, by)


def distance(sensor, beacon):
    sx, sy = sensor
    bx, by = beacon
    return abs(sx - bx) + abs(sy - by)


def main():
    lines = get_lines('')

    sensors_beacons = [parse_line(line) for line in lines]

    print(sum(((((distance(sensor, beacon) ** 2) * 2) ** 0.5) * 4) for sensor, beacon in sensors_beacons))
    print()
    for sensor, beacon in sensors_beacons:
        dis_beacon = distance(sensor, beacon)
        print(((((distance(sensor, beacon) ** 2) * 2) ** 0.5) * 4))

    exit()
    max_x = max_y = 4_000_000

    for x in range(0, max_x):
        print('x', x)
        for y in range(0, max_y):
            if y % 100_000 == 0:
                print('y', y)
            position = (x, y)
            in_range_of_sensor = False
            for sensor, beacon in sensors_beacons:
                dis_beacon = distance(sensor, beacon)
                pos_beacon = distance(sensor, position)
                if pos_beacon <= dis_beacon:
                    in_range_of_sensor = True
            if not in_range_of_sensor:
                print(position)

    print(None)


if __name__ == "__main__":
    main()
