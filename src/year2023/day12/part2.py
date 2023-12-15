from src.common.common import get_lines
from functools import cache


def parse_line(line):
    springs, groups = line.split()

    groups = tuple(int(x) for x in groups.split(','))

    springs = '?'.join(([springs] * 5))
    groups = tuple(i for _ in range(5) for i in groups)

    return springs, groups


@cache
def solve(springs, groups):
    if not springs and not groups:
        return True
    if not springs:
        return False
    if not groups:
        return '#' not in springs
    
    min_springs = sum(groups) + len(groups) - 1 # 1,1,3 -> (1+1+3)*'#' + 2*'.'
    if len(springs) < min_springs:
        return False;

    springs_head, springs_tail = springs[0], springs[1:]
    groups_head, groups_tail = groups[0], groups[1:]

    match springs_head:
        case '#':
            if '.' in springs[:groups_head] or springs[groups_head] == '#':
                return False
            return solve(springs[groups_head + 1:], groups_tail)
        case '.':
            return solve(springs_tail, groups)
        case '?':
            return solve('#' + springs_tail, groups) + solve('.' + springs_tail, groups)


def main():
    lines = get_lines('')

    total = 0

    progress = 0

    for line in lines:
        progress += 1
        springs, groups = parse_line(line)
        total += solve(springs + '.', groups) # add . to make if check easier
    
    print(total)


if __name__ == "__main__":
    main()
