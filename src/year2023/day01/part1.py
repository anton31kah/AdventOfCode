from src.common.common import get_lines


def main():
    lines = get_lines('')

    total = 0

    for line in lines:
        first = None
        second = None
        for c in line:
            if c.isdigit():
                first = int(c)
                break
        for c in line[::-1]:
            if c.isdigit():
                second = int(c)
                break
        num = first * 10 + second
        total += num
    
    print(total)


if __name__ == "__main__":
    main()
