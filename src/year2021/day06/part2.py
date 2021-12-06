from collections import Counter
from src.common.common import get_lines


"""
Counter() == defaultdict(lambda: 0) == dict with default value
"""


def print_dict(fish):
    return ','.join((str(life) for life, count in sorted(fish.items()) for _ in range(count)))


def main():
    lines = get_lines()

    # life days -> fish count with same life days
    lantern_fish = Counter()

    for fish in (int(x) for x in lines[0].split(',')):
        lantern_fish[fish] += 1

    day = 0

    while day < 256:
        # print(day, print_dict(lantern_fish))

        min_fish = min(lantern_fish.keys()) + 1

        new_lantern_fish = Counter()

        for life, fish_count in lantern_fish.items():
            new_lantern_fish[life - min_fish] = fish_count

        day += min_fish

        lantern_fish = new_lantern_fish
        del new_lantern_fish

        lantern_fish[6] += lantern_fish[-1]
        lantern_fish[8] += lantern_fish[-1]
        lantern_fish.pop(-1)

    # print(day, print_dict(lantern_fish))
    print(sum(lantern_fish.values()))


if __name__ == "__main__":
    main()
