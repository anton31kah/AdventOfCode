from src.common.common import get_lines


def find_invalid():
    lines = get_lines()
    numbers = list(map(int, lines))

    preamble = []

    invalid = None

    for num in numbers:
        if len(preamble) < 25:
            preamble.append(num)
            continue
        found = False
        if len(preamble) >= 25:
            for x in preamble:
                for y in preamble:
                    if x != y and x + y == num:
                        found = True
                        break
            if not found:
                invalid = num
                break
            preamble.pop(0)
            preamble.append(num)

    return invalid


if __name__ == "__main__":
    invalid = find_invalid()
    print(invalid)
