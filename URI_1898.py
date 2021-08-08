import sys

sys.stdin.reconfigure(errors='ignore')


row_1 = ''.join([char for char in input() if char.isnumeric() or char == '.'])
row_2 = ''.join([char for char in input() if char.isnumeric() or char == '.'])
dot_index = row_1.find('.')
if dot_index < 0:
    value_a = float(row_1[11:])
else:
    value_a = float(row_1[11:dot_index + 3])
dot_index = row_2.find('.')
if dot_index < 0:
    value_b = float(row_2)
else:
    value_b = float(row_2[:dot_index + 3])
print('cpf {}\n{:.2f}'.format(row_1[:11], value_a + value_b))
