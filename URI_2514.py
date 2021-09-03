import sys
from math import lcm

if __name__ == '__main__':
    for input_data in sys.stdin:
        last_alignment = int(input_data)
        t1, t2, t3 = map(int, input().split())
        print(lcm(lcm(t1, t2), t3) - last_alignment)
