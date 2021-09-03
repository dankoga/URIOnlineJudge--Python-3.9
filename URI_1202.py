# Pisano periods.


FIBONACCI_MOD = [0, 1, 1]
for n in range(3, 1501):
    FIBONACCI_MOD.append((FIBONACCI_MOD[n - 1] + FIBONACCI_MOD[n - 2]) % 1000)


def bin_to_dec_mod(number_bin):
    number_dec = 0
    for digit in number_bin:
        number_dec = (2 * number_dec + int(digit)) % 1500
    return number_dec


tests_qty = int(input())
for t in range(tests_qty):
    row_occupation = input()
    print('{:0>3d}'.format(FIBONACCI_MOD[bin_to_dec_mod(row_occupation)]))
