import functools
import re
from src.common.common import get_lines


def parse_packet(text):
    result = None
    current = []

    for token in re.split(r'(\[|\]|\d+|,)', text):
        match token:
            case '[':
                lis = []
                if result is None:
                    result = lis
                else:
                    current[-1].append(lis)
                current.append(lis)
            case ']':
                current.pop()
            case num if num.isdigit():
                current[-1].append(int(num))

    return result


def compare_packets(packet1, packet2):
    match packet1, packet2:
        case int(a), int(b):
            return a - b
        case list(a), list(b):
            for i in range(max(len(a), len(b))):
                if i >= len(a):
                    return -1
                if i >= len(b):
                    return 1
                items_comparison = compare_packets(a[i], b[i])
                if items_comparison != 0:
                    return items_comparison
            return 0
        case list(a), int(b):
            return compare_packets(a, [b])
        case int(a), list(b):
            return compare_packets([a], b)

    raise ValueError('Weird input', packet1, packet2)


def main():
    lines = get_lines('')

    lines.append('[[2]]')
    lines.append('[[6]]')

    packets = []

    for line in lines:
        if len(line) > 0:
            packets.append(parse_packet(line))

    packets.sort(key=functools.cmp_to_key(compare_packets))

    # for packet in packets:
    #     print(packet)

    index2 = packets.index([[2]]) + 1
    index6 = packets.index([[6]]) + 1

    print(index2 * index6)


if __name__ == "__main__":
    main()
