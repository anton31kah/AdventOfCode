from src.common.common import get_lines


def main():
    lines = get_lines('S')

    numbers = [int(line) for line in lines]
    indexes = {idx: idx for idx, num in enumerate(numbers)}

    for idx in sorted(indexes.keys()):
        position = indexes[idx]
        number = numbers[position]
        new_position = (position + number) % len(numbers)

        if new_position < position:
            numbers.pop(position)
            numbers.insert(new_position, number)
            for i in range(new_position + 1, position + 1):
                # pos[i] = pos[i] - 1
                # need two way map
                ...
        elif new_position > position:
            numbers.insert(new_position, number)
            numbers.pop(position)
            for i in range(position, new_position):
                # pos[i] = pos[i] - 1
                ...

    # print(numbers[1000 % len(numbers)] + numbers[2000 % len(numbers)] + numbers[3000 % len(numbers)])


if __name__ == "__main__":
    main()
