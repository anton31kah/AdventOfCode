from collections import Counter
from src.common.common import get_lines


def read_input(lines):
    template = lines[0]

    pairs = []

    for line in lines[2:]:
        pairs.append(line.split(' -> '))

    return template, dict(pairs)


def main():
    lines = get_lines()

    template, pairs = read_input(lines)

    for step in range(10):
        new_template = []
        for idx in range(1, len(template)):
            s1, s2 = template[idx - 1], template[idx]
            window = s1 + s2
            if len(new_template) == 0:
                new_template.append(s1)
            new_template.append(f'{pairs[window]}{s2}')
        template = ''.join(new_template)

    counter = Counter(template)
    common = counter.most_common()
    most_common, least_common = common[0], common[-1]
    print(most_common[1] - least_common[1])


if __name__ == "__main__":
    main()
