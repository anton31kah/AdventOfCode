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


def main():
    lines = get_lines('')

    numbers = set() # contexts
    symbols = set() # positions

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
                symbols.add((x, y))
        currentNumber = NumberContext()
    currentNumber = NumberContext()

    total = 0

    for number in numbers:
        for symbol in symbols:
            if symbol in number.surrounding_positions:
                total += number.value
                break
    
    print(total)


if __name__ == "__main__":
    main()
