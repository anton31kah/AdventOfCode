from src.common.common import get_lines


def parse_rule(line):
    name, rule = line.split(': ')
    range1, range2 = rule.split(' or ')
    range1min, range1max = range1.split('-')
    range2min, range2max = range2.split('-')
    range1min, range1max = int(range1min), int(range1max)
    range2min, range2max = int(range2min), int(range2max)
    return name, ((range1min, range1max), (range2min, range2max))


def read_input(lines):    
    rules = {}
    my_ticket = None
    nearby_tickets = []

    line_idx = 0

    while line_idx < len(lines):
        line = lines[line_idx]
        if not line:
            line_idx += 1
            break

        name, rule = parse_rule(line)
        rules[name] = rule

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
    
    return rules, my_ticket, nearby_tickets


def is_rule_valid(rule, field):
    (r1min, r1max), (r2min, r2max) = rule
    return r1min <= field <= r1max or r2min <= field <= r2max


def check_rules(rules, field):
    for rule in rules.values():
        if is_rule_valid(rule, field):
            return True
    return False


def filter_valid_tickets(tickets, rules):
    valid_tickets = []

    for ticket in tickets:
        valid = True
        for field in ticket:
            if not check_rules(rules, field):
                valid = False
                break
        if valid:
            valid_tickets.append(ticket)

    return valid_tickets


def main():
    lines = get_lines()

    rules, my_ticket, tickets = read_input(lines)

    tickets = filter_valid_tickets(tickets, rules)

    rules_fields_validity = {}

    for rule_name in rules:
        rules_fields_validity.setdefault(rule_name, [0] * len(my_ticket))

    for ticket in tickets:
        for field_idx, field in enumerate(ticket):
            for rule_name, rule_range in rules.items():
                if is_rule_valid(rule_range, field):
                    rules_fields_validity[rule_name][field_idx] += 1

    valid_tickets_count = len(tickets)

    rule_field = {}

    while rules_fields_validity:
        rule_name, field_idx = next((rule_name, fields.index(valid_tickets_count)) for rule_name, fields in rules_fields_validity.items() if fields.count(valid_tickets_count) == 1)
        rule_field[rule_name] = field_idx
        rules_fields_validity.pop(rule_name)
        for fields in rules_fields_validity.values():
            fields[field_idx] = -1

    multiplied = 1

    for rule_name, field_idx in rule_field.items():
        if rule_name.startswith('departure'):
            multiplied *= my_ticket[field_idx]

    print(multiplied)


if __name__ == "__main__":
    main()
