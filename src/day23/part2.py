from collections import deque
from src.common.common import get_lines


def fulfill_cups(cups):
    cups.extend(range(max(cups) + 1, 1000001))
    return cups


def remove_cups(cups, after, n=3):
    after_idx = cups.index(after)
    removed_cups = [cups[i % len(cups)] for i in range(after_idx + 1, after_idx + 4)]
    new_cups = [cup for cup in cups if cup not in removed_cups]
    return new_cups, removed_cups


def find_destination(cups, current):
    current -= 1
    while current not in cups:
        if current < min(cups):
            current = max(cups)
            break
        current -= 1
    return current


def add_cups(cups, to_add, after):
    after_idx = cups.index(after)
    cups[after_idx + 1:after_idx + 1] = to_add
    return cups


def find_new_current(cups, current):
    current_idx = cups.index(current)
    current_idx += 1
    current_idx %= len(cups)
    current = cups[current_idx]
    return current


def after_cup(cups, after, n):
    idx = cups.index(after)
    new_cups = []
    while len(new_cups) < n:
        idx += 1
        idx %= len(cups)
        new_cups.append(cups[idx])
    return new_cups


def main():
    lines = get_lines()
    cups = list(map(int, lines[0]))
    cups = [3, 8, 9, 1, 2, 5, 4, 6, 7]

    cups = deque(fulfill_cups(cups))

    current = cups[0]

    try:
        for move in range(1, 10000001):
            cups, removed = remove_cups(cups, current)
            destination = find_destination(cups, current)
            cups = add_cups(cups, removed, destination)
            current = find_new_current(cups, current)
    except KeyboardInterrupt:
        print('move', move)
        exit()

    after_1 = after_cup(cups, 1, 2)
    print(after_1)
    print(after_1[0] * after_1[1])


if __name__ == "__main__":
    main()
