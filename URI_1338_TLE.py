import time
import sys
from math import sqrt, log


def prime_sieve(n):
    sieve = [True for _ in range(n)]
    sieve[0:2] = [False] * 2
    sieve[4::2] = [False] * len(sieve[4::2])
    sieve[6::3] = [False] * len(sieve[6::3])
    for p in range(5, int(sqrt(n)) + 1, 2):
        if sieve[p]:
            sieve[p*p::p] = [False] * len(sieve[p*p::p])
    return [p for p, s in enumerate(sieve) if s]


def mobius_function(n, p_list):
    mu = [1 for _ in range(n + 1)]
    for p in p_list:
        if p > n:
            break
        p2 = p * p
        mu[p2::p2] = [0] * len(mu[p2::p2])
        mu[p::p] = [-m for m in mu[p::p]]
    return mu


def square_free_count(n, m_list):
    return sum([m_list[i] * (n // (i ** 2)) for i in range(1, int(sqrt(n)) + 1)])


def square_free(n, m_list):
    index_l = 4 * n // 6
    index_r = 10 * n // 6
    while index_l < index_r:
        index_m = (index_l + index_r) // 2
        count = square_free_count(index_m, m_list)
        if count < n:
            index_l = index_m+1
        else:
            index_r = index_m
    return index_l


if __name__ == "__main__":
    t_start = time.perf_counter()
    cases_qty = input()
    input_values = [int(line) for line in sys.stdin]
    n_max = max(input_values)
    limit_upper = 10 * n_max // 6
    limit_sqrt = int(sqrt(limit_upper))
    t1 = time.perf_counter()

    primes = prime_sieve(limit_sqrt + int(log(limit_upper)))
    t2 = time.perf_counter()

    mobius = mobius_function(limit_sqrt + 1, primes)
    t3 = time.perf_counter()

    for n in input_values:
        print(square_free(n, mobius))
    t4 = time.perf_counter()
    print('Input: {}'.format(t1 - t_start))
    print('Primes: {}'.format(t2 - t1))
    print('Mobius: {}'.format(t3 - t2))
    print('Results: {}'.format(t4 - t3))
    print('TOTAL: {}'.format(t4 - t_start))
