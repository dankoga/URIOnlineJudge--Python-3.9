import re

operands_qty = int(input())
test_number = 1
while operands_qty > 0:
    print('Teste {}'.format(test_number))
    print(eval(re.sub(r'\b0+(?!\b)', '', input())))
    print()
    test_number += 1
    operands_qty = int(input())
