from src.common.common import get_lines


class NumberContext:
    def __init__(self):
        self.value = 0
        self.positions = []
        self.surrounding_positions = set()
    
    def add_digit(self, digit, position):
        self.value *= 10
        self.value += digit
        
        self.positions.append(position)

        x, y = position
        self.surrounding_positions.add((x - 1, y - 1))
        self.surrounding_positions.add((x - 1, y))
        self.surrounding_positions.add((x - 1, y + 1))
        self.surrounding_positions.add((x, y - 1))
        self.surrounding_positions.add((x, y))
        self.surrounding_positions.add((x, y + 1))
        self.surrounding_positions.add((x + 1, y - 1))
        self.surrounding_positions.add((x + 1, y))
        self.surrounding_positions.add((x + 1, y + 1))
    
    def __str__(self):
        return str({
            'value': self.value,
            'positions': self.positions,
            'surrounding_positions': self.surrounding_positions,
        })
    
    def __repr__(self):
        return str(self)


def product(items):
    res = 1
    for x in items:
        res *= x
    return res


def main():
    lines = get_lines('')

    numbers = set() # contexts
    symbols = {} # positions

    currentNumber = NumberContext()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == '.':
                currentNumber = NumberContext()
            elif c.isdigit():
                currentNumber.add_digit(int(c), (x, y))
                numbers.add(currentNumber)
            else:
                currentNumber = NumberContext()
                if c not in symbols:
                    symbols[c] = set()
                symbols[c].add((x, y))
        currentNumber = NumberContext()
    currentNumber = NumberContext()

    gears_numbers = {} # symbol_pos -> [number.value]

    for number in numbers:
        for symbol in symbols['*']:
            if symbol in number.surrounding_positions:
                if symbol not in gears_numbers:
                    gears_numbers[symbol] = []
                gears_numbers[symbol].append(number.value)
                break

    total = 0

    for values in gears_numbers.values():
        if len(values) > 1:
            # print(values)
            total += product(values)

    print(total)


if __name__ == "__main__":
    main()
