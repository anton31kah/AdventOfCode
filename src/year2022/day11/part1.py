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
        _, expression = self.__operation.split("=")
        new = eval(expression)
        new //= 3
        return new


    def which_monkey_next(self, worry):
        mod = self.__test.split()[-1]
        when_true_id = self.__when_true.split()[-1]
        when_false_id = self.__when_false.split()[-1]

        mod = int(mod)

        if worry % mod == 0:
            return when_true_id
        else:
            return when_false_id


def parse_monkey(lines):
    id = lines[0].split()[-1][:-1]

    items = lines[1].split(':')[-1]
    items = list(map(int, items.split(',')))

    operation = lines[2].split(':')[-1]
    test = lines[3].split(':')[-1]
    when_true = lines[4].split(':')[-1]
    when_false = lines[5].split(':')[-1]

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
