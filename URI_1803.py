import sys


matring = [line.rstrip() for line in sys.stdin]

f = int(''.join([line[0] for line in matring]))
l = int(''.join([line[-1] for line in matring]))

decoded_message = []
for i in range(1, len(matring[0]) - 1):
    number_col = int(''.join([line[i] for line in matring]))
    decoded_message += [(f * number_col + l) % 257]

print(''.join([chr(d) for d in decoded_message]))
