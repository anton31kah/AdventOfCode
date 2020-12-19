import itertools
from src.common.common import get_lines


def find_first_startswith(string, prefixes):
    for prefix in prefixes:
        if string.startswith(prefix):
            return prefix
    return None


def find_first_endswith(string, suffixes):
    for suffix in suffixes:
        if string.endswith(suffix):
            return suffix
    return None


def check(message: str, v42, v31):
    v42_count = 0
    v31_count = 0

    prefix = find_first_startswith(message, v42)
    while prefix:
        v42_count += 1
        message = message[len(prefix):]
        prefix = find_first_startswith(message, v42)

    suffix = find_first_endswith(message, v31)
    while suffix:
        v31_count += 1
        message = message[:-len(suffix)]
        suffix = find_first_endswith(message, v31)

    return not message and v42_count > v31_count > 0


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

    rules[8] = parse_rule('42 | 42 8')
    rules[11] = parse_rule('42 31 | 42 11 31')

    valid42 = set(rules_run(42, rules, {}))
    valid31 = set(rules_run(31, rules, {}))

    total_valid = 0

    for message in messages:
        total_valid += check(message, valid42, valid31)

    print(total_valid)


if __name__ == "__main__":
    main()
