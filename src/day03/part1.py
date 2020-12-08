from src.common.common import get_lines


graph = get_lines()

col = 0
trees = 0

for row in graph:
    if row[col] == '#':
        trees += 1
    col += 3
    col %= len(row)

print(trees)
