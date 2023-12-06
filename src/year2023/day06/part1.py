import re
from src.common.common import get_lines


def calculate_distance(speed, time):
    return speed * (time - speed)


def main():
    lines = get_lines('')

    times = [int(x) for x in re.findall(r'\d+', lines[0])]
    distances = [int(x) for x in re.findall(r'\d+', lines[1])]

    product = 1

    for time, distance in zip(times, distances):
        time_half = time // 2
        speed = time_half
        total = 0
        while calculate_distance(speed, time) > distance:
            total += 2
            speed -= 1
        if time % 2 == 0:
            total -= 1

        product *= total

    print(product)


if __name__ == "__main__":
    main()
