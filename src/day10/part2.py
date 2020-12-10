import datetime
from src.common.common import get_lines


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.leaves = None

    def add_child(self, obj):
        self.children.append(obj)
    
    def count_leaves(self):
        """
        to count the different arrangments, we simply need to count all the leaves.
        """

        if self.leaves:
            return self.leaves

        if not self.children:
            return 1

        count = 0

        for child in self.children:
            count += child.count_leaves()

        self.leaves = count

        return count


def find_adapter(adapter, list_of_adapters):
    valid = []
    for element in list_of_adapters:
        if adapter + 1 <= element <= adapter + 3:
            valid.append(element)
    return valid


lines = get_lines()

adapters = sorted(map(int, lines))

device = adapters[-1] + 3

adapters.insert(0, 0)
adapters.insert(device, device)

adapter_nodes = {jolt: Node(jolt) for jolt in adapters}

for jolt, node in adapter_nodes.items():
    valid = find_adapter(jolt, adapters)

    for element in valid:
        node.add_child(adapter_nodes[element])

print(adapter_nodes[0].count_leaves())
