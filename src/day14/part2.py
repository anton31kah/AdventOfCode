import re
from src.common.common import get_lines


def parse_command(line: str):
    if line.startswith('mem'):
        r = re.search(r'mem\[(\d+)\] = (\d+)', line)
        return ('mem', (int(r.group(1)), int(r.group(2))))
    elif line.startswith('mask'):
        _, mask = line.split(' = ')
        return ('mask', mask)


def apply_mask_bit(mask_bit, value_bit):
    if mask_bit == '0':
        return value_bit
    elif mask_bit == '1':
        return '1'
    else:
        return 'X'


def to_bin(num, length):
    return bin(num)[2:].rjust(length, '0')


def replace(string1, char, string2):
    chars = list(string1)
    new_chars = []
    i = 0
    for c in chars:
        if c == char:
            new_chars.append(string2[i])
            i += 1
        else:
            new_chars.append(c)
    return ''.join(new_chars)


def apply_mask(mask, value):
    binary = to_bin(value, 36)
    new_binary = ''.join([apply_mask_bit(mask_bit, num_bit) for mask_bit, num_bit in zip(mask, binary)])
    Xs = new_binary.count('X')
    count = 2 ** Xs
    result = []
    for i in range(count):
        i_bin = to_bin(i, Xs)
        result.append(replace(new_binary, 'X', i_bin))
    return result


lines = get_lines()

commands = list(map(parse_command, lines))

mask = None
memory = {}

for op, args in commands:
    if op == 'mem':
        address, value = args
        addresses = apply_mask(mask, address)
        for address in addresses:
            memory[address] = value
    elif op == 'mask':
        mask = args

print(sum(memory.values()))
