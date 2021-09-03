import sys


def is_div3(s):
    digital_sum = sum([int(d) for d in s])
    return digital_sum % 3 == 0


def is_div4(s):
    return int(s[-2:]) % 4 == 0


def is_div5(s):
    return s[-1] == '0' or s[-1] == '5'


def is_div11(s):
    alter_digital_sum = sum([int(d) * ((-1) ** i) for i, d in enumerate(s)])
    return alter_digital_sum % 11 == 0


def is_div100(s):
    return s[-2:] == '00'


def is_div400(s):
    return s[-2:] == '00' and int(s[-4:-2]) % 4 == 0


is_first = True
for input_line in sys.stdin:
    if is_first:
        is_first = False
    else:
        print()
    year = input_line.rstrip()

    if (is_div4(year) and not is_div100(year)) or is_div400(year):
        print('This is leap year.')
        is_leap_year = True
    else:
        is_leap_year = False

    is_festival_year = False
    if is_div3(year) and is_div5(year):
        print('This is huluculu festival year.')
        is_festival_year = True
    if is_leap_year and is_div5(year) and is_div11(year):
        print('This is bulukulu festival year.')
        is_festival_year = True

    if not (is_leap_year or is_festival_year):
        print('This is an ordinary year.')
