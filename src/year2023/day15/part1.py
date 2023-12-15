from src.common.common import get_lines


def hash(part):
    res = 0
    for c in part:
        res += ord(c)
        res *= 17
        res %= 256
    return res


def main():
    lines = get_lines('')
    parts = lines[0].split(',')
    total = sum(hash(part) for part in parts)
    print(total)


if __name__ == "__main__":
    main()
