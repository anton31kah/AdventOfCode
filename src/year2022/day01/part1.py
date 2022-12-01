from src.common.common import get_lines


def main():
    lines = get_lines()

    max_cal = -1
    curr = 0

    for line in lines:
        if line:
            curr += int(line)
        else:
            max_cal = max(max_cal, curr)
            curr = 0

    max_cal = max(max_cal, curr)

    print(max_cal)


if __name__ == "__main__":
    main()
