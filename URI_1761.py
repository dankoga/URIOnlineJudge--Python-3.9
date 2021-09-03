import sys
from math import tan

RAD = 3.141592654 / 180.0


if __name__ == '__main__':
    for data in sys.stdin:
        angle, distance, height = map(float, data.split())
        print('{:.2f}'.format(5.0 * (height + distance * tan(angle * RAD))))
