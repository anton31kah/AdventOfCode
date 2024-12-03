from src.common.common import get_lines
import re


def main():
    lines = get_lines('')

    full_input = ''.join(lines)

    regex = r"(mul\((\d+),(\d+)\))|(do\(\))|(don't\(\))"

    matches = re.finditer(regex, full_input, re.MULTILINE)

    result = 0

    do = True

    for match in matches:
        part = match.group()
        if part.startswith('mul') and do:
            result += int(match.group(2)) * int(match.group(3))
        elif part == 'do()':
            do = True
        elif part == "don't()":
            do = False
    
    print(result)


if __name__ == "__main__":
    main()
