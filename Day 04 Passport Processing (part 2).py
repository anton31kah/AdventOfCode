import re
from common import get_lines


regex = re.compile(r"(?=.*\bbyr:\d{4}\b)(?=.*\biyr:\d{4}\b)(?=.*\beyr:\d{4}\b)(?=.*\bhgt:\d+(cm|in)\b)(?=.*\bhcl:#[0-9a-fA-F]{6}\b)(?=.*\becl:(amb|blu|brn|gry|grn|hzl|oth)\b)(?=.*\bpid:\d{9}\b).*")


def check_fields(passport):
    byr = re.search(r"byr:(\d{4})\b", passport).group(1)
    iyr = re.search(r"iyr:(\d{4})\b", passport).group(1)
    eyr = re.search(r"eyr:(\d{4})\b", passport).group(1)
    hgt = re.search(r"hgt:(\d+)(cm|in)\b", passport).group(1)
    incm = re.search(r"hgt:(\d+)(cm|in)\b", passport).group(2)
    
    byr, iyr, eyr, hgt = int(byr), int(iyr), int(eyr), int(hgt)
    
    return 1920 <= byr <= 2002 and \
            2010 <= iyr <= 2020 and \
            2020 <= eyr <= 2030 and \
            (150 <= hgt <= 193 if incm == 'cm' else 59 <= hgt <= 76)


def check(passport):
    return regex.match(passport) and check_fields(passport)


lines = get_lines()

valid = 0
passport = ''

for line in lines:
    if line:
        passport += ' ' + line
    else:
        if check(passport):
            valid += 1
        passport = ''

if check(passport):
    valid += 1

print(valid)
