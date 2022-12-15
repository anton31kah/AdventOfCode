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
    lines = get_lines('S')

    sensors_beacons = [parse_line(line) for line in lines]

    # print(sum(((((distance(sensor, beacon) ** 2) * 2) ** 0.5) * 4) for sensor, beacon in sensors_beacons))
    # print()
    # for sensor, beacon in sensors_beacons:
    #     dis_beacon = distance(sensor, beacon)
    #     print(((((distance(sensor, beacon) ** 2) * 2) ** 0.5) * 4))
    # exit()

    min_x = min_y = 0
    max_x = max_y = 4_000_000
    max_x = max_y = 20

    for sensor, beacon in sensors_beacons:
        dis_beacon = distance(sensor, beacon)
        sx, sy = sensor
        points = [
            (sx - dis_beacon - 1, sy),
            (sx + dis_beacon + 1, sy),
            (sx, sy - dis_beacon - 1),
            (sx, sy + dis_beacon + 1),
        ]
        for position in points:
            in_range_of_sensor = False
            for sensor, beacon in sensors_beacons:
                dis_beacon = distance(sensor, beacon)
                pos_beacon = distance(sensor, position)
                if pos_beacon <= dis_beacon:
                    in_range_of_sensor = True
            if not in_range_of_sensor:
                x, y = position
                if min_x <= x <= max_x and min_y <= y <= max_y:
                    print(position)

    # max_x = max_y = 4_000_000

    # for x in range(0, max_x):
    #     print('x', x)
    #     for y in range(0, max_y):
    #         if y % 100_000 == 0:
    #             print('y', y)
    #         position = (x, y)
    #         in_range_of_sensor = False
    #         for sensor, beacon in sensors_beacons:
    #             dis_beacon = distance(sensor, beacon)
    #             pos_beacon = distance(sensor, position)
    #             if pos_beacon <= dis_beacon:
    #                 in_range_of_sensor = True
    #         if not in_range_of_sensor:
    #             print(position)


if __name__ == "__main__":
    main()
