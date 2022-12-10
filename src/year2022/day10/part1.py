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
        if line.startswith('noop'):
            cycle += 1
            check_state()
        elif line.startswith('addx'):
            _, x_increase = line.split(' ')
            x_increase = int(x_increase)

            cycle += 1
            check_state()

            cycle += 1
            check_state()

            state_x += x_increase

    print(total)


if __name__ == "__main__":
    main()
