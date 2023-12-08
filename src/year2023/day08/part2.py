from src.common.common import get_lines
import re
from math import lcm


class Node:
    def __init__(self, name):
        self.name = name
        self.type = name[-1]
        self.left = None
        self.right = None
    
    def __eq__(self, other):
        return type(other) is Node and self.name == other.name
    
    def __str__(self):
        return f"{self.name} = ({self.left.name}, {self.right.name})"
    
    def __repr__(self):
        return str(self)


def parse_input(lines):
    directions = list(lines[0])

    nodes = {}

    for line in lines[2:]:
        current, left, right = re.findall(r'\w+', line)
        for x in [current, left, right]:
            if x not in nodes:
                nodes[x] = Node(x)
        nodes[current].left = nodes[left]
        nodes[current].right = nodes[right]
    
    return directions, nodes


def count_steps(nodes, directions, start, end):
    current_node = nodes[start]

    steps = 0

    while True:
        if current_node.name == end and steps > 0:
            break

        for step in directions:
            if step == 'L':
                current_node = current_node.left
            elif step == 'R':
                current_node = current_node.right
            steps += 1

            if current_node.name == end and steps > 0:
                break
    
    return steps

"""
observations:
1. we have 6 nodes of type A and 6 of type Z
   - for every node of type A we have L, R nodes
2. for for every A node, there is a matching Z node where A(L,R) == Z(R, L)
   - so basically A and Z lead to same nodes just in different directions
3. and the total steps from every A to its matching Z nodes takes S steps where S MOD len(directions) == 0
4. going from Z to Z again (since A and Z refer to the same nodes) we notice that we use the same amount of steps
5. we need lcm(all step counts)
"""
def main():
    lines = get_lines('')

    directions, nodes = parse_input(lines)

    # (1)
    starting_nodes = [node for node in nodes.values() if node.type == 'A']
    ending_nodes = [node for node in nodes.values() if node.type == 'Z']

    # (2)
    matching_nodes = [(start, next(filter(lambda end: (end.left, end.right) == (start.right, start.left), ending_nodes))) for start in starting_nodes]

    # (3)
    steps_start_end = []
    for start, end in matching_nodes:
        steps = count_steps(nodes, directions, start.name, end.name)
        steps_start_end.append(steps)
        print(start, end, steps, steps/len(directions))

    print()

    # (4)
    steps_end_end = []
    for _, end in matching_nodes:
        steps = count_steps(nodes, directions, end.name, end.name)
        steps_end_end.append(steps)
        print(end, end, steps, steps/len(directions))
    
    print(steps_start_end == steps_end_end)

    print(lcm(*steps_start_end))


if __name__ == "__main__":
    main()
