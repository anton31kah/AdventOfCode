from cachetools import cached, LRUCache
from cachetools.keys import hashkey
from itertools import chain, combinations
import math
import re
from src.common.common import get_lines


class ValveNode:
    def __init__(self, valve_id: str, flow: int, tunnels: 'list[ValveNode]'):
        self.valve_id = valve_id
        self.flow = flow
        self.tunnels = tunnels


    def __str__(self):
        return f'Valve{{{self.valve_id}, {self.flow}, {[t.valve_id for t in self.tunnels]}}}'


    def __repr__(self):
        return f'Valve{{{self.valve_id}, {self.flow}, {[t.valve_id for t in self.tunnels]}}}'


def parse_line(line):
    regex = r'^Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)$'
    valve, flow, tunnels = re.findall(regex, line)[0]
    return valve, int(flow), tunnels.split(', ')


def parse_input(lines) -> list[ValveNode]:
    valves = {}

    for line in lines:
        valve_id, flow, tunnels = parse_line(line)
        valves[valve_id] = ValveNode(valve_id, flow, []), tunnels

    for valve_node, tunnels in list(valves.values()):
        valve_node.tunnels = [valves[t][0] for t in tunnels]

    for valve_id in list(valves.keys()):
        valves[valve_id] = valves[valve_id][0]

    return list(valves.values())


def floyd_warshall(valves: list[ValveNode]) -> dict[tuple[str, str], int]:
    dist = {}

    for valve in valves:
        for tunnel in valve.tunnels:
            dist[(valve.valve_id, tunnel.valve_id)] = 1
            dist[(tunnel.valve_id, valve.valve_id)] = 1
        dist[(valve.valve_id, valve.valve_id)] = 0
    for valve_k in valves:
        k = valve_k.valve_id
        for valve_i in valves:
            i = valve_i.valve_id
            for valve_j in valves:
                j = valve_j.valve_id

                dist.setdefault((i, j), math.inf)
                dist.setdefault((i, k), math.inf)
                dist.setdefault((k, j), math.inf)

                if dist[(i, j)] > dist[(i, k)] + dist[(k, j)]:
                    dist[(i, j)] = dist[(i, k)] + dist[(k, j)]

    return dist


def powerset(s):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(s)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


@cached(cache=LRUCache(maxsize=1_000_000), key=lambda valves, distances, time_left, valves_to_open, current_valve: hashkey(time_left, valves_to_open, current_valve))
def find_max(valves: list[ValveNode], distances: dict[tuple[str, str], int], time_left: int, valves_to_open: frozenset[str], current_valve: str):
    if time_left < 0:
        return 0

    possible = []

    for valve in valves:
        if valve.valve_id in valves_to_open and valve.flow > 0 and valve.valve_id != current_valve:
            cost = distances[(valve.valve_id, current_valve)] + 1
            value = find_max(valves, distances, time_left - cost, valves_to_open - {valve.valve_id}, valve.valve_id)
            value += valve.flow * max(time_left - cost, 0)
            possible.append(value)

    if len(possible) == 0:
        return 0

    return max(possible)


def main():
    lines = get_lines('')

    valves = parse_input(lines)
    distances = floyd_warshall(valves)

    valves_to_open = frozenset([valve.valve_id for valve in valves if valve.flow > 0])

    possible = []

    for i, s in enumerate(powerset(valves_to_open)):
        if i % 10 == 0:
            print(i)

        person = frozenset(s)
        elephant = valves_to_open - person
        value_person = find_max(valves, distances, 26, person, 'AA')
        value_elephant = find_max(valves, distances, 26, elephant, 'AA')
        value = value_person + value_elephant
        possible.append(value)

    value = max(possible)

    print(value)


if __name__ == "__main__":
    main()
