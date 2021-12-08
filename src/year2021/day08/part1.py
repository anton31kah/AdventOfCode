from src.common.common import get_lines


UNIQUE_LENGTHS = {
    1: 2,
    4: 4,
    7: 3,
    8: 7
}


def parse_input(line):
    input, output = line.split(' | ')
    input = input.split(' ')
    output = output.split(' ')
    return input, output


def main():
    lines = get_lines()

    lines = list(map(parse_input, lines))

    total = 0

    for input, output in lines:
        unique_input = [o for o in output if len(o) in UNIQUE_LENGTHS.values()]
        total += len(unique_input)

    print(total)


if __name__ == "__main__":
    main()
