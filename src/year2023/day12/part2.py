from src.common.common import get_lines


def parse_line(line):
    first, second = line.split()

    groups = [int(x) for x in second.split(',')]

    first = '?'.join(([first] * 5))
    second = [i for _ in range(5) for i in second]

    hash_ranges = []
    unknown = []

    for i, c in enumerate(first):
        match c:
            case '?':
                unknown.append(i)
            case '#':
                if not hash_ranges:
                    hash_ranges.append([i, i])
                else:
                    if hash_ranges[-1][-1] + 1 == i:
                        hash_ranges[-1][-1] = i
                    else:
                        hash_ranges.append([i, i])

    return hash_ranges, unknown, groups


def all_indexes(string, search_char):
    return [idx for idx, str_char in enumerate(string) if str_char == search_char]


def copy_nested_list(arr):
    return [item[:] for item in arr]


def in_bounds(arr, idx):
    return 0 <= idx < len(arr)


def generate_options(unknown):
    value = 2 ** len(unknown) - 1
    for i in range(value + 1):
        string = format(i, f"0{len(unknown)}b") # .replace('0', '.').replace('1', '#')
        yield [unknown[j] for j in all_indexes(string, '1')]


def merge_hashes(hash_ranges, hash_positions):
    result = copy_nested_list(hash_ranges)

    if not result:
        if not hash_positions:
            return []
        else:
            result = [[hash_positions[0], hash_positions[0]]]

    current_range_index = 0

    for pos in hash_positions:
        while True:
            start, end = result[current_range_index]

            if start <= pos <= end:
                break

            if pos == end + 1:
                result[current_range_index][-1] = pos
                if in_bounds(result, current_range_index + 1) and result[current_range_index + 1][0] == pos + 1:
                    result[current_range_index][-1] = result[current_range_index + 1][-1]
                    result.pop(current_range_index + 1)
                break
            elif pos == start - 1:
                result[current_range_index][0] = pos
                if in_bounds(result, current_range_index - 1) and result[current_range_index - 1][-1] == pos - 1:
                    result[current_range_index][0] = result[current_range_index - 1][0]
                    result.pop(current_range_index - 1)
                    current_range_index -= 1
                break
            elif pos > end + 1:
                if in_bounds(result, current_range_index + 1):
                    if pos < result[current_range_index + 1][0] - 1:
                        result.insert(current_range_index + 1, [pos, pos])
                        break
                    else:
                        current_range_index += 1
                else:
                    result.append([pos, pos])
                    break
            elif pos < start - 1:
                if in_bounds(result, current_range_index - 1):
                    if pos > result[current_range_index - 1][-1] + 1:
                        result.insert(current_range_index, [pos, pos])
                        break
                    else:
                        current_range_index -= 1
                else:
                    result.insert(0, [pos, pos])
                    break

    return result


def count_options(hash_ranges, unknown, groups):
    count_valid = 0
    # print(hash_ranges)
    for option in generate_options(unknown):
        merged_hashes = merge_hashes(hash_ranges, option)
        counts = [e + 1 - s for s, e in merged_hashes]
        valid = counts == groups
        # print(f"    {'x' if valid else ' '} +{option} = {merged_hashes}")
        if valid:
            count_valid += 1
    return count_valid


def main():
    lines = get_lines('S')

    total = 0

    progress = 0

    for line in lines:
        progress += 1
        print(f"{progress/len(lines)*100}%")
        hash_ranges, unknown, groups = parse_line(line)
        total += count_options(hash_ranges, unknown, groups)
    
    print(total)


if __name__ == "__main__":
    main()
