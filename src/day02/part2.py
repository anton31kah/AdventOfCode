from src.common.common import get_lines
import re


def extract(line):
    pos1, pos2, char, password = re.findall(r"\w+", line)
    return ((char, int(pos1), int(pos2)), password)


policies_passwords = list(map(extract, get_lines()))
count_valid = 0

for ((char, pos1, pos2), password) in policies_passwords:
    occurances = 0
    if password[pos1 - 1] == char:
        occurances += 1
    if password[pos2 - 1] == char:
        occurances += 1
    if occurances == 1:
        count_valid += 1

print(count_valid)
