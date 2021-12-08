from src.common.common import get_lines

NUMBERS = {
    1: set('cf'),
    7: set('acf'),
    4: set('bcdf'),
    8: set('abcdefg'),
    2: set('acdeg'),
    3: set('acdfg'),
    5: set('abdfg'),
    0: set('abcefg'),
    6: set('abdefg'),
    9: set('abcdfg'),
}

UNIQUE_LENGTHS = {
    1: 2,
    4: 4,
    7: 3,
    8: 7
}


def find_by_number(seq, num):
    return next(filter(lambda s: len(s) == UNIQUE_LENGTHS[num], seq))


def find_by_length(seq, length):
    return list(filter(lambda s: len(s) == length, seq))


def is_same_number(num1, num2):
    return set(num1) == set(num2)


def parse_input(line):
    input, output = line.split(' | ')
    input = input.split(' ')
    output = output.split(' ')
    return input, output


"""
  1:      4:      7:      8:  
 ....    ....    aaaa    aaaa 
.    c  b    c  .    c  b    c
.    c  b    c  .    c  b    c
 ....    dddd    ....    dddd 
.    f  .    f  .    f  e    f
.    f  .    f  .    f  e    f
 ....    ....    ....    gggg 


7 - 1 -> A (char in 7 but not in 1)
8 - 4 -> E G (A is known)
4 - 1 -> B D

========================================
========================================

  2:      3:      5:  
 aaaa    aaaa    aaaa 
.    c  .    c  b    .
.    c  .    c  b    .
 dddd    dddd    dddd 
e    .  .    f  .    f
e    .  .    f  .    f
 gggg    gggg    gggg 

  0:      6:      9:
 aaaa    aaaa    aaaa
b    c  b    .  b    c
b    c  b    .  b    c
 ....    dddd    dddd
e    f  e    f  .    f
e    f  e    f  .    f
 gggg    gggg    gggg


2, 3, 5 ->
    3 is where (cf) is in it
    2 is where (eg) is in it
    5 is the other

0, 6, 9 ->
    9 is where (eg) is NOT found
    6 is where (bd) is found
    0 is the other

========================================
========================================

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

"""


def deduct_unique_segments(one, four, seven, eight):
    cf = one
    a = list(set(seven) - set(one))[0]
    bd = ''.join(list(set(four) - set(one)))
    eg = ''.join(list(set(eight) - set(four) - set(a)))
    return {
        'a': a,
        'cf': cf,
        'bd': bd,
        'eg': eg,
    }


def deduct_other_numbers(unique_segments, two_three_five, zero_six_nine):
    three = list(filter(lambda s: set(unique_segments['cf']).issubset(set(s)), two_three_five))[0]
    two = list(filter(lambda s: set(unique_segments['eg']).issubset(set(s)), two_three_five))[0]
    five = list(set(two_three_five) - {three, two})[0]

    nine = list(filter(lambda s: not set(unique_segments['eg']).issubset(set(s)), zero_six_nine))[0]
    zero_six = list(set(zero_six_nine) - {nine})
    six = list(filter(lambda s: set(unique_segments['bd']).issubset(set(s)), zero_six))[0]
    zero = list(set(zero_six) - {six})[0]

    return {
        3: three,
        2: two,
        5: five,
        9: nine,
        6: six,
        0: zero,
    }


def main():
    lines = get_lines()

    lines = list(map(parse_input, lines))

    total = 0

    for input, output in lines:
        unique_input = [i for i in input if len(i) in UNIQUE_LENGTHS.values()]

        one = find_by_number(unique_input, 1)
        four = find_by_number(unique_input, 4)
        seven = find_by_number(unique_input, 7)
        eight = find_by_number(unique_input, 8)

        unique_segments = deduct_unique_segments(one, four, seven, eight)

        two_three_five = find_by_length(input, 5)
        zero_six_nine = find_by_length(input, 6)

        other_numbers = deduct_other_numbers(unique_segments, two_three_five, zero_six_nine)

        all_numbers = other_numbers.copy()
        all_numbers[1] = one
        all_numbers[4] = four
        all_numbers[7] = seven
        all_numbers[8] = eight

        output_number = ''

        for num in output:
            for digit, string_num in all_numbers.items():
                if is_same_number(num, string_num):
                    output_number += str(digit)
                    break

        total += int(output_number)

    print(total)


if __name__ == "__main__":
    main()
