from src.common.common import get_lines


def read_input(lines):
    reading_folds = False

    dots = set()
    folds = []

    for line in lines:
        if len(line) == 0:
            reading_folds = True
            continue

        if reading_folds:
            _, fold = line.split('fold along ')
            direction, coordinate = fold.split('=')
            coordinate = int(coordinate)
            folds.append((direction, coordinate))
        else:
            x, y = line.split(',')
            x, y = int(x), int(y)
            dots.add((x, y))

    return dots, folds


def fold_matrix(dots, fold):
    fold_direction, fold_coordinate = fold

    dots_to_remove = set()
    dots_to_add = set()

    if fold_direction == 'x':
        for x, y in dots:
            if x > fold_coordinate:
                to_fold = x - fold_coordinate
                opposite = x - (2 * to_fold), y
                if opposite not in dots:
                    dots_to_add.add(opposite)
                dots_to_remove.add((x, y))
    else:
        for x, y in dots:
            if y > fold_coordinate:
                to_fold = y - fold_coordinate
                opposite = x, y - (2 * to_fold)
                if opposite not in dots:
                    dots_to_add.add(opposite)
                dots_to_remove.add((x, y))

    dots.difference_update(dots_to_remove)
    dots.update(dots_to_add)

    return dots


def print_dots(dots):
    max_x = max(x for x, y in dots)
    max_y = max(y for x, y in dots)

    matrix = [[0 for x in range(max_x + 1)] for y in range(max_y + 1)]

    for x, y in dots:
        matrix[y][x] += 1

    for row in matrix:
        print(''.join('.' if col == 0 else '#' for col in row))

    print()

def main():
    lines = get_lines()

    dots, folds = read_input(lines)

    for fold in folds:
        dots = fold_matrix(dots, fold)

    print_dots(dots)


if __name__ == "__main__":
    main()
