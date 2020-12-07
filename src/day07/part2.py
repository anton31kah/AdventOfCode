from src.common.common import get_lines


class Tree:
    def __init__(self, color, count, parent: 'Tree'):
        self.color = color
        self.count = count
        self.parent = parent
        self.children = []
    
    def add_child(self, color, count):
        node = Tree(color, count, self)
        self.children.append(node)
        return node
    
    def count_bags(self):
        total = 0
        for child in self.children:
            total += child.count_bags()
        return self.count * total + self.count
    
    def __hash__(self):
        if self.parent:
            return hash((self.color, self.count, hash(self.parent)))
        else:
            return hash((self.color, self.count))
    
    def __eq__(self, other):
        return other is self

    def __ne__(self, other):
        return other is not self


def parse_rule(line: str):
    parent_color, rest = line.split(' bags contain ')
    rest = rest.split(', ')
    inner_bags = [bag.split(' bag')[0] for bag in rest if bag != 'no other bags.']
    inner_bags = [tuple(bag.split(' ', 1)) for bag in inner_bags]
    inner_bags = [(int(count), color) for count, color in inner_bags]
    return parent_color, inner_bags


rules = get_lines()

rules = [parse_rule(rule) for rule in rules]
rules = dict(rules)

root = Tree('shiny gold', 1, None)
colors_to_check = set([root])

while colors_to_check:
    color_to_check = colors_to_check.pop()
    new_colors_to_check = set()
    for count, color in rules[color_to_check.color]:
        new_colors_to_check.add(color_to_check.add_child(color, count))
    colors_to_check.update(new_colors_to_check)

print(root.count_bags() - 1)
