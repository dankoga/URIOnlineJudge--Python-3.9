from math import ceil

tests_qty = int(input())
for t in range(tests_qty):
    input_line = input()
    half = int(ceil(len(input_line) / 2))
    encrypted = [chr(ord(c) + 2) if c.isalpha() else chr(ord(c) - 1) for c in input_line[:half]] + \
                [chr(ord(c) + 3) if c.isalpha() else c for c in input_line[half:]]
    print(''.join(reversed(encrypted)))
