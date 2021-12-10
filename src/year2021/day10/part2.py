from src.common.common import get_lines

BRACKET_START = ['(', '[', '{', '<']
BRACKET_END = [')', ']', '}', '>']

AUTOCOMPLETE_POINTS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


def are_match(bracket_start, bracket_end):
    return BRACKET_START.index(bracket_start) == BRACKET_END.index(bracket_end)


def reverse_bracket(bracket):
    if bracket in BRACKET_START:
        return BRACKET_END[BRACKET_START.index(bracket)]
    elif bracket in BRACKET_END:
        return BRACKET_START[BRACKET_END.index(bracket)]
    raise Exception(f"Invalid bracket character {bracket}")


def main():
    lines = get_lines()

    all_scores = []

    for line in lines:
        stack = []

        is_corrupted = False

        for bracket in line:
            if bracket in BRACKET_START:
                stack.append(bracket)
            else:
                last = stack.pop()
                if not are_match(last, bracket):
                    is_corrupted = True
                    break

        if is_corrupted:
            continue

        autocompleted = [reverse_bracket(bracket) for bracket in stack[::-1]]

        line_points = 0

        for bracket in autocompleted:
            line_points *= 5
            line_points += AUTOCOMPLETE_POINTS[bracket]

        all_scores.append(line_points)

    all_scores.sort()

    middle = len(all_scores) // 2

    print(all_scores[middle])


if __name__ == "__main__":
    main()
