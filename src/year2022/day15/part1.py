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

    min_x_beacon = min(bx for _, (bx, _) in sensors_beacons)
    max_x_beacon = max(bx for _, (bx, _) in sensors_beacons)

    y = 2000000

    total = 0

    print(min_x_beacon, max_x_beacon, len(range(min_x_beacon * 2, max_x_beacon * 2)))
    for x in range(min_x_beacon * 2, max_x_beacon * 2):
        if x % 100_000 == 0:
            print(x, total)
        position = (x, y)
        in_range_of_sensor = False
        for sensor, beacon in sensors_beacons:
            dis_beacon = distance(sensor, beacon)
            pos_beacon = distance(sensor, position)
            if pos_beacon <= dis_beacon:
                in_range_of_sensor = True
        if in_range_of_sensor:
            same_position_as_beacon = False
            for sensor, beacon in sensors_beacons:
                if position in (sensor, beacon):
                    same_position_as_beacon = True
                    break
            if not same_position_as_beacon:
                total += 1

    print(total)


if __name__ == "__main__":
    main()
