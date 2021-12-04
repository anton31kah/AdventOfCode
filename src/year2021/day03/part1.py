from collections import Counter
from src.common.common import get_lines


def transpose(lines):
    return list(map(list, zip(*lines)))


def bit_not(n, numbits=8):
    return (1 << numbits) - 1 - n


def main():
    lines = get_lines()

    transposed = transpose(lines)
    gamma = ''

    for item in transposed:
        data = Counter(item)
        gamma += data.most_common(1)[0][0]

    bits_count = len(gamma)
    gamma = int(gamma, base=2)
    epsilon = bit_not(gamma, bits_count)

    power_consumption = gamma * epsilon

    print(power_consumption)


if __name__ == "__main__":
    main()
