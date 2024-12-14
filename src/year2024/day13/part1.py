from src.common.common import get_lines
import re


class Machine:
    def __init__(self, a: tuple[int, int], b: tuple[int, int], prize: tuple[int, int]):
        self.a = a
        self.b = b
        self.prize = prize
    
    def __key(self):
        return (self.a, self.b, self.prize)
    
    def __eq__(self, other):
        if isinstance(other, Machine):
            return self.__key() == other.__key()
        return NotImplemented
    
    def __hash__(self):
        return hash(self.__key())
    
    def __str__(self):
        return f"A {self.a} * B {self.b} = Prize {self.prize}"
    
    def __repr__(self):
        return str(self)


def parse_input(lines: list[str]):
    machines: list[Machine] = []

    for line_num, line in enumerate(lines):
        val = tuple(map(int, re.findall(r'\d+', line)))
        match line_num % 4:
            case 0: # button A
                a = val
            case 1: # button B
                b = val
            case 2: # prize
                machines.append(Machine(a, b, val))
    
    return machines


def calculate_min_tokens(machine: Machine):
    min_tokens = float('inf')

    ax, ay = machine.a
    bx, by = machine.b
    prizex, prizey = machine.prize

    for a_presses in range(101):
        for b_presses in range(101):
            if a_presses * ax + b_presses * bx == prizex and a_presses * ay + b_presses * by == prizey:
                min_tokens = min(min_tokens, a_presses * 3 + b_presses)
    
    return min_tokens


def main():
    lines = get_lines('')

    machines = parse_input(lines)

    total = 0

    for machine in machines:
        min_tokens = calculate_min_tokens(machine)
        if min_tokens != float('inf'):
            total += min_tokens
        # print(machine, min_tokens)
    
    print(total)


if __name__ == "__main__":
    main()
