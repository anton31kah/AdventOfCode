from src.common.common import get_lines
import re


def find_value(text, search):
    return int(re.search('(\d+) ' + search, text).group(1)) if search in text else 0


def parse_line(line):
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    game_str, cubes_str = line.split(': ')
    id = int(game_str.split(':')[0].split(' ')[1])
    cubes_str_arr = cubes_str.split('; ')
    cubes_arr = [(find_value(x, 'red'), find_value(x, 'green'), find_value(x, 'blue')) for x in cubes_str_arr]
    return id, cubes_arr


def main():
    lines = get_lines('')

    total = 0

    for line in lines:
        id, cubes = parse_line(line)
        r = max(r for r, g, b in cubes)
        g = max(g for r, g, b in cubes)
        b = max(b for r, g, b in cubes)
        value = r * g * b
        total += value
    
    print(total)


if __name__ == "__main__":
    main()
