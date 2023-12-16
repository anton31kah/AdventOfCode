from src.common.common import get_lines
import time


def parse_input(lines):
    elements = {
        '|': set(),
        '-': set(),
        '/': set(),
        '\\': set(),
        '#': set()
    }

    for y, line in enumerate(lines):
        for x, elem in enumerate(line):
            if elem in elements:
                elements[elem].add((x, y))

    elements['#'].add((-1, -1))
    for x in range(len(lines[0])):
        elements['#'].add((x, -1))
    elements['#'].add((len(lines[0]), -1))
    
    for y, line in enumerate(lines):
        elements['#'].add((-1, y))
        elements['#'].add((len(line), y))

    elements['#'].add((-1, len(lines)))
    for x in range(len(lines[0])):
        elements['#'].add((x, len(lines)))
    elements['#'].add((len(lines[0]), len(lines)))
    
    return elements


def add_wall(lines, elements):
    elements['#'].add((-1, -1))
    for x in range(len(lines[0])):
        elements['#'].add((x, -1))
    elements['#'].add((len(lines[0]), -1))
    
    for y, line in enumerate(lines):
        elements['#'].add((-1, y))
        elements['#'].add((len(line), y))

    elements['#'].add((-1, len(lines)))
    for x in range(len(lines[0])):
        elements['#'].add((x, len(lines)))
    elements['#'].add((len(lines[0]), len(lines)))


def print_beams(beams, elements, width, height):
    for y in range(-1, height + 1):
        for x in range(-1, width + 1):
            found = False
            for elem, positions in elements.items():
                if (x, y) in positions:
                    found = True
                    print(elem, end='')
                    break
            if not found:
                for beam in beams:
                    if (x, y) in map(lambda t: t[0], beam):
                        found = True
                        print('#', end='')
                        break
            if not found:
                print('.', end='')
        print()


def print_energized(energized, width, height):
    for y in range(height):
        for x in range(width):
            if (x, y) in energized:
                print('#', end='')
            else:
                print('.', end='')
        print()


def find_beams(elements, start):
    beams = [[start]]

    visited = set()
    visited.add(start)

    while True:
        beams_moved = 0

        new_beams = []

        for i in range(len(beams)):
            beam = beams[i]

            last_position, direction = beam[-1]

            current_element = None

            for elem, positions in elements.items():
                if last_position in positions:
                    current_element = elem
                    break

            if current_element is None:
                current_element = '.'

            new_direction = None
            new_position = None
            x, y = last_position

            match current_element:
                case '-':
                    match direction:
                        case '>':
                            new_position = x + 1, y
                            new_direction = direction
                        case '<':
                            new_position = x - 1, y
                            new_direction = direction
                        case 'v' | '^':
                            new_position = x + 1, y
                            new_direction = '>'
                            new_beams.append(((x - 1, y), '<'))
                case '|':
                    match direction:
                        case 'v':
                            new_position = x, y + 1
                            new_direction = direction
                        case '^':
                            new_position = x, y - 1
                            new_direction = direction
                        case '>' | '<':
                            new_position = x, y + 1
                            new_direction = 'v'
                            new_beams.append(((x, y - 1), '^'))
                case '/':
                    match direction:
                        case 'v':
                            new_position = x - 1, y
                            new_direction = '<'
                        case '^':
                            new_position = x + 1, y
                            new_direction = '>'
                        case '<':
                            new_position = x, y + 1
                            new_direction = 'v'
                        case '>':
                            new_position = x, y - 1
                            new_direction = '^'
                case '\\':
                    match direction:
                        case 'v':
                            new_position = x + 1, y
                            new_direction = '>'
                        case '^':
                            new_position = x - 1, y
                            new_direction = '<'
                        case '<':
                            new_position = x, y - 1
                            new_direction = '^'
                        case '>':
                            new_position = x, y + 1
                            new_direction = 'v'
                case '.':
                    match direction:
                        case 'v':
                            new_position = x, y + 1
                            new_direction = 'v'
                        case '^':
                            new_position = x, y - 1
                            new_direction = '^'
                        case '<':
                            new_position = x - 1, y
                            new_direction = '<'
                        case '>':
                            new_position = x + 1, y
                            new_direction = '>'

            if new_position and new_direction:
                if (new_position, new_direction) not in visited:
                    beams[i].append((new_position, new_direction))
                    visited.add((new_position, new_direction))
                    beams_moved += 1
        
        for beam_position, beam_direction in new_beams:
            beams.append([(beam_position, beam_direction)])

        if not beams_moved:
            break

    return beams


def find_energized(beams, width, height):
    points = set()

    for beam in beams:
        for (x, y), _ in beam:
            if 0 <= x < width and 0 <= y < height:
                points.add((x, y))
    
    return points


def solve(elements, width, height, start):
    beams = find_beams(elements, start)
    energized = find_energized(beams, width, height)
    return len(energized)


def timed_solve(elements, width, height, start):
    time_start = time.time()

    score = solve(elements, width, height, start)

    time_end = time.time()

    print('took', round(time_end - time_start, 2), 'seconds for point', start, 'and found', score)

    return score


def main():
    lines = get_lines('')
    width, height = len(lines[0]), len(lines)
    elements = parse_input(lines)
    add_wall(lines, elements)

    max_energized = 0

    for y in range(height):
        start = ((0, y), '>')
        max_energized = max(max_energized, timed_solve(elements, width, height, start))

        start = ((width - 1, y), '<')
        max_energized = max(max_energized, timed_solve(elements, width, height, start))

    for x in range(width):
        start = ((x, 0), 'v')
        max_energized = max(max_energized, timed_solve(elements, width, height, start))

        start = ((x, height - 1), '^')
        max_energized = max(max_energized, timed_solve(elements, width, height, start))

    print(max_energized)


if __name__ == "__main__":
    main()
