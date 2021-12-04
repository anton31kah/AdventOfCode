from src.common.common import get_lines
from src.day09.part1 import find_invalid


lines = get_lines()
numbers = list(map(int, lines))

invalid = find_invalid()

left = 0
right = 0 # inclusive
range_sum = numbers[0]

while True:
    if range_sum < invalid:
        right += 1
        range_sum += numbers[right]
    elif range_sum > invalid:
        range_sum -= numbers[left]
        left += 1
    else:
        range_nums = numbers[left:right+1]
        range_min, range_max = min(range_nums), max(range_nums)
        print(f"{range_min=}, {range_max=}, sum = {range_min + range_max}")
        break
