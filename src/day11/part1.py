from src.common.common import get_lines


def safe_list_get(l, idx, default):
    if idx in range(len(l)):
        return l[idx]
    else:
        return default


def is_seat_occupied(graph, row, col):
    line = safe_list_get(graph, row, [])
    seat = safe_list_get(line, col, '.')
    return seat == '#'


def count_occupied_around_seat(row, col, seat, graph):
    occupied = 0

    occupied += int(is_seat_occupied(graph, row - 1, col - 1))
    occupied += int(is_seat_occupied(graph, row - 1, col))
    occupied += int(is_seat_occupied(graph, row - 1, col + 1))

    occupied += int(is_seat_occupied(graph, row, col - 1))
    occupied += int(is_seat_occupied(graph, row, col + 1))

    occupied += int(is_seat_occupied(graph, row + 1, col - 1))
    occupied += int(is_seat_occupied(graph, row + 1, col))
    occupied += int(is_seat_occupied(graph, row + 1, col + 1))

    return occupied


def apply_rules_on_seat(row, col, seat, graph):
    occupied = count_occupied_around_seat(row, col, seat, graph)

    if seat == 'L' and occupied == 0:
        return '#'

    if seat == '#' and occupied >= 4:
        return 'L'

    return seat


def apply_rules(graph):
    copy = []

    for row, line in enumerate(graph):
        new_line = []
        for col, seat in enumerate(line):
            new_seat = apply_rules_on_seat(row, col, seat, graph)
            new_line.append(new_seat)
        copy.append(new_line)

    return copy


def count_occupied(graph):
    occupied = 0
    for line in graph:
        for seat in line:
            occupied += int(seat == '#')
    return occupied


def print_graph(round, graph):
    header = f"=== ROUND #{round} ==="
    print('=' * len(header))
    print(header)
    print('=' * len(header))

    for line in graph:
        if isinstance(line, str):
            print(line)
        elif isinstance(line, list):
            print(''.join(line))
        else:
            print(line)

    print()
    print()


graph = get_lines()

# graph = [
#     'L.LL.LL.LL',
#     'LLLLLLL.LL',
#     'L.L.L..L..',
#     'LLLL.LL.LL',
#     'L.LL.LL.LL',
#     'L.LLLLL.LL',
#     '..L.L.....',
#     'LLLLLLLLLL',
#     'L.LLLLLL.L',
#     'L.LLLLL.LL',
# ]

graph = list(map(list, graph))

# print_graph(0, graph)

# for round in range(1, 10):
#     graph = apply_rules(graph)
#     print_graph(round, graph)

while True:
    new_graph = apply_rules(graph)
    if graph == new_graph:
        print(count_occupied(graph))
        break
    graph = new_graph
