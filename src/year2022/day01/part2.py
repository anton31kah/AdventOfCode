from src.common.common import get_lines


def main():
    lines = get_lines()

    cals = []
    curr = 0

    for line in lines:
        if line:
            curr += int(line)
        else:
            cals.append(curr)
            curr = 0

    cals.append(curr)
    
    res = sum(sorted(cals)[-3:])

    print(res)


if __name__ == "__main__":
    main()
