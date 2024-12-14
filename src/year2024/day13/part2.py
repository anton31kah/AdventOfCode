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
    
    def __format__(self, format_spec):
        match format_spec:
            case 'simple':
                return f"A {self.a} * B {self.b} = Prize {self.prize}"
            case 'math':
                return f"{self.a[0]}x + {self.b[0]}y = {self.prize[0]}, {self.a[1]}x + {self.b[1]}y = {self.prize[1]}"
        raise ValueError(f"Invalid format spec for Machine '{format_spec}', only math & simple are allowed!")

    def __str__(self):
        return format(self, 'simple')
    
    def __repr__(self):
        return str(self)


def parse_input(lines: list[str]):
    machines: list[Machine] = []

    prize_add = 10000000000000
    # prize_add = 0

    for line_num, line in enumerate(lines):
        val = tuple(map(int, re.findall(r'\d+', line)))
        match line_num % 4:
            case 0: # button A
                a = val
            case 1: # button B
                b = val
            case 2: # prize
                prize = val[0] + prize_add, val[1] + prize_add
                machines.append(Machine(a, b, prize))
    
    return machines


def solve_machine(machine: Machine):
    """

    https://www.cuemath.com/geometry/intersection-of-two-lines/

    Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400
    94x + 22y = 8400, 34x + 67y = 5400
    a1 = 94
    b1 = 22
    c1 = -8400
    a2 = 34
    b2 = 67
    c2 = -5400
    (x, y) = ((b1c2-b2c1)/(a1b2-a2b1), (c1a2-c2a1)/(a1b2-a2b1))

    Button A: X+26, Y+66
    Button B: X+67, Y+21
    Prize: X=12748, Y=12176
    26x + 67y = 12748, 66x + 21y = 12176

    Button A: X+17, Y+86
    Button B: X+84, Y+37
    Prize: X=7870, Y=6450
    17x + 84y = 7870, 86x + 37y = 6450

    Button A: X+69, Y+23
    Button B: X+27, Y+71
    Prize: X=18641, Y=10279
    69x + 27y = 18641, 23x + 71y = 10279

    """
    a1, a2 = machine.a
    b1, b2 = machine.b
    c1, c2 = machine.prize
    c1, c2 = -c1, -c2
    x, y = (b1*c2-b2*c1)/(a1*b2-a2*b1), (c1*a2-c2*a1)/(a1*b2-a2*b1)
    if x.is_integer() and y.is_integer():
        return x, y
    return None


def main():
    lines = get_lines('')

    machines = parse_input(lines)

    total = 0

    for machine in machines:
        answer = solve_machine(machine)
        if answer is not None:
            x, y = answer
            total += x * 3 + y
            print(machine, answer)

    print(total)


if __name__ == "__main__":
    main()
