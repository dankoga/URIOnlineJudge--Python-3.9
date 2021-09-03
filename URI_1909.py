from math import prod, sqrt


def prime_sieve(n):
    is_p = [True] * (n + 1)
    is_p[0:1] = [False] * 2
    is_p[4::2] = [False] * len(is_p[4::2])
    is_p[9::3] = [False] * len(is_p[9::3])
    f = 5
    while f * f <= n:
        if is_p[f]:
            is_p[f * f::f] = [False] * len(is_p[f * f::f])
        f += 2
    return [p for p, f in enumerate(is_p) if f]


def factorization(n, p_list):
    e = [0] * len(p_list)
    for i, p in enumerate(p_list):
        while n % p == 0:
            n //= p
            e[i] += 1
        if n == 1:
            break
    return e


def divisors(n):
    d = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            d.append(i)
            d.append(n//i)
    return sorted(d)


if __name__ == '__main__':
    target_periods = []
    balls_periods = []
    while True:
        balls, target = map(int, input().split())
        if balls == target == 0:
            break
        target_periods.append(target)
        balls_periods.append(list(map(int, input().split())))

    primes = prime_sieve(max(target_periods))

    for target, balls in zip(target_periods, balls_periods):
        if any([target % b != 0 for b in balls]):
            print('impossivel')
            continue

        target_factorized = factorization(target, primes)
        balls_lcm_factorized = [0] * len(primes)
        for each_ball in balls:
            ball_period_factorized = factorization(each_ball, primes)
            balls_lcm_factorized = [max(a, b) for a, b in zip(balls_lcm_factorized, ball_period_factorized)]

        if target_factorized == balls_lcm_factorized:
            for d in divisors(target)[1::]:
                if d not in balls:
                    print(d)
                    break
            else:
                print('impossivel')
        else:
            new_ball_factorized = [a if a > b else 0 for a, b in zip(target_factorized, balls_lcm_factorized)]
            print(prod([p ** e for p, e in zip(primes, new_ball_factorized)]))