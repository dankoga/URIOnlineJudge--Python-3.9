MOD = 1300031


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


def binomial(n, k, f_list):
    if k > n:
        return 0

    m_n, f_n = factorial_mod(n, f_list)
    m_k, f_k = factorial_mod(k, f_list)
    m_nk, f_nk = factorial_mod(n - k, f_list)

    return int(m_n == m_k + m_nk) * (f_n * pow((f_k * f_nk) % MOD, MOD - 2, MOD)) % MOD


if __name__ == '__main__':
    cases_qty = int(input())
    n_list = []
    k_list = []
    for _ in range(cases_qty):
        variables, constant = map(int, input().split())
        n_list.append(constant + (variables - 1))
        k_list.append(variables - 1)

    factorials = generate_factorials(min(max(n_list), MOD))
    for n, k in zip(n_list, k_list):
        print(binomial(n, k, factorials))


#   O número de soluções de uma equação linear diofantina de 1 variável é:
#     x1 = c
#
#   Logo:
#     P_{1}(c) = 1
#
#   Já para 2 variáveis:
#     0 + (x1 - 0) = c
#     1 + (x1 - 1) = c
#     2 + (x1 - 2) = c
#     ...
#     c + 0 = c
#
#     P_{2}(c) = P_{1}(c) + P_{1}(c-1) + ... P_{1}(0)
#
#   Generalizando:
#     P_{N}(c) = sum(P_{N-1](i) i = 0 .. c
#
#   Olhando o padrão que se forma nos números, eles se organizam como elementos de um triângulo de Pascal, então:
#     P_{N}(c) = c * (c + 1) * (c + 2) * ... (c + N - 1) / N!
#
#
#   O cálculo do coeficiente binomial modular seguiu essa referência:
#  https://cp-algorithms.com/algebra/factorial-modulo.html
