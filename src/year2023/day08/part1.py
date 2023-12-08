from src.common.common import get_lines
import re


class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


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


def main():
    lines = get_lines('')

    directions, nodes = parse_input(lines)

    current_node = nodes['AAA']

    steps = 0

    while True:
        if current_node.name == 'ZZZ':
            break

        for step in directions:
            if step == 'L':
                current_node = current_node.left
            elif step == 'R':
                current_node = current_node.right
            steps += 1

            if current_node.name == 'ZZZ':
                break
    
    print(steps)


if __name__ == "__main__":
    main()
