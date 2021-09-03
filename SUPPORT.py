from itertools import accumulate

MOD = 1300031


def diophantine_count(n, c):
    # count solutions for x1 + x2 + ... xn = c
    p = [1 for _ in range(c+1)]
    print(p)
    for i in range(1, n):
        p = list(accumulate(p, lambda x, y: (x + y) % MOD))
        print(p)

diophantine_count(10,10)