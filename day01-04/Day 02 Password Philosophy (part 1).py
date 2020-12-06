import re


def extract(line):
    min_occ, max_occ, char, password = re.findall(r"\w+", line)
    return ((char, int(min_occ), int(max_occ)), password)


with open('Day 02 Password Philosophy.in.txt') as f:
    policies_passwords = list(map(lambda l: extract(l.strip()), f.readlines()))
    count_valid = 0

    for ((char, min_occ, max_occ), password) in policies_passwords:
        if min_occ <= password.count(char) <= max_occ:
            count_valid += 1
    
    print(count_valid)
