import itertools
from src.common.common import get_lines


def rules_run(idx: int, rules: dict, rules_cache: dict):
    if idx in rules_cache:
        return rules_cache[idx]

    rule = rules[idx]

    if isinstance(rule, str):
        rules_cache[idx] = rule
        return rule

    results = []

    for union in rule:
        result = []
        for dependency in union:
            r = rules_run(dependency, rules, rules_cache)
            result.append(r)

        if all(isinstance(r, str) for r in result):
            results.append(''.join(result))
        elif any(isinstance(r, list) for r in result):
            # converts each element to a singleton list if not already a list
            # this is done for the next step (product)
            result = [(r if isinstance(r, list) else [r]) for r in result]
            all_combinations = set(''.join(r) for r in itertools.product(*result))
            results.extend(all_combinations)

    rules_cache[idx] = results
    return results


def parse_rule(value: str):
    if value.startswith('"') and value.endswith('"'):
        return value.strip('"')
    unions = value.split(' | ')
    dependencies = []
    for union in unions:
        dependency = [int(key) for key in union.split(' ')]
        dependencies.append(dependency)
    return dependencies


def main():
    lines = get_lines()

    rules = {}
    messages = []

    reading_rules = True

    for line in lines:
        if not line:
            reading_rules = False
            continue
        if reading_rules:
            key, value = line.split(': ')
            key = int(key)
            value = parse_rule(value)
            rules[key] = value
        else:
            messages.append(line)

    valid = set(rules_run(0, rules, {}))

    answer = sum(message in valid for message in messages)
    print(answer)


if __name__ == "__main__":
    main()
