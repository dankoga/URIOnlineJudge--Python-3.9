from functools import reduce
import sys

MOD = 1000000007


def generate_factorials(n_max):
    f_list = list(range(n_max + 1))
    f_list[0] = 1
    for n in range(1, n_max + 1):
        f_list[n] = (f_list[n] * f_list[n - 1]) % MOD
    return f_list


def factorial_mod(n, f_list):
    # if n > MOD, returns (m, (n!/MOD^m) % MOD) where m is the MOD multiplicity
    if n < MOD:
        return [0, f_list[n]]
    else:
        f = 1
        m = 0
        while n > 1:
            if (n // MOD) % 2 > 0:
                f = MOD - f
            f = (f * f_list[n % MOD]) % MOD
            n //= MOD
            m += n
        return m, f


if __name__ == '__main__':
    words = [w.rstrip() for w in sys.stdin]

    factorials = generate_factorials(min(max([len(w) for w in words]), MOD))
    for w in words:
        letter_count = [0] * 26
        for l in w:
            letter_count[ord(l) - 65] += 1

        m1, f1 = factorial_mod(len(w), factorials)
        f_letters = [factorial_mod(count, factorials) for count in letter_count]
        m2 = sum([f[0] for f in f_letters])
        f2 = reduce(lambda x, y: (x * y) % MOD, [f[1] for f in f_letters])

        print(int(m1 == m2) * (f1 * pow(f2, MOD - 2, MOD)) % MOD)


#   O cálculo do coeficiente binomial modular seguiu essa referência:
#  https://cp-algorithms.com/algebra/factorial-modulo.html
