from src.common.common import get_lines

BRACKET_START = ['(', '[', '{', '<']
BRACKET_END = [')', ']', '}', '>']

ERROR_POINTS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}


def are_match(bracket_start, bracket_end):
    return BRACKET_START.index(bracket_start) == BRACKET_END.index(bracket_end)


def main():
    lines = get_lines()

    errors = {bracket: 0 for bracket in BRACKET_END}

    for line in lines:
        stack = []
        for bracket in line:
            if bracket in BRACKET_START:
                stack.append(bracket)
            else:
                last = stack.pop()
                if not are_match(last, bracket):
                    errors[bracket] += 1

    total = sum(ERROR_POINTS[bracket] * count for bracket, count in errors.items())

    print(total)


if __name__ == "__main__":
    main()
