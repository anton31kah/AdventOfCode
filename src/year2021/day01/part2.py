from src.common.common import get_lines


def main():
    lines = get_lines()

    numbers = list(map(int, lines))
    increases = 0
    last3 = [*numbers[:3]]

    for i in range(3, len(numbers)):
        sum_prev = sum(last3)
        last3.pop(0)
        last3.append(numbers[i])
        sum_next = sum(last3)
        if sum_next > sum_prev:
            increases += 1

    print(increases)


if __name__ == "__main__":
    main()
