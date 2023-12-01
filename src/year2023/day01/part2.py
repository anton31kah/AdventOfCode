from src.common.common import get_lines


SEARCH_VALUES = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}


def main():
    lines = get_lines('')

    total = 0

    for line in lines:
        smallest_position, first = -1, None
        biggest_position, second = -1, None
        for key, value in SEARCH_VALUES.items():
            pos = line.find(key)
            if pos >= 0 and (pos < smallest_position or smallest_position < 0):
                smallest_position = pos
                first = value
            pos = line.rfind(key)
            if pos >= 0 and (pos > biggest_position or biggest_position < 0):
                biggest_position = pos
                second = value
        num = first * 10 + second
        total += num
    print(total)


if __name__ == "__main__":
    main()
