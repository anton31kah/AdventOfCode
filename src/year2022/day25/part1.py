from src.common.common import get_lines


def snafu_digit_to_int_digit(snafu_digit):
    match snafu_digit:
        case '2':
            return 2
        case '1':
            return 1
        case '0':
            return 0
        case '-':
            return -1
        case '=':
            return -2


def int_digit_to_snafu_digit(snafu_digit):
    match snafu_digit:
        case 0:
            return '0'
        case 1:
            return '1'
        case 2:
            return '2'
        case -1:
            return '-'
        case -2:
            return '='


def snafu_to_int(snafu):
    number = 0
    for i, digit in enumerate(snafu):
        digit = snafu_digit_to_int_digit(digit)
        place = 5 ** (len(snafu) - i - 1)
        number += digit * place
    return number


def int_to_snafu(number):
    # https://cp-algorithms.com/algebra/balanced-ternary.html#conversion-algorithm

    snafu_digits = []
    while number > 0:
        number, remainder = divmod(number, 5)
        snafu_digits.append(remainder)
    snafu_digits.reverse()

    snafu_digits.insert(0, 0)

    while any(d >= 3 for d in snafu_digits):
        for i in reversed(range(len(snafu_digits))):
            if snafu_digits[i] >= 3:
                snafu_digits[i] -= 5
                snafu_digits[i - 1] += 1

    snafu_digits = list(map(int_digit_to_snafu_digit, snafu_digits))

    return ''.join(snafu_digits).removeprefix('0')


def main():
    lines = get_lines('')

    total = 0

    for line in lines:
        total += snafu_to_int(line)

    print(int_to_snafu(total))


if __name__ == "__main__":
    main()
