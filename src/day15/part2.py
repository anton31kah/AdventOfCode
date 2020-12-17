from src.common.common import get_lines


def limit(array, elements_count):
    while len(array) > 2:
        array.pop(0)


lines = get_lines()
numbers = list(map(int, lines[0].split(',')))

last_spoken_times = {}

for r, num in enumerate(numbers, 1):
    last_spoken_times[num] = [r]

last_number = numbers[-1]

for r in range(len(numbers) + 1, 30000000 + 1):
    new_number = None

    if last_number in last_spoken_times:
        times = last_spoken_times[last_number]

        if len(times) == 1:
            new_number = 0
        elif len(times) == 2:
            new_number = times[1] - times[0]

    else:
        new_number = 0

    numbers.append(new_number)
    spoken_times = last_spoken_times.setdefault(new_number, [])
    spoken_times.append(r)
    limit(spoken_times, 2)

    last_number = numbers[-1]

print(numbers[-1])
