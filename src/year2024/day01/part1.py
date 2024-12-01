from src.common.common import get_lines


def main():
    lines = get_lines()

    left = []
    right = []

    for line in lines:
        l, r = line.split()
        l, r = int(l), int(r)
        left.append(l)
        right.append(r)
    
    left = sorted(left)
    right = sorted(right)

    distance = 0

    for l, r in zip(left, right):
        distance += abs(l - r)
    
    print(distance)


if __name__ == "__main__":
    main()
