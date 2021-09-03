import sys
from math import sqrt, pow

P = sqrt((25.0 + 10.0 * sqrt(5.0))) / 4.0

if __name__ == '__main__':
    cases_qty = input()
    for side_length in sys.stdin:
        print('{:.3f}'.format(P * pow(float(side_length), 2)))
