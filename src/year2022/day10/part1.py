from src.common.common import get_lines


def main():
    lines = get_lines('')

    cycles_to_check = [20, 60, 100, 140, 180, 220]

    total = 0
    state_x = 1
    cycle = 0

    def check_state():
        nonlocal total

        if cycle in cycles_to_check:
            total += cycle * state_x

    for line in lines:
        match line.split():
            case ['noop']:
                cycle += 1
                check_state()
            case ['addx', x_increase]:
                cycle += 1
                check_state()

                cycle += 1
                check_state()

                state_x += int(x_increase)

    print(total)


if __name__ == "__main__":
    main()
