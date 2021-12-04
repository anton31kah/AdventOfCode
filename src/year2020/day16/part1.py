from src.common.common import get_lines


def check_rules(rules, field):
    for (r1min, r1max), (r2min, r2max) in rules.values():
        if r1min <= field <= r1max or r2min <= field <= r2max:
            return True
    return False


lines = get_lines()

rules = {}
my_ticket = None
nearby_tickets = []

line_idx = 0

while line_idx < len(lines):
    line = lines[line_idx]
    if not line:
        line_idx += 1
        break

    name, rule = line.split(': ')
    range1, range2 = rule.split(' or ')
    range1min, range1max = range1.split('-')
    range2min, range2max = range2.split('-')
    range1min, range1max = int(range1min), int(range1max)
    range2min, range2max = int(range2min), int(range2max)
    rules[name] = ((range1min, range1max), (range2min, range2max))

    line_idx += 1

while line_idx < len(lines):
    line = lines[line_idx]
    if not line:
        line_idx += 1
        break

    if ',' in line:
        my_ticket = list(map(int, line.split(',')))

    line_idx += 1

while line_idx < len(lines):
    line = lines[line_idx]
    if not line:
        break

    if ',' in line:
        ticket = list(map(int, line.split(',')))
        nearby_tickets.append(ticket)

    line_idx += 1

invalid_sum = 0

for ticket in nearby_tickets:
    for field in ticket:
        if not check_rules(rules, field):
            invalid_sum += field

print(invalid_sum)
