from math import sqrt, log

SQRT5 = sqrt(5.0)
GAMMA = 1.0 / log((SQRT5 + 1) / 2)


def not_fibonacci(n):
    m = n + 1
    return int(m + GAMMA * log(SQRT5 * (GAMMA * log(SQRT5 * m) + m) - 5.0 + 3.0 / m) - 2.0)


term_order = float(input())
print(not_fibonacci(term_order))
