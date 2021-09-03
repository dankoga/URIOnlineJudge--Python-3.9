import sys
from math import gcd

if __name__ == '__main__':
    for input_line in sys.stdin:
        size_x, size_y = map(int, input_line.split())
        print(2 * (size_x + size_y) // gcd(size_x, size_y))
