from src.common.common import get_lines


def parse_command(command):
    direction, amount = command.split()
    return direction, int(amount)


def main():
    lines = get_lines()

    horizontal_position = 0
    depth = 0
    aim = 0

    for command in lines:
        direction, amount = parse_command(command)
        if direction == 'forward':
            horizontal_position += amount
            depth += amount * aim
        elif direction == 'down':
            aim += amount
        elif direction == 'up':
            aim -= amount

    print(horizontal_position * depth)


if __name__ == "__main__":
    main()
