input_line = input()
displacement = abs(ord(input_line[0]) - ord(input_line[3])) \
               + 10 * abs(int(input_line[1]) - int(input_line[4]))
if displacement == 12 or displacement == 21:
    print('VALIDO')
else:
    print('INVALIDO')
