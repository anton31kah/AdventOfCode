from textwrap import wrap
from src.common.common import get_lines


def main():
    lines = get_lines('')

    crt = []
    sprite = 1
    cycle = 0

    def check_state():
        nonlocal crt

        if (cycle % 40) - 1 in range(sprite - 1, sprite + 2):
            crt.append('#')
        else:
            crt.append('.')

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

            sprite += x_increase

    big_crt = ''.join(crt)
    for line in wrap(big_crt, 40):
        print(line)


if __name__ == "__main__":
    main()
