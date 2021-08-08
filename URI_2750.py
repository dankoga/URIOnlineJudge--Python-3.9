print('-' * 39)
print('|  decimal  |  octal  |  Hexadecimal  |')
print('-' * 39)
for number in range(16):
    print('|{:>7d}    |{:>5o}    |{:>8X}       |'.format(number, number, number))
print('-' * 39)
