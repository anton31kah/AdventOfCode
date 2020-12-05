graph = None

with open('Day 03 Toboggan Trajectory.in.txt') as f:
    graph = list(map(lambda l: l.strip(), f.readlines()))

col = 0
trees = 0

for row in graph:
    if row[col] == '#':
        trees += 1
    col += 3
    col %= len(row)

print(trees)
