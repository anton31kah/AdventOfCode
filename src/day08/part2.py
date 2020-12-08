from src.common.common import get_lines


def parse_instruction(instruction):
    command, arg = instruction.split(' ')
    return command, int(arg)


def switch_command(command):
    if command == 'acc':
        return command
    elif command == 'jmp':
        return 'nop'
    elif command == 'nop':
        return 'jmp'


def switch_at(code, index):
    new_code = code[:]
    old_command, arg = code[index]
    new_code[index] = switch_command(old_command), arg
    return new_code


code = get_lines()
code = list(map(parse_instruction, code))

possible_changes = [i for i in range(len(code)) if code[i][0] in ('jmp', 'nop')]

for change in possible_changes:
    modified_code = switch_at(code, change)

    acc_register = 0
    instruction_pointer = 0

    executed_instruction_pointers = []

    did_terminate = False

    while True:
        if instruction_pointer >= len(modified_code):
            did_terminate = True
            break

        instruction, arg = modified_code[instruction_pointer]

        if instruction_pointer in executed_instruction_pointers:
            did_terminate = False
            break

        executed_instruction_pointers.append(instruction_pointer)

        if instruction == 'acc':
            acc_register += arg
            instruction_pointer += 1
        elif instruction == 'jmp':
            instruction_pointer += arg
        elif instruction == 'nop':
            instruction_pointer += 1

    if did_terminate:
        print(acc_register)
