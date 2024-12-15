from src.common.common import get_lines


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
            position = row, col
            match cell:
                case '#':
                    obstacles.add(position)
                    rows = max(rows, row + 1)
                    cols = max(cols, col + 1)
                case 'O':
                    boxes.add(position)
                case '@':
                    robot = position
                case '>' | '<' | '^' | 'v':
                    moves.append(arrow_to_delta(cell))

    return obstacles, boxes, robot, moves, (rows, cols)


def print_game(obstacles, boxes, robot, grid_end):
    (rows, cols) = grid_end

    for row in range(rows):
        for col in range(cols):
            pos = row, col
            printed = 0
            if pos in obstacles:
                print('#', end='')
                printed += 1
            if pos in boxes:
                print('O', end='')
                printed += 1
            if pos == robot:
                print('@', end='')
                printed += 1
            match printed:
                case 0:
                    print('.', end='')
                case 1:
                    pass
                case _:
                    raise ValueError(f'Overlap in {pos}: obstacles={pos in obstacles} boxes={pos in boxes} robot={pos == robot}')
        print()
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

        if (nx, ny) in obstacles:
            # print(f'after {delta_to_arrow((dx, dy))} (new robot in obstacle - skip):')
            # print_game(obstacles, boxes, robot, grid_end)
            continue

        if (nx, ny) in boxes:
            boxes_to_move = [(nx, ny)]

            bx, by = boxes_to_move[-1]
            while (bx+dx, by+dy) in boxes:
                boxes_to_move.append((bx+dx, by+dy))
                bx, by = boxes_to_move[-1]
            
            if (bx+dx, by+dy) in obstacles:
                # print(f'after {delta_to_arrow((dx, dy))} (boxes in obstacle - skip):')
                # print_game(obstacles, boxes, robot, grid_end)
                continue

            boxes.difference_update(boxes_to_move)
            moved_boxes = boxes_to_move[1:] + [(bx+dx, by+dy)]
            boxes.update(moved_boxes)
        
        robot = nx, ny

        # print(f'after {delta_to_arrow((dx, dy))} (moved):')
        # print_game(obstacles, boxes, robot, grid_end)
    
    total = 0
    for x, y in boxes:
        total += 100 * x + y
    print(total)


if __name__ == "__main__":
    main()
