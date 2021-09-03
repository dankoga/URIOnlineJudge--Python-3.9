import sys

MOD = 1000000009
# using Fermat's little theorem 1/6 mod MOD = pow(6, MOD - 2, MOD)
INV6MOD = 833333341


def prime_sieve(n_max):
    is_prime = [True] * (n_max + 1)
    is_prime[0:2] = [False] * 2
    is_prime[4::2] = [False for _ in is_prime[4::2]]
    is_prime[9::3] = [False for _ in is_prime[9::3]]
    p = 5
    while p * p <= n_max:
        if is_prime[p]:
            is_prime[p * p::p] = [False for _ in is_prime[p * p::p]]
        p += 2
        if is_prime[p]:
            is_prime[p * p::p] = [False for _ in is_prime[p * p::p]]
        p += 4
    return [n for n, is_p in enumerate(is_prime) if is_p]


def factorial_mod(n, p_list):
    # Using Legendre's formula.
    result = 1
    for p in p_list:
        exponent = 0
        m = n
        while m > 0:
            m //= p
            exponent += m
        result = (result * pow(p, exponent, MOD)) % MOD
        if p > n:
            break
    return result


if __name__ == '__main__':
    input_list = [int(i) for i in sys.stdin.readlines()]
    primes_list = prime_sieve(max(input_list))
    for people in input_list[:-1]:
        print((factorial_mod(people, primes_list) * INV6MOD) % MOD)


#  Para resolver o problema, vamos começar com uma fila com somente A, B e C em ordem:
#    ABC
#
#  Existem 4 posições possíveis para adicionarmos uma pessoa formando filas diferentes mantendo a ordem de ABC:
#    xABC, AxBC, ABxC, ABCx
#
#  Agora, não importa qual das filas acima foi formada, existem 5 posições possíveis para adicionarmos uma nova pessoa.
# Seguindo o raciocínio, se quisermos manter a ordem de k pessoas, a quantidade de filas diferentes, se adicionarmos n
# novas pessoas será:
#   F(n,k) = (k+1) * (k + 2) * ... * (k + n)
#
#  Lembrando que:
#    k! = 1 * 2 * ... * k
# podemos reescrever F(n,k) como:
#   F(n, k) = 1/(k!) * (1 * 2 * ... * k * (k + 1) * (k + 2) * ... * (k + n))
#   F(n, k) = ((k + n)!))/(k!)
#
#
#  Como temos que calcular o fatorial em modulo M de números grandes, foi usada a fórmula de Legendre:
#    https://en.wikipedia.org/wiki/Legendre%27s_formula
