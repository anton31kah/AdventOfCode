import math
from src.common.common import get_lines


# function Dijkstra(Graph, source):
#
#     for each vertex v in Graph.Vertices:
#         dist[v] ← INFINITY
#         prev[v] ← UNDEFINED
#         add v to Q
#     dist[source] ← 0
#
#     while Q is not empty:
#         u ← vertex in Q with min dist[u]
#
#         if u = target:
#             S ← empty sequence
#             u ← target
#             if prev[u] is defined or u = source:          # Do something only if the vertex is reachable
#                 while u is defined:                       # Construct the shortest path with a stack S
#                     insert u at the beginning of S        # Push the vertex onto the stack
#                     u ← prev[u]                           # Traverse from target to source
#
#         remove u from Q
#
#         for each neighbor v of u still in Q:
#             alt ← dist[u] + Graph.Edges(u, v)
#             if alt < dist[v]:
#                 dist[v] ← alt
#                 prev[v] ← u
#
#     return dist[], prev[]
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

        if u == target:
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

    if (ha, hb) == ('S', 'a') or (ha, hb) == ('z', 'E'):
        return 0

    if ha in ('S', 'E') or hb in ('S', 'E'):
        return math.inf

    dist = ord(hb) - ord(ha)

    if dist > 1:
        return math.inf

    return dist


def value(graph, node):
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

    result = dijkstra(grid, source, target)
    print(result)
    print(len(result) - 1)


if __name__ == "__main__":
    main()
