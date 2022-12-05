import re
from src.common.common import get_lines


def batch(lis, n=1):
    l = len(lis)
    for ndx in range(0, l, n):
        yield lis[ndx:min(ndx + n, l)]


def parse_stack_line(line):
    result = {}
    for idx, stack in enumerate(batch(line, 4)):
        ids = re.findall(r'[A-Z]+', stack)
        if len(ids) > 0:
            result[idx + 1] = ids[0]
    return result


def parse_move_line(line):
    return list(map(int, re.findall(r'\d+', line)))


def main():
    lines = get_lines()

    stacks = {}

    stacks_builders = []
    reading_stack = True

    for line in lines:
        if reading_stack:
            if line == '':
                reading_stack = False
            elif line.startswith('['):
                stacks_builders.append(parse_stack_line(line))
            else:
                for builder in stacks_builders:
                    for id, stack_item in builder.items():
                        if id not in stacks:
                            stacks[id] = []
                        stacks[id].append(stack_item)
                for stack in stacks.values():
                    stack.reverse()
        else:
            count, from_id, to_id = parse_move_line(line)
            for i in range(count):
                stacks[to_id].append(stacks[from_id].pop())

    result = ''.join([str(stacks[id][-1]) for id in sorted(stacks)])

    print(result)


if __name__ == "__main__":
    main()
