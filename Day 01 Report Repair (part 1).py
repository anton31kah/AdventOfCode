with open('Day 01 Report Repair.in.txt') as f:
    numbers = list(map(lambda l: int(l.strip()), f.readlines()))
    visited = set()

    for num in numbers:
        other = 2020 - num
        if (other) in visited:
            print(num, '*', other, '=', other * num)
            break
        visited.add(num)
