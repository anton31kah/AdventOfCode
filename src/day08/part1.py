from src.common.common import get_lines


def parse_instruction(instruction):
    command, arg = instruction.split(' ')
    return command, int(arg)


code = get_lines()

acc_register = 0
instruction_pointer = 0

executed_instruction_pointers = []

while True:
    instruction, arg = parse_instruction(code[instruction_pointer])

    if instruction_pointer in executed_instruction_pointers:
        print(acc_register)
        break

    executed_instruction_pointers.append(instruction_pointer)

    if instruction == 'acc':
        acc_register += arg
        instruction_pointer += 1
    elif instruction == 'jmp':
        instruction_pointer += arg
    elif instruction == 'nop':
        instruction_pointer += 1

