from src.common.common import get_lines


def main():
    lines = get_lines()

    lantern_fish = [int(x) for x in lines[0].split(',')]

    for day in range(80):
        # print(day, lantern_fish)
        fish_to_add = 0
        for fish_idx in range(len(lantern_fish)):
            lantern_fish[fish_idx] -= 1
            if lantern_fish[fish_idx] < 0:
                lantern_fish[fish_idx] = 6
                fish_to_add += 1
        for idx in range(fish_to_add):
            lantern_fish.append(8)

    print(len(lantern_fish))


if __name__ == "__main__":
    main()
