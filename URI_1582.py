import sys
from math import gcd

if __name__ == '__main__':
    for input_line in sys.stdin:
        triple = list(map(int, input_line.split()))
        triple.sort()
        if triple[0] ** 2 + triple[1] ** 2 == triple[2] ** 2:
            if gcd(gcd(triple[0], triple[1]), triple[2]) == 1:
                print('tripla pitagorica primitiva')
            else:
                print('tripla pitagorica')
        else:
            print('tripla')
