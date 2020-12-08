from src.common.common import get_lines
import re


def extract(line):
    min_occ, max_occ, char, password = re.findall(r"\w+", line)
    return ((char, int(min_occ), int(max_occ)), password)


policies_passwords = list(map(extract, get_lines()))
count_valid = 0

for ((char, min_occ, max_occ), password) in policies_passwords:
    if min_occ <= password.count(char) <= max_occ:
        count_valid += 1

print(count_valid)
