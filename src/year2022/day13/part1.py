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
            if a == b:
                return None
            return a < b
        case list(a), list(b):
            for i in range(max(len(a), len(b))):
                if i >= len(a):
                    return True
                if i >= len(b):
                    return False
                items_comparison = compare_packets(a[i], b[i])
                if items_comparison is not None:
                    return items_comparison
            return None
        case list(a), int(b):
            return compare_packets(a, [b])
        case int(a), list(b):
            return compare_packets([a], b)

    raise ValueError('Weird input', packet1, packet2)


def main():
    lines = get_lines('')

    pairs = [[]]

    for line in lines:
        if len(line) == 0:
            pairs.append([])
            continue
        pairs[-1].append(parse_packet(line))

    in_right_order = []

    for idx, pair in enumerate(pairs, start=1):
        if compare_packets(*pair) is not False:
            in_right_order.append(idx)

    print(in_right_order)
    print(sum(in_right_order))


if __name__ == "__main__":
    main()
