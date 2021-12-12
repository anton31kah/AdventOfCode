from dataclasses import dataclass

from src.common.common import get_lines


@dataclass
class Node:
    name: str

    neighbors: list['Node']

    is_big: bool
    is_small: bool

    is_start: bool
    is_end: bool

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


Graph = dict[str, Node]


def create_node(name: str, graph: Graph) -> Node:
    if name in graph:
        return graph[name]
    else:
        graph[name] = Node(
            name=name,
            neighbors=[],
            is_big=name.isupper() and name not in ('start', 'end'),
            is_small=name.islower() and name not in ('start', 'end'),
            is_start=name == 'start',
            is_end=name == 'end',
        )
        return graph[name]


def read_graph(lines) -> Graph:
    graph: Graph = dict()

    for edge in lines:
        start, end = edge.split('-')

        start_node = create_node(start, graph)
        end_node = create_node(end, graph)

        start_node.neighbors.append(end_node)
        end_node.neighbors.append(start_node)

    return graph


def count_small(path: list[Node]) -> dict[str, int]:
    result = {}
    for node in path:
        if node.is_small:
            if node.name in result:
                result[node.name] += 1
            else:
                result[node.name] = 1
    return result


def can_visit_small(node: Node, previous_stats: dict[str, int]):
    if not node.is_small:
        raise Exception('Not a small cave')

    potential_new_stats = {k: v for k, v in previous_stats.items()}
    if node.name in potential_new_stats:
        potential_new_stats[node.name] += 1
    else:
        potential_new_stats[node.name] = 1

    visited_twice = set(node_name for node_name, visits in potential_new_stats.items() if visits == 2)
    visited_more = set(node_name for node_name, visits in potential_new_stats.items() if visits > 2)

    return len(visited_twice) <= 1 and len(visited_more) == 0


def find_all_paths(graph: Graph):
    def dfs(graph: Graph, path: list[Node]):
        current = path[-1]

        if current.is_end:
            return [path]

        paths = []

        small_until_now = count_small(path)

        for neighbor in current.neighbors:
            if neighbor.is_start:
                continue

            if neighbor.is_small and not can_visit_small(neighbor, small_until_now):
                continue

            neighbor_path = dfs(graph, [*path, neighbor])
            paths.extend(neighbor_path)

        return paths

    return dfs(graph, [graph['start']])


def main():
    lines = get_lines()

    graph = read_graph(lines)
    paths = find_all_paths(graph)

    for i, path in enumerate(paths, start=1):
        print(i, path)


if __name__ == "__main__":
    main()
