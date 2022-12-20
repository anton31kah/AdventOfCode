from src.common.common import get_lines


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.is_head = False

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


def to_linkedlist_array(array):
    result = [LinkedListNode(val) for val in array]

    for i in range(len(result) - 1):
        result[i].next = result[i + 1]
        result[i - 1].prev = result[i]

    result[-1].next = result[0]
    result[0].prev = result[-1]

    result[0].is_head = True

    return result


def main():
    lines = get_lines('')

    numbers = [int(line) * 811589153 for line in lines]
    numbers = to_linkedlist_array(numbers)

    current = numbers[0]

    hit_head_times = 0

    while True:
        if current.is_head and hit_head_times >= 10:
            break

        if current.is_head:
            hit_head_times += 1

        position = numbers.index(current)

        new_position = (position + current.value) % (len(numbers) - 1)

        numbers.insert(new_position, numbers.pop(position))

        # print(current, ';', numbers, ';', {new_position < position:'<', new_position > position: '>'}.get(True, ''))

        current = current.next

    # print(numbers)

    positions = [1000, 2000, 3000]

    for idx, node in enumerate(numbers):
        if node.value == 0:
            positions = [p + idx for p in positions]

    result = [numbers[p % len(numbers)].value for p in positions]

    # print(list(zip(positions, result)))

    result = sum(result)

    print(result)


if __name__ == "__main__":
    main()
