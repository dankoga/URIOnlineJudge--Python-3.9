from math import log2, ceil

tests_qty = int(input())
for t in range(tests_qty):
    initial_food = float(input())
    print('{:.0f} dias'.format(ceil(log2(initial_food))))
