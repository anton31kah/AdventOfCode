from src.common.common import get_lines
import re


CONVERSIONS = [
    'seed-to-soil',
    'soil-to-fertilizer',
    'fertilizer-to-water',
    'water-to-light',
    'light-to-temperature',
    'temperature-to-humidity',
    'humidity-to-location',
]


def read_input(suffix):
    lines = get_lines(suffix)

    seeds = [int(x) for x in re.findall(r'\d+', lines[0])]

    conversions = {}

    currentlyReading = None

    for line in lines[1:]:
        if not line:
            currentlyReading = None
            continue
        if line[0].isdigit():
            numbers = [int(x) for x in re.findall(r'\d+', line)]
            destination_start, source_start, range_length = numbers
            conversions[currentlyReading].append((
                (source_start, source_start + range_length),
                (destination_start, destination_start + range_length)
            ))
        else:
            currentlyReading = line.split()[0]
            if currentlyReading not in CONVERSIONS:
                raise ValueError("Found invalid conversion " + currentlyReading)
            if currentlyReading in conversions:
                raise ValueError("Already read conversion " + currentlyReading)
            conversions[currentlyReading] = []

    return seeds, conversions # list[int], dict[key, list[range[int]]]


def main():
    seeds, conversions = read_input('')
    results = seeds[:]

    for conv in CONVERSIONS:
        for seed_idx, seed in enumerate(results):
            ranges = conversions[conv]
            for (source_start, source_end), (dest_start, dest_end) in ranges:
                if seed in range(source_start, source_end):
                    results[seed_idx] = seed - source_start + dest_start
                    break

    print(min(results))


if __name__ == "__main__":
    main()
