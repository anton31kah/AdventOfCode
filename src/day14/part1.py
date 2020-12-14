import re
from src.common.common import get_lines


def parse_command(line: str):
    if line.startswith('mem'):
        r = re.search(r'mem\[(\d+)\] = (\d+)', line)
        return ('mem', (r.group(1), int(r.group(2))))
    elif line.startswith('mask'):
        _, mask = line.split(' = ')
        return ('mask', mask)


def apply_mask(mask, value):
    binary = bin(value)[2:].rjust(36, '0')
    new_binary = ''.join([(num_bit if mask_bit == 'X' else mask_bit) for mask_bit, num_bit in zip(mask, binary)])
    return int(new_binary, base=2)


lines = get_lines()
commands = list(map(parse_command, lines))

mask = None
memory = {}

for op, args in commands:
    if op == 'mem':
        address, value = args
        memory[address] = apply_mask(mask, value)
    elif op == 'mask':
        mask = args

print(sum(memory.values()))
