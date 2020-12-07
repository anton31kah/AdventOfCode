from src.common.common import get_lines


def parse_rule(line: str):
    # parse_rule('clear tan bags contain 5 bright purple bags, 1 pale black bag, 5 muted lime bags.')
    # parse_rule('pale maroon bags contain 2 dotted orange bags.')

    ## clear tan >>> [('5', 'bright purple'), ('1', 'pale black'), ('5', 'muted lime')]
    ## pale maroon >>> [('2', 'dotted orange')]
    parent_color, rest = line.split(' bags contain ')
    rest = rest.split(', ')
    inner_bags = [bag.split(' bag')[0] for bag in rest]
    inner_bags = [tuple(bag.split(' ', 1)) for bag in inner_bags]
    return parent_color, inner_bags


# rule can contain color
def check_rule(rule, color):
    # print(check_rule(rules[0], 'wavy gray'))
    return any([child[1] == color for child in rule[1]])


rules = get_lines()

rules = [parse_rule(rule) for rule in rules]

checked_colors = set()
colors_to_check = set(['shiny gold'])

while colors_to_check:
    color_to_check = colors_to_check.pop()
    new_colors_to_check = set([rule[0] for rule in rules if check_rule(rule, color_to_check)])
    colors_to_check.update(new_colors_to_check)
    checked_colors.add(color_to_check)

checked_colors.remove('shiny gold')

print(len(checked_colors))
