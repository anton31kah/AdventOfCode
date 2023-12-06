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

    time = int(''.join(re.findall(r'\d+', lines[0])))
    distance = int(''.join(re.findall(r'\d+', lines[1])))

    print('math', quick_math(time, distance))

    time_half = time // 2
    speed = time_half
    total = 0

    # Can probably be done using a math but I don't know enough math.
    # I know that speed * (time - speed) is a quadratic function.
    # We have f(x)=x*(T-x) where T is a constant
    # and we need to find how many x are there for which f(x) > D where D is also a constant
    while calculate_distance(speed, time) > distance:
        total += 2
        speed -= 1
    if time % 2 == 0:
        total -= 1

    print(total)


if __name__ == "__main__":
    main()
