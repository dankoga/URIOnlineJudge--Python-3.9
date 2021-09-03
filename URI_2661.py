def count_prime_factors(n):
    INCREASE = [4, 2, 4, 2, 4, 6, 2, 6]
    factors_qty = int(n % 2 == 0) + int(n % 3 == 0) + int(n % 5 == 0)
    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //= 5

    factor = 7
    i = 0
    while factor * factor <= n:
        factors_qty += int(n % factor == 0)
        while n % factor == 0:
            n //= factor
        factor += INCREASE[i]
        i = (i + 1) % 8
    if n > 1:
        factors_qty += 1

    return factors_qty


if __name__ == '__main__':
    factors_qty = count_prime_factors(int(input()))
    print(2 ** factors_qty - factors_qty - 1)
