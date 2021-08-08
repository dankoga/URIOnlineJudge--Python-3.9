import sys

tests_qty = input()
for line in sys.stdin:
    number_larger, number_smaller = line.split()
    if number_larger[-len(number_smaller):] == number_smaller:
        print('encaixa')
    else:
        print('nao encaixa')
