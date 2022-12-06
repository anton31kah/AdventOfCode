from src.common.common import get_lines


def main():
    lines = get_lines()
    line = lines[0]

    index = 4

    while True:
        if len(set(line[index - 4:index])) == 4:
            break
        index += 1

    print(index)


if __name__ == "__main__":
    main()
