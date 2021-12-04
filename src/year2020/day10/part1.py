from src.common.common import get_lines


lines = get_lines()

adapters = sorted(map(int, lines))

differences = {
    1: 0,
    2: 0,
    3: 1 # device difference
}

current_adapter = 0

for adapter in adapters:
    diff = adapter - current_adapter
    differences[diff] += 1
    current_adapter = adapter

print(differences, 'result =', differences[1] * differences[3])
