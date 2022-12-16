import re
from src.common.common import get_lines


class ValveNode:
    def __init__(self, valve_id, flow, tunnels):
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


def parse_input(lines):
    valves = {}

    for line in lines:
        valve_id, flow, tunnels = parse_line(line)
        valves[valve_id] = ValveNode(valve_id, flow, []), tunnels

    for valve_node, tunnels in list(valves.values()):
        valve_node.tunnels = [valves[t][0] for t in tunnels]

    for valve_id in list(valves.keys()):
        valves[valve_id] = valves[valve_id][0]

    return valves


def find_max():
    """
    HH [22] => cost = 5+1=6 => value => 22*24=528
    JJ [21] => cost = 2+1=3 => value => 21*27=567
    DD [20] => cost = 1+1=2 => value => 20*28=560
    BB [13] => cost = 1+1=2 => value => 13*28=364
    EE  [3] => cost = 2+1=3 => value =>  3*27=81
    CC  [2] => cost = 2+1=3 => value =>  2*27=54
    """
    ...


def main():
    lines = get_lines('S')

    valves = parse_input(lines)

    print(valves)


if __name__ == "__main__":
    main()
