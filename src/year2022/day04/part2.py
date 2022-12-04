from src.common.common import get_lines


def overlap(a, b):
    a1, a2 = a
    b1, b2 = b
    return b1 <= a1 <= b2 or a1 <= b1 <= a2


def main():
    lines = get_lines()

    total = 0

    for line in lines:
        r1, r2 = line.split(',')
        r1 = list(map(int, r1.split('-')))
        r2 = list(map(int, r2.split('-')))
        
        if overlap(r1, r2):
            total += 1

    print(total)


if __name__ == "__main__":
    main()
