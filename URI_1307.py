import math

pairs_qty = int(input())
for p in range(pairs_qty):
    number_s = int(input(), 2)
    number_l = int(input(), 2)
    print('Pair #{}:'.format(p + 1), end=' ')
    if math.gcd(number_s, number_l) == 1:
        print('Love is not all you need!')
    else:
        print('All you need is love!')
