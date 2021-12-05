from src.common.common import get_lines


def read_board(lines):
    board = []

    for line in lines:
        row = [int(num) for num in line.strip().split()]
        board.append(row)

    return board


def read_input(lines):
    numbers = [int(num) for num in lines[0].split(',')]

    boards = []

    for idx in range(1, len(lines), 6):
        boards.append(read_board(lines[idx + 1:idx + 6]))

    return numbers, boards


def generate_marker_board():
    return [[False for _ in range(5)] for _ in range(5)]


def mark_number(number, board, marker_board):
    for row_idx in range(len(board)):
        for col_idx in range(len(board[row_idx])):
            if board[row_idx][col_idx] == number:
                marker_board[row_idx][col_idx] = True

    return board, marker_board


def transpose(board):
    return list(map(list, zip(*board)))


def print_board(board, marker_board):
    for row_idx in range(len(board)):
        print([col if not marked else -col for col, marked in zip(board[row_idx], marker_board[row_idx])])
    print()


def is_winner(marker_board):
    for row in marker_board:
        if all(row):
            return True
    for col in transpose(marker_board):
        if all(col):
            return True
    return False


def count_board(board, marker_board, marker=False):
    total = 0

    for row, marker_row in zip(board, marker_board):
        total += sum(col for col, marked in zip(row, marker_row) if marked == marker)

    return total


def main():
    lines = get_lines()

    numbers, boards = read_input(lines)
    marker_boards = [generate_marker_board() for _ in range(len(boards))]

    winning_log = []

    for number in numbers:
        for board, marker_board in zip(boards, marker_boards):
            if is_winner(marker_board):
                continue
            mark_number(number, board, marker_board)
            if is_winner(marker_board):
                total = count_board(board, marker_board)
                winning_log.append(total * number)

    print(winning_log[-1])


if __name__ == "__main__":
    main()
