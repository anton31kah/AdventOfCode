graph = None

with open('Day 03 Toboggan Trajectory.in.txt') as f:
    graph = list(map(lambda l: l.strip(), f.readlines()))

trees_mul = 1

# Right 1, down 1.

col = 0
trees = 0

for row in graph:
    if row[col] == '#':
        trees += 1
    col += 1
    col %= len(row)

trees_mul *= trees
print(trees)

# Right 3, down 1. (This is the slope you already checked.)

col = 0
trees = 0

for row in graph:
    if row[col] == '#':
        trees += 1
    col += 3
    col %= len(row)

trees_mul *= trees
print(trees)

# Right 5, down 1.

col = 0
trees = 0

for row in graph:
    if row[col] == '#':
        trees += 1
    col += 5
    col %= len(row)

trees_mul *= trees
print(trees)

# Right 7, down 1.

col = 0
trees = 0

for row in graph:
    if row[col] == '#':
        trees += 1
    col += 7
    col %= len(row)

trees_mul *= trees
print(trees)

# Right 1, down 2.

row, col = 0, 0
trees = 0

while row < len(graph):
    line = graph[row]
    if line[col] == '#':
        trees += 1
    col += 1
    col %= len(line)
    row += 2

trees_mul *= trees
print(trees)

# MULTIPLICATION

print(trees_mul)
