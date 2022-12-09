from src.common.common import get_lines


def touching(head, tail):
    diff_x = head[0] - tail[0]
    diff_y = head[1] - tail[1]
    return abs(diff_x) <= 1 and abs(diff_y) <= 1


def calc_move(head, tail):
    diff_x = head[0] - tail[0]
    diff_y = head[1] - tail[1]

    move_x = 0
    move_y = 0

    if diff_x > 0:
        move_x = +1

    if diff_x < 0:
        move_x = -1

    if diff_y > 0:
        move_y = +1

    if diff_y < 0:
        move_y = -1

    return move_x, move_y


def main():
    lines = get_lines('')

    visited = {(0, 0)}

    head = (0, 0)
    tail = (0, 0)

    for line in lines:
        direction, steps = line.split(' ')
        steps = int(steps)

        # print(f"{direction},{steps}")

        for i in range(steps):
            if direction == 'U':
                head = head[0], head[1] + 1
            elif direction == 'D':
                head = head[0], head[1] - 1
            elif direction == 'L':
                head = head[0] - 1, head[1]
            elif direction == 'R':
                head = head[0] + 1, head[1]

            # print(f"  {i + 1}: H:{head}, T:{tail}")

            while not touching(head, tail):
                move_tail_x, move_tail_y = calc_move(head, tail)
                tail = tail[0] + move_tail_x, tail[1] + move_tail_y
                visited.add(tail)

            # print(f"   {i + 1}: H:{head}, T:{tail}")

    print(len(visited))


if __name__ == "__main__":
    main()
