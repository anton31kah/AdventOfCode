from src.common.common import get_lines
import math
import functools


def count_digits(num):
    return math.floor(math.log10(num)) + 1


@functools.cache
def stone_blink(value, blinks):
    if blinks == 75:
        return 1

    if value == 0:
        return stone_blink(1, blinks + 1)
    
    digits_len = count_digits(value)
    if digits_len % 2 == 0:
        mul = 10 ** (digits_len // 2)
        left = value // mul
        right = value % mul
        return stone_blink(left, blinks + 1) + stone_blink(right, blinks + 1)

    return stone_blink(value * 2024, blinks + 1)


def main():
    lines = get_lines('')

    numbers = [int(x) for x in lines[0].split()]

    total = 0

    for n in numbers:
        total += stone_blink(n, 0)
    
    print(total)


if __name__ == "__main__":
    main()
