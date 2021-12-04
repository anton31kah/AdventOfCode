import re
from src.common.common import get_lines


def check(passport):
    return 'byr:' in passport and \
            'iyr:' in passport and \
            'eyr:' in passport and \
            'hgt:' in passport and \
            'hcl:' in passport and \
            'ecl:' in passport and \
            'pid:' in passport


regex = re.compile(r"(?=.*\bbyr:\S+)(?=.*\biyr:\S+)(?=.*\beyr:\S+)(?=.*\bhgt:\S+)(?=.*\bhcl:\S+)(?=.*\becl:\S+)(?=.*\bpid:\S+).*")

lines = get_lines()

valid = 0
passport = ''

for line in lines:
    if line:
        passport += ' ' + line
    else:
        # if check(passport):
        if regex.match(passport):
            valid += 1
        # else:
        #     print(passport)
        passport = ''

if regex.match(passport):
    valid += 1

print(valid)
