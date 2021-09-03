from math import sqrt

SQRT5 = sqrt(5)
PHI = (1 + SQRT5) / 2


def fast_fibonacci(n):
    return int(pow(PHI, n) / SQRT5 + 0.5)


if __name__ == '__main__':
    while True:
        tiles_qty = float(input())
        if tiles_qty == 0:
            break
        print(fast_fibonacci(tiles_qty + 1))
