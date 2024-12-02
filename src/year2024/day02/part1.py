from src.common.common import get_lines


def determine_if_increasing(levels):
    for a, b in zip(levels, levels[1:]):
        if a > b:
            return False
        elif a < b:
            return True
    return None


def main():
    lines = get_lines('')

    total_safe = 0

    for line in lines:
        levels = list(map(int, line.split()))
        increasing = determine_if_increasing(levels)
        safe = True
        for a, b in zip(levels, levels[1:]):
            diff = b - a
            if (increasing and not (1 <= diff <= 3)) or (not increasing and not (-3 <= diff <= -1)):
                safe = False
                break
        if safe:
            total_safe += 1
    
    print(total_safe)


if __name__ == "__main__":
    main()
