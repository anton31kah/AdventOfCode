from src.common.common import get_lines


def fuel_consumption(crabs, position):
    return sum(abs(c - position) for c in crabs)


def main():
    lines = get_lines()

    crabs = [int(p) for p in lines[0].split(',')]

    lower, upper = min(crabs), max(crabs)
    middle = (lower + upper) // 2

    consumption = fuel_consumption(crabs, middle)
    min_fuel = consumption

    ranges_to_try = ((lower, middle), (middle, upper))

    while True:
        (left_lower, left_upper), (right_lower, right_upper) = ranges_to_try

        if left_lower == left_upper or right_lower == right_upper:
            break

        left_consumption = fuel_consumption(crabs, (left_lower + left_upper) // 2)
        right_consumption = fuel_consumption(crabs, (right_lower + right_upper) // 2)

        if left_consumption < right_consumption:
            min_fuel = left_consumption
            left_middle = (left_lower + left_upper) // 2
            ranges_to_try = ((left_lower, left_middle), (left_middle, left_upper))
        else:
            min_fuel = right_consumption
            right_middle = (right_lower + right_upper) // 2
            ranges_to_try = ((right_lower, right_middle), (right_middle, right_upper))

    print(min_fuel)


if __name__ == "__main__":
    main()
