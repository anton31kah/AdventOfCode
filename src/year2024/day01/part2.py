from src.common.common import get_lines
from collections import Counter


def main():
    lines = get_lines()

    left = []
    right = Counter()

    for line in lines:
        l, r = line.split()
        l, r = int(l), int(r)
        left.append(l)
        right[r] += 1

    score = 0

    for l in left:
        score += l * right[l]
    
    print(score)


if __name__ == "__main__":
    main()
