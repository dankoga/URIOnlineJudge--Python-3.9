NUMBASE = {'bin': 2, 'dec': 10, 'hex': 16}

cases_qty = int(input())
for c in range(1, cases_qty + 1):
    number_str, base = input().split()
    number = int(number_str, NUMBASE[base])
    print('Case {}:'.format(c))
    if base == 'bin':
        print('{} dec'.format(number))
        print('{:x} hex'.format(number))
    elif base == 'dec':
        print('{:x} hex'.format(number))
        print('{:b} bin'.format(number))
    elif base == 'hex':
        print('{} dec'.format(number))
        print('{:b} bin'.format(number))
    print()
