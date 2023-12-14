from src.common.common import get_lines


def parse_input(lines):
    all_patterns = []
    current = []

    for line in lines:
        if line:
            current.append(line)
        else:
            all_patterns.append(current)
            current = []
    all_patterns.append(current)
    current = []

    return all_patterns


def transpose(pattern):
    return [''.join(i) for i in zip(*pattern)]


def find_reflection_start(pattern, ignore=None):
    for i in range(len(pattern) // 2, 0, -1):
        if pattern[:i] == list(reversed(pattern[i:i*2])) and (ignore is None or i != ignore):
            return i
    return -1


def find_reflection_end(pattern, ignore=None):
    for i in range(len(pattern) // 2, 0, -1):
        if pattern[-i:] == list(reversed(pattern[-i*2:-i])) and (ignore is None or len(pattern) - i != ignore):
            return len(pattern) - i
    return -1


def find_reflection(pattern, ignore=None):
    end = find_reflection_end(pattern, ignore)
    if end >= 1:
        return end
    start = find_reflection_start(pattern, ignore)
    if start >= 1:
        return start
    return -1


def flip(pattern, x, y):
    def flip_pattern_item(item):
        if item == '#':
            return '.'
        else:
            return '#'

    copy = [list(line) for line in pattern]
    copy[y][x] = flip_pattern_item(copy[y][x])
    return [''.join(line) for line in copy]


def main():
    lines = get_lines('')
    patterns = parse_input(lines)
    score = 0
    for pattern in patterns:
        old_col = find_reflection(transpose(pattern))
        old_row = find_reflection(pattern)
        cols = set()
        rows = set()
        for y in range(len(pattern)):
            for x in range(len(pattern[0])):
                new_pattern = flip(pattern, x, y)
                new_col = find_reflection(transpose(new_pattern), old_col)
                if new_col >= 1 and new_col != old_col:
                    cols.add(new_col)
                new_row = find_reflection(new_pattern, old_row)
                if new_row >= 1 and new_row != old_row:
                    rows.add(new_row)
        score += next(iter(cols), 0) + next(iter(rows), 0) * 100
    print(score)


if __name__ == "__main__":
    main()
