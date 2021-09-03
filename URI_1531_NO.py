import sys
from math import sqrt

SQRT5 = sqrt(5.0)
PHI = (1.0 + SQRT5) / 2.0


def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            return i + 1


def fibonacci(n, m):
    f = 1
    p = PHI
    while n > 0:
        if n & 1:
            f = (f * p) % m
        n >>= 1
        p = (p * p) % m
    return int(f / SQRT5 + 0.5)


if __name__ == '__main__':
    mod = 0
    period1 = 0
    period2 = 0
    for input_line in sys.stdin:
        N, mod_new = map(int, input_line.split())
        if mod_new != mod:
            period1 = pisano_period(mod_new)
            period2 = pisano_period(period1)

        mod = mod_new
        print(fibonacci(fibonacci(N % period2, period1), mod))
