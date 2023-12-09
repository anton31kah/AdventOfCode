from src.common.common import get_lines


def get_next_sequence(sequence):
    return [v2 - v1 for v1, v2 in zip(sequence, sequence[1:])]


def predicate_value(sequence):
    sequences = [sequence]
    while not all(x == 0 for x in sequences[-1]):
        sequences.append(get_next_sequence(sequences[-1]))

    sequences[-1].append(0)
    for seq_idx in range(len(sequences) - 2, -1, -1):
        sequences[seq_idx].append(sequences[seq_idx + 1][-1] + sequences[seq_idx][-1])

    return sequences[0][-1]


def main():
    lines = get_lines('')

    total = 0

    for line in lines:
        sequence = [int(x) for x in line.split()]
        total += predicate_value(sequence)
    
    print(total)


if __name__ == "__main__":
    main()
