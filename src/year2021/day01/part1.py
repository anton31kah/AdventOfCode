from src.common.common import get_lines


def main():
    lines = get_lines()

    numbers = list(map(int, lines))
    increases = 0

    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i - 1]:
            increases += 1

    print(increases)


if __name__ == "__main__":
    main()
