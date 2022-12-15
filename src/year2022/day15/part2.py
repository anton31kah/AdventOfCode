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

    # print(sum(((((distance(sensor, beacon) ** 2) * 2) ** 0.5) * 4) for sensor, beacon in sensors_beacons))
    # print()
    # for sensor, beacon in sensors_beacons:
    #     dis_beacon = distance(sensor, beacon)
    #     print(((((distance(sensor, beacon) ** 2) * 2) ** 0.5) * 4))
    # exit()

    min_x = min_y = 0
    max_x = max_y = 4_000_000
    # max_x = max_y = 20

    for sensor, beacon in sensors_beacons:
        dis_beacon = distance(sensor, beacon)
        sx, sy = sensor

        dy = 0

        # print(len(range(sx - dis_beacon - 1, sx + dis_beacon + 2)))
        for x in range(sx - dis_beacon - 1, sx + dis_beacon + 2):
            y = sy - dy
            position = x, y
            # print(sensor, dis_beacon, position)

            if min_x <= x <= max_x and min_y <= y <= max_y:
                in_range_of_sensor = any(distance(sensor, position) <= distance(sensor, beacon) for sensor, beacon in sensors_beacons)
                if not in_range_of_sensor:
                    print(position)
                    print(x * 4_000_000 + y)
                    exit()

            y = sy + dy
            position = x, y
            # print(sensor, dis_beacon, position)

            if min_x <= x <= max_x and min_y <= y <= max_y:
                in_range_of_sensor = any(distance(sensor, position) <= distance(sensor, beacon) for sensor, beacon in sensors_beacons)
                if not in_range_of_sensor:
                    print(position)
                    print(x * 4_000_000 + y)
                    exit()

            dy += 1


if __name__ == "__main__":
    main()
