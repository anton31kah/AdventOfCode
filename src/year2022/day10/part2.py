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
        match line.split():
            case ['noop']:
                cycle += 1
                check_state()
            case ['addx', x_increase]:
                cycle += 1
                check_state()

                cycle += 1
                check_state()

                sprite += int(x_increase)

    big_crt = ''.join(crt)
    for line in wrap(big_crt, 40):
        print(line)


if __name__ == "__main__":
    main()
