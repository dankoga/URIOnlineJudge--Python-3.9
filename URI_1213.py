import sys

for input_line in sys.stdin:
    number = int(input_line)
    ones_sequence = 0
    digits = 0
    while True:
        digits += 1
        ones_sequence = (10 * ones_sequence + 1) % number
        if ones_sequence == 0:
            break
    print(digits)
