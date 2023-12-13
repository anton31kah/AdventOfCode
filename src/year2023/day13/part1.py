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


def main():
    lines = get_lines('')
    patterns = parse_input(lines)
    i = 0
    score = 0
    for pattern in patterns:
        i += 1
        col, count_around_col = find_reflection(transpose(pattern))
        row, count_around_row = find_reflection(pattern)
        if count_around_col > count_around_row:
            score += col
        elif count_around_row > count_around_col:
            score += row * 100
    print(score)


if __name__ == "__main__":
    main()
