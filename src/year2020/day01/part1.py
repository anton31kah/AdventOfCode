from src.common.common import get_lines


numbers = list(map(int, get_lines()))
visited = set()

for num in numbers:
    other = 2020 - num
    if (other) in visited:
        print(num, '*', other, '=', other * num)
        break
    visited.add(num)
