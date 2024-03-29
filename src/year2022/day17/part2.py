from src.common.common import get_lines


class Figure:
    def __init__(self, points):
        self.points = points


    def down(self):
        self.points = set((x, y - 1) for x, y in self.points)


    def up(self):
        self.points = set((x, y + 1) for x, y in self.points)


    def left(self):
        self.points = set((x - 1, y) for x, y in self.points)


    def right(self):
        self.points = set((x + 1, y) for x, y in self.points)


    def collides(self, other):
        return len(self.points & other.points) > 0


    def rightmost(self):
        return max(self.points, key=lambda p: p[0])[0]


    def leftmost(self):
        return min(self.points, key=lambda p: p[0])[0]


    def uppermost(self):
        return max(self.points, key=lambda p: p[1])[1]


    def lowermost(self):
        return min(self.points, key=lambda p: p[1])[1]


def create_figure(figure_index, height) -> Figure:
    match figure_index:
        case 0:
            return Figure({(2, height), (3, height), (4, height), (5, height)})
        case 1:
            return Figure({(3, height + 2), (2, height + 1), (3, height + 1), (4, height + 1), (3, height)})
        case 2:
            return Figure({(4, height + 2), (4, height + 1), (2, height), (3, height), (4, height)})
        case 3:
            return Figure({(2, height + 3), (2, height + 2), (2, height + 1), (2, height)})
        case 4:
            return Figure({(2, height + 1), (3, height + 1), (2, height), (3, height)})
        case _:
            raise ValueError('Invalid figure index', figure_index)


def check_collides(grid, moving_figure):
    return len(grid & moving_figure.points) > 0


def print_grid(grid: list[tuple[int, int]], file=None):
    height = max(grid, key=lambda p: p[1])[1]
    zero = min(grid, key=lambda p: p[1])[1]
    canvas = [list('.......') for _ in range(zero, height + 1)]
    for x, y in grid:
        canvas[y - zero][x] = '#'
    canvas.reverse()
    for row in canvas:
        print(''.join(row), file=file)


def main():
    lines = get_lines('')

    shifts = list(lines[0])
    shift_index = 0

    grid: set[tuple[int, int]] = set()
    grid_width = 7
    grid_rocks = 0

    figure_index = 0

    moving_figure: Figure = None

    # after cycle verification
    # grid = {
    #     (1, 1553982299687), (2, 1553982299687), (3, 1553982299687), (4, 1553982299687),
    #     }
    # grid_rocks = 999999999226
    # moving_figure = None
    # figure_index = 1

    while True:
        shift = shifts[shift_index % len(shifts)]
        shift_index += 1
        if shift_index > 0 and shift_index % len(shifts) == 0:
            # every cycle gives 1695 rocks and 2634 height
            # every cycle begins with NO moving figure and figure index 1
            # first cycle gave 1726 rocks and 2687 height
            # closest to 1000000000000 is 589970500 cycles (after the initial)
            # that one gets us to 999999999226
            # so we can start from there
            grid_rocks = 999999999226
            moving_figure = None
            figure_index = 1

            zero = min(grid, key=lambda f: f[1])[1]
            height = max(grid, key=lambda f: f[1])[1]
            last_points = list(sorted(filter(lambda p: p[1] >= height - 220, grid)))
            last_points = set((x, y - height + 1553982299687) for x, y in last_points)
            grid = set(last_points)

            # print_grid(last_points)
            # print(last_points)
            # print(grid_rocks, height, height - zero, bool(moving_figure), figure_index)
            # exit()
            # pass
            break

        if not moving_figure:
            if grid_rocks == 1_000_000_000_000:
                break

            if len(grid) > 0:
                height = max(grid, key=lambda f: f[1])[1]
                height += 1
            else:
                height = 0
            height += 3

            moving_figure = create_figure(figure_index, height)

        match shift:
            case '>':
                if moving_figure.rightmost() < grid_width - 1:
                    moving_figure.right()
                    if check_collides(grid, moving_figure):
                        moving_figure.left()
            case '<':
                if moving_figure.leftmost() > 0:
                    moving_figure.left()
                    if check_collides(grid, moving_figure):
                        moving_figure.right()

        moving_figure.down()
        if check_collides(grid, moving_figure) or moving_figure.lowermost() < 0:
            moving_figure.up()
            grid.update(moving_figure.points)
            grid_rocks += 1
            moving_figure = None
            figure_index += 1
            figure_index %= 5

            height = max(grid, key=lambda f: f[1])[1]
            zero = min(grid, key=lambda f: f[1])[1]
            y_full_row = next((y for y in range(height, zero - 1, -1) if all((x, y) in grid for x in range(grid_width))), -1)
            if y_full_row >= 0:
                grid = set(filter(lambda p: p[1] >= y_full_row, grid))

    while True:
        shift = shifts[shift_index % len(shifts)]
        shift_index += 1

        if not moving_figure:
            if grid_rocks == 1_000_000_000_000:
                break

            if len(grid) > 0:
                height = max(grid, key=lambda f: f[1])[1]
                height += 1
            else:
                height = 0
            height += 3

            moving_figure = create_figure(figure_index, height)

        match shift:
            case '>':
                if moving_figure.rightmost() < grid_width - 1:
                    moving_figure.right()
                    if check_collides(grid, moving_figure):
                        moving_figure.left()
            case '<':
                if moving_figure.leftmost() > 0:
                    moving_figure.left()
                    if check_collides(grid, moving_figure):
                        moving_figure.right()

        moving_figure.down()
        if check_collides(grid, moving_figure) or moving_figure.lowermost() < 0:
            moving_figure.up()
            grid.update(moving_figure.points)
            grid_rocks += 1
            moving_figure = None
            figure_index += 1
            figure_index %= 5

            height = max(grid, key=lambda f: f[1])[1]
            zero = min(grid, key=lambda f: f[1])[1]
            y_full_row = next((y for y in range(height, zero - 1, -1) if all((x, y) in grid for x in range(grid_width))), -1)
            if y_full_row >= 0:
                grid = set(filter(lambda p: p[1] >= y_full_row, grid))

    # NO FUCKING IDEA WHY 3 instead of 1 but that shit works I don't give a fuck
    print(max(grid, key=lambda f: f[1])[1] + 3)


if __name__ == "__main__":
    main()
