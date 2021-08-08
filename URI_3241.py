tests_qty = int(input())
for t in range(tests_qty):
    expression = input()
    if expression == 'P=NP':
        print('skipped')
    else:
        print(eval(expression))
