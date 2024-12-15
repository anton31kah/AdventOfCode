from src.common.common import get_lines
from collections import deque


def arrow_to_delta(arrow):
    match arrow:
        case '>':
            return ( 0, +1)
        case '<':
            return ( 0, -1)
        case 'v':
            return (+1,  0)
        case '^':
            return (-1,  0)
    raise ValueError(f'Invalid arrow {arrow}!')


def delta_to_arrow(delta):
    match delta:
        case (0, 1):
            return '>'
        case (0, -1):
            return '<'
        case (1, 0):
            return 'v'
        case (-1, 0):
            return '^'
    raise ValueError(f'Invalid delta {delta}!')


def parse_input(lines):
    obstacles = set()
    boxes = set()
    robot = None
    moves = []
    rows, cols = 0, 0

    for row, line in enumerate(lines):
        for col, cell in enumerate(line):
            position = row, 2 * col
            match cell:
                case '#':
                    obstacles.add(position)
                    rows = max(rows, row + 1)
                    cols = max(cols, 2 * col + 2)
                case 'O':
                    boxes.add(position)
                case '@':
                    robot = position
                case '>' | '<' | '^' | 'v':
                    moves.append(arrow_to_delta(cell))

    return obstacles, boxes, robot, moves, (rows, cols)


def wide_in(element, iterable, wide_element=True):
    x, y = element
    matching = []
    for xx, yy in iterable:
        if (x, y) == (xx, yy) or (x, y) == (xx, yy + 1) or (wide_element and (x, y + 1) == (xx, yy)):
            matching.append((xx, yy))
    return matching


def print_game(obstacles, boxes, robot, grid_end):
    (rows, cols) = grid_end

    for row in range(rows):
        line = ['.'] * cols
        for col in range(cols):
            pos = row, col
            printed = 0
            if pos in obstacles:
                line[col:col+2] = ['#', '#']
                printed += 1
            if pos in boxes:
                line[col:col+2] = ['[', ']']
                printed += 1
            if pos == robot:
                line[col:col+2] = ['@', '.']
                printed += 1
            if printed >= 2:
                raise ValueError(f'Overlap in {pos}: obstacles={pos in obstacles} boxes={pos in boxes} robot={pos == robot}')
        print(''.join(line))
    print()
    print()


def main():
    lines = get_lines('')

    obstacles, boxes, robot, moves, grid_end = parse_input(lines)

    # print('initial state:')
    # print_game(obstacles, boxes, robot, grid_end)

    for dx, dy in moves:
        x, y = robot
        nx, ny = x + dx, y + dy

        if wide_in((nx, ny), obstacles, wide_element=False):
            # print(f'after {delta_to_arrow((dx, dy))} (new robot in obstacle - skip):')
            # print_game(obstacles, boxes, robot, grid_end)
            continue

        if robot_box_hit := wide_in((nx, ny), boxes, wide_element=False):
            queue = deque([])

            cannot_move = False
            new_boxes = set()
            old_boxes = set()
            
            # robot_box_hit is a list of a single element
            # robot can always only push a single box
            queue.append(robot_box_hit)

            while queue:
                current_boxes = queue.popleft()
                for box in current_boxes:
                    if box in old_boxes:
                        continue
                    bx, by = box
                    moved_box = bx + dx, by + dy
                    old_boxes.add(box)
                    new_boxes.add(moved_box)
                    if wide_in(moved_box, obstacles, wide_element=True):
                        cannot_move = True
                        break
                    if box_box_hit := wide_in(moved_box, boxes, wide_element=True):
                        queue.append(box_box_hit)

            if cannot_move:
                # print(f'after {delta_to_arrow((dx, dy))} (boxes in obstacle - skip):')
                # print_game(obstacles, boxes, robot, grid_end)
                continue

            boxes.difference_update(old_boxes)
            boxes.update(new_boxes)
        
        robot = nx, ny

        # print(f'after {delta_to_arrow((dx, dy))} (moved):')
        # print_game(obstacles, boxes, robot, grid_end)
    
    total = 0
    for x, y in boxes:
        total += 100 * x + y
    print(total)


if __name__ == "__main__":
    main()
