import sys

input_numbers = sys.stdin.readlines()
max_length = max(map(len, input_numbers))

mod_base = 10 ** 9 + 7
BASE_26 = [pow(26, i, mod_base) for i in range(0, max_length)]

for number_ABC in input_numbers:
    number_10 = sum([((ord(c) - 65) * BASE_26[i]) % mod_base for i, c in enumerate(reversed(number_ABC.rstrip()))]) % mod_base
    print(number_10)