ASCII_DICT = {'**** ** ** ****': 0,
              '  *  *  *  *  *': 1,
              '***  *****  ***': 2,
              '***  ****  ****': 3,
              '* ** ****  *  *': 4,
              '****  ***  ****': 5,
              '****  **** ****': 6,
              '***  *  *  *  *': 7,
              '**** ***** ****': 8,
              '**** ****  ****': 9}

input_line = input()
digits_qty = (len(input_line) - 3) // 4 + 1
digits_ascii = [input_line[:3]] + [input_line[4*i:4*i + 3] for i in range(1, digits_qty)]
for line in range(1, 5):
    input_line = input()
    digits_ascii[0] += input_line[:3]
    for i in range(1, digits_qty):
        digits_ascii[i] += input_line[4 * i:4 * i + 3]

try:
    digits_num = [ASCII_DICT[d] for d in digits_ascii]
except KeyError:
    print('BOOM!!')
    exit(0)
if digits_num[-1] % 2 == 0 and sum(digits_num) % 3 == 0:
    print('BEER!!')
else:
    print('BOOM!!')
