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
    seeds = list(zip(seeds[::2], seeds[1::2]))
    seeds = [(seed_start, seed_start + seed_length) for seed_start, seed_length in seeds]

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

    return seeds, conversions # list[range], dict[key, list[range]] # range=tuple[int, int]


def range_intersect(r1, r2):
    if type(r1) is tuple:
        r1 = range(r1[0], r1[1])
    if type(r2) is tuple:
        r2 = range(r2[0], r2[1])
    return range(max(r1.start,r2.start), min(r1.stop,r2.stop)) or None


def range_union(r1, r2):
    inclusive_end = False
    if type(r1) is tuple:
        r1 = range(r1[0], r1[1])
    if type(r2) is tuple:
        r2 = range(r2[0], r2[1])
    if range_intersect(r1, r2):
        return range(min(r1.start,r2.start), max(r1.stop,r2.stop)) or None
    if r1.start <= r2.start:
        if r1.stop == r2.start or ((r1.stop + 1) == r2.start and inclusive_end):
            return range(r1.start, r2.stop)
    if r2.start <= r1.start:
        if r2.stop == r1.start or ((r2.stop + 1) == r1.start and inclusive_end):
            return range(r2.start, r1.stop)
    return None


def main():
    seeds, conversions = read_input('')
    seeds_ranges = seeds[:]

    print(seeds_ranges)

    for conv in CONVERSIONS:
        conversion_ranges = conversions[conv]

        new_ranges = []
        
        for seed_start, seed_end in seeds_ranges:
            covered_ranges = []
            range_to_cover = (seed_start, seed_end)
            for (source_start, source_end), (dest_start, dest_end) in conversion_ranges:
                intersection = range_intersect((source_start, source_end), range_to_cover)
                if intersection:
                    intersection_start = intersection.start
                    intersection_end = intersection.stop
                    start_diff = source_start - intersection_start
                    end_diff = source_end - intersection_end
                    new_ranges.append((dest_start - start_diff, dest_end - end_diff))
                    covered_ranges.append((source_start - start_diff, source_end - end_diff))
            left_to_cover = []
            # find left to cover
            # currently range_to_cover [..........................................................]
            # currently covered_ranges      [.....]        [.......]             [............]
            # need to find uncovered = [....]     [........]       [.............]            [...]
            # print('covered_ranges', covered_ranges, 'for', range_to_cover)

        seeds_ranges = new_ranges
        print(seeds_ranges)

    print(seeds_ranges)
    print(min(start for start, end in seeds_ranges))


if __name__ == "__main__":
    main()
