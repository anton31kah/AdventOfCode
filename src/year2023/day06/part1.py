import re
from math import ceil, floor, sqrt
from src.common.common import get_lines


def calculate_distance(speed, time):
    return speed * (time - speed)


# NOT MY SOLUTION, THIS CAME AFTER 
def quick_math(time, distance):
    b1 = floor((time + sqrt(time**2 - 4 * distance))/2)
    b2 = ceil((time - sqrt(time**2 - 4 * distance))/2)

    return b1 - b2 + 1


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

        print('my', total, 'math', quick_math(time, distance))
        product *= total

    print(product)


if __name__ == "__main__":
    main()
