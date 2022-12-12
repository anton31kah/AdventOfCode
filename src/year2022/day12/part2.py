import math
from src.common.common import get_lines


def dijkstra(graph, source, target):
    dist = {}
    prev = {}
    queue = []

    for row_idx in range(len(graph)):
        for col_idx in range(len(graph[0])):
            v = (row_idx, col_idx)
            dist[v] = math.inf
            prev[v] = None
            queue.append(v)

    dist[source] = 0

    while len(queue) > 0:
        u = min(queue, key=lambda u: dist[u])

        if value(graph, u) == target:
            path = []
            if prev[u] is not None:
                while u is not None:
                    path.append(u)
                    u = prev[u]

            return list(reversed(path))

        queue.remove(u)

        for v in neighbors(graph, u):
            if v in queue:
                alt = dist[u] + distance(graph, u, v)
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

    return None


def neighbors(graph, node):
    result = []

    nodes = [
        (node[0] - 1, node[1]),
        (node[0] + 1, node[1]),
        (node[0], node[1] - 1),
        (node[0], node[1] + 1),
    ]

    for n in nodes:
        if 0 <= n[0] < len(graph) and 0 <= n[1] < len(graph[0]):
            result.append(n)

    return result


def distance(graph, a, b):
    ha = value(graph, a)
    hb = value(graph, b)

    hops = ord(ha) - ord(hb)

    if hops > 1:
        return math.inf

    return 1


def value(graph, node, new_value=None):
    if new_value is not None:
        graph[node[0]][node[1]] = new_value
    return graph[node[0]][node[1]]


def main():
    lines = get_lines('')

    grid = [list(line) for line in lines]

    source = None
    target = None

    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            match col:
                case 'S':
                    source = (row_idx, col_idx)
                case 'E':
                    target = (row_idx, col_idx)

    value(grid, source, 'a')
    value(grid, target, 'z')

    result = dijkstra(grid, target, 'a')

    # for row_idx, row in enumerate(grid):
    #     for col_idx, col in enumerate(row):
    #         if (row_idx, col_idx) in result:
    #             print('#', end='')
    #         else:
    #             print('.', end='')
    #     print()

    print(len(result) - 1)


if __name__ == "__main__":
    main()
