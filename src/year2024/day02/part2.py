from src.common.common import get_lines


def determine_if_increasing(levels):
    for a, b in zip(levels, levels[1:]):
        if a > b:
            return False
        elif a < b:
            return True
    return None


def all_combinations(levels):
    yield levels
    for i in range(len(levels)):
        yield levels[:i] + levels[i + 1:]


def main():
    lines = get_lines('')

    total_safe = 0

    for line in lines:
        initial_levels = list(map(int, line.split()))
        for levels in all_combinations(initial_levels):
            increasing = determine_if_increasing(levels)
            safe = True
            for a, b in zip(levels, levels[1:]):
                diff = b - a
                if (increasing and not (1 <= diff <= 3)) or (not increasing and not (-3 <= diff <= -1)):
                    safe = False
                    break
            if safe:
                total_safe += 1
                break
    
    print(total_safe)


if __name__ == "__main__":
    main()
