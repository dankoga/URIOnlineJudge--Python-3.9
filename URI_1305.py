def number_splitter(num):
    if '.' in num:
        if num[0] == '.':
            return '0', num[1:]
        elif num[-1] == '.':
            return num[:-1], '0'
        else:
            return num.split('.')
    else:
        return num, '0'


def rounder(frac, cutoff):
    if len(frac) > len(cutoff):
        cutoff = cutoff + '0' * (len(frac) - len(cutoff))
    else:
        frac = frac + '0' * (len(cutoff) - len(frac))

    for i, digit in enumerate(frac):
        if int(digit) > int(cutoff[i]):
            return 1
        elif int(digit) < int(cutoff[i]):
            return 0
    return 0


while True:
    try:
        number_int_str, number_frac_str = number_splitter(input())
    except EOFError:
        break
    cutoff_int_str, cutoff_frac_str = number_splitter(input())

    print(int(number_int_str) + rounder(number_frac_str, cutoff_frac_str))
