from src.common.common import get_lines


def main():
    lines = get_lines()
    line = lines[0]

    length = 14

    index = length

    while True:
        if len(set(line[index - length:index])) == length:
            break
        index += 1

    print(index)


if __name__ == "__main__":
    main()
