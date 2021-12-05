from dataclasses import dataclass

from src.common.common import get_lines


@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int


def read_line(line) -> Line:
    point1, point2 = line.split(' -> ')
    x1, y1 = point1.split(',')
    x2, y2 = point2.split(',')
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    return Line(x1, y1, x2, y2)


def generate_board(lines: list[Line]):
    max_x = max(max(lines, key=lambda line: line.x1).x1, max(lines, key=lambda line: line.x2).x2)
    max_y = max(max(lines, key=lambda line: line.y1).y1, max(lines, key=lambda line: line.y2).y2)
    return [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]


def generate_points(line: Line):
    # https://en.wikipedia.org/wiki/Digital_differential_analyzer_(graphics_algorithm)

    dx = line.x2 - line.x1
    dy = line.y2 - line.y1

    step = max(abs(dx), abs(dy))

    dx = dx / step
    dy = dy / step

    x = line.x1
    y = line.y1

    dots = []

    for i in range(1, step + 1):
        dots.append((int(x), int(y)))
        x = x + dx
        y = y + dy

    if (line.x1, line.y1) not in dots:
        dots.append((line.x1, line.y1))

    if (line.x2, line.y2) not in dots:
        dots.append((line.x2, line.y2))

    return dots


def print_board(board):
    for row in board:
        print(''.join([str(col) if col > 0 else '.' for col in row]))
    print()


def mark_board(board, line: Line):
    points = generate_points(line)
    # print(line, points)
    for (x, y) in points:
        board[y][x] += 1
    # print_board(board)


def main():
    lines = get_lines()

    lines = [read_line(line) for line in lines]
    # lines = list(filter(lambda line: line.x1 == line.x2 or line.y1 == line.y2, lines))

    board = generate_board(lines)

    for line in lines:
        mark_board(board, line)

    total = 0

    for row in board:
        for col in row:
            if col >= 2:
                total += 1

    print(total)
    # print_board(board)


if __name__ == "__main__":
    main()
