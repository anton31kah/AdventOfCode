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


def in_bounds(array, index):
    return 0 <= index < len(array)


def count_reflection_rows(pattern, around):
    offset = 0
    while True:
        if (in_bounds(pattern, around + offset)
            and in_bounds(pattern, around - 1 - offset)
            and pattern[around + offset] == pattern[around - 1 - offset]):
            offset += 1
        else:
            break
    return offset


def find_reflection(pattern):
    res = {}
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[i - 1]:
            res[i] = count_reflection_rows(pattern, i)
    if not res:
        return -1, -1

    for around, count in res.items():
        is_start = around - count == 0
        is_end = around + count == len(pattern)
        if is_start or is_end:
            return around, count
    
    return -1, -1


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
    i = 0
    score = 0
    for pattern in patterns:
        i += 1
        old_col = find_reflection(transpose(pattern))
        old_row = find_reflection(pattern)
        cols = []
        rows = []
        for y in range(len(pattern)):
            for x in range(len(pattern[0])):
                new_pattern = flip(pattern, x, y)
                cols.append(find_reflection(transpose(new_pattern)))
                rows.append(find_reflection(new_pattern))
        cols = set([(i, j) for i, j in cols if i >= 0 and j >= 0 and (i, j) != old_col])
        rows = set([(i, j) for i, j in rows if i >= 0 and j >= 0 and (i, j) != old_row])
        print(cols, rows)
        # if count_around_col > count_around_row:
        #     score += col
        # elif count_around_row > count_around_col:
        #     score += row * 100
    print(score)


if __name__ == "__main__":
    main()
