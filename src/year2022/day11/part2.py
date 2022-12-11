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

        self.test_mod = self.__test


    def calculate_worry(self, old, mod):
        new = eval(self.__operation)
        new %= mod
        return new


    def which_monkey_next(self, worry):
        if worry % self.__test == 0:
            return self.__when_true
        else:
            return self.__when_false


    def __str__(self):
        return f'Monkey {self.id}: {self.items}'


    def __repr__(self):
        return f'Monkey {self.id}: {self.items}'


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
    lines = get_lines('', strip=False)

    monkeys = [parse_monkey(monkey_lines) for monkey_lines in group_lines_per_monkey(lines)]
    monkeys_map = {monkey.id: monkey for monkey in monkeys}

    # NOT MY SOLUTION
    # I assumed `(a mod c) mod n ≡ a mod n` (`n` is any of those test values, `a` is worry level).
    # I thought that it would work with modules 1000 or 1000000007.
    # But we need to use the property `(a mod kn) mod n ≡ a mod n`. So `c` must be `k × n`.
    # For `c` I used the product of the test mods, but LCM should work too, but LCM of coprimes
    #  is equal to their product, especially since they're primes here too.
    # But why does `c` need to be the product? Well first read about the Chinese Remainder Theorem.
    # When `c` is the product, it makes sure to cover the whole set of numbers that can result
    #  when testing the modulo, this way we're sure that it's unique according to the CRT.
    mod = 1
    for monkey in monkeys:
        mod *= monkey.test_mod

    inspection_times = {}

    for i in range(10000):
        # if i % 100 == 0:
        #     print('Round:', i)

        for monkey in monkeys:
            for worry in monkey.items:
                new_worry = monkey.calculate_worry(worry, mod)
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
