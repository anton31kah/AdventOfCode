import re
from src.common.common import get_lines


class Monkey:
    def __init__(self, id, items, operation, test, when_true, when_false):
        self.id = id
        self.items = items
        self.__operation = operation
        self.__test = test
        self.__when_true = when_true
        self.__when_false = when_false


    def calculate_worry(self, old):
        new = eval(self.__operation)
        new //= 3
        return new


    def which_monkey_next(self, worry):
        if worry % self.__test == 0:
            return self.__when_true
        else:
            return self.__when_false


def parse_monkey(lines):
    regex = (r"Monkey (\d+):\n"
             r"  Starting items: ((\d+(, )?)+)\n"
             r"  Operation: new = (old [*+] \w+)\n"
             r"  Test: divisible by (\d+)\n"
             r"    If true: throw to monkey (\d+)\n"
             r"    If false: throw to monkey (\d+)")
    result = re.findall(regex, '\n'.join(lines), re.MULTILINE)[0]

    id = int(result[0])
    items = list(map(int, result[1].split(',')))
    operation = result[4]
    test = int(result[5])
    when_true = int(result[6])
    when_false = int(result[7])

    return Monkey(id, items, operation, test, when_true, when_false)


def group_lines_per_monkey(lines):
    per_monkey = [[]]

    current_index = 0

    for line in lines:
        if len(line) == 0:
            current_index += 1
            per_monkey.append([])
            continue
        per_monkey[current_index].append(line)

    return per_monkey


def main():
    lines = get_lines('')

    monkeys = [parse_monkey(monkey_lines) for monkey_lines in group_lines_per_monkey(lines)]
    monkeys_map = {monkey.id: monkey for monkey in monkeys}

    inspection_times = {}

    for i in range(20):
        for monkey in monkeys:
            for worry in monkey.items:
                new_worry = monkey.calculate_worry(worry)
                next_monkey_id = monkey.which_monkey_next(new_worry)
                monkeys_map[next_monkey_id].items.append(new_worry)

                if monkey.id not in inspection_times:
                    inspection_times[monkey.id] = 0
                inspection_times[monkey.id] += 1
            monkey.items = []

    top1, top2 = sorted(inspection_times.values())[-2:]
    print(top1 * top2)


if __name__ == "__main__":
    main()
