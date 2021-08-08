ROMANS_0 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
ROMANS_1 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
ROMANS_2 = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']

number_str = input()
digits = [0, 0] + [int(d) for d in number_str]
print(ROMANS_2[digits[-3]] + ROMANS_1[digits[-2]] + ROMANS_0[digits[-1]])
