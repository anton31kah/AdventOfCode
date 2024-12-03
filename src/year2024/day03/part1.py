from src.common.common import get_lines
import re


def main():
    lines = get_lines('')

    full_input = ''.join(lines)

    regex = r"mul\((\d+),(\d+)\)"

    matches = re.finditer(regex, full_input, re.MULTILINE)

    result = 0

    for match in matches:
        result += int(match.group(1)) * int(match.group(2))
    
    print(result)


if __name__ == "__main__":
    main()
