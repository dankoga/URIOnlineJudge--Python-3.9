import sys


def barrel_range(n):
    current = 5
    increase = 2
    while current < n + 1:
        yield current
        current += increase
        increase ^= 6


def prime_sieve(number_max):
    if number_max < 2:
        return []
    if number_max == 2:
        return [2]

    prime_list = [2, 3]
    sieve_list = [True] * (number_max + 1)
    for each_number in barrel_range(number_max):
        if sieve_list[each_number]:
            prime_list.append(each_number)
            for multiple in range(each_number*each_number, number_max + 1, each_number):
                sieve_list[multiple] = False
    return prime_list


key_prime_list = [list(map(int, line.split())) for line in sys.stdin.readlines()]
primes_list = prime_sieve(max(key_prime_list, key=lambda x: x[1])[1])

for key_prime in key_prime_list[:-1]:
    p = 0
    while p < len(primes_list) and primes_list[p] < key_prime[1]:
        if key_prime[0] % primes_list[p] == 0:
            print('BAD {}'.format(primes_list[p]))
            break
        p += 1
    else:
        print('GOOD')

