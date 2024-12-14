from src.common.common import get_lines
import math
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
                prize = val[0] + 10000000000000, val[1] + 10000000000000
                machines.append(Machine(a, b, prize))
    
    return machines


def calculate_min_tokens(machine: Machine, max_presses):
    min_tokens = float('inf')

    ax, ay = machine.a
    bx, by = machine.b
    prizex, prizey = machine.prize

    for a_presses in range(max_presses):
        # (8400 - 94 * 80) / 22 == (5400 - 34 * 80) / 67
        # (przX - aX * aP) / bX == (przY - aY * aP) / bY
        if a_presses % 10_000_000 == 0:
            print(machine, a_presses)
        b_presses_x = (prizex - ax * a_presses) / bx
        b_presses_y = (prizey - ay * a_presses) / by
        if b_presses_x == b_presses_y:
            min_tokens = min(min_tokens, a_presses * 3 + b_presses_x)
    
    return min_tokens


def main():
    lines = get_lines('')

    machines = parse_input(lines)

    max_presses = 0

    for machine in machines:
        max_presses = max(max_presses, math.ceil(machine.prize[0] / machine.a[0]))
        max_presses = max(max_presses, math.ceil(machine.prize[1] / machine.a[1]))
        max_presses = max(max_presses, math.ceil(machine.prize[0] / machine.b[0]))
        max_presses = max(max_presses, math.ceil(machine.prize[1] / machine.b[1]))
    
    for machine in machines:
        min_tokens = calculate_min_tokens(machine, max_presses)
        if min_tokens != float('inf'):
            total += min_tokens
        print(machine, min_tokens)
    
    print(total)


if __name__ == "__main__":
    main()
