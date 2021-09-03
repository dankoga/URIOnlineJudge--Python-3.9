import time
st = time.perf_counter()
import sys


MOD = 1300031

tests_qty = input()
inputs_list = []
for line in sys.stdin:
    N, C = map(int, line.split())
    N += C - 1
    inputs_list.append([N, C])

# Precomputing factorials and inverse multiplicative factorials up to the biggest n or MOD
factorials = [[1, 1]]
for n in range(1, min(max(max(inputs_list, key=max)) + 1, MOD)):
    new_f = ((factorials[n - 1][0] % MOD) * n) % MOD
    # Using Fermat's little theorem for the inverse multiplicative
    factorials.append([new_f, pow(new_f, MOD - 2, MOD)])

for binomial in inputs_list:
    n = binomial[0]
    k = binomial[1]
    result = 1
    # Using Lucas' theorem to expand the binomials in base MOD
    # as N, C < MOD, no factorial will be divisible by MOD, so no problems here
    while n + k > 0:
        n, n_m = divmod(n, MOD)
        k, k_m = divmod(k, MOD)
        result = ((result * factorials[n_m][0]) % MOD *
                  (factorials[n_m - k_m][1] * factorials[k_m][1]) % MOD) % MOD
    print(result)

print(time.perf_counter() - st)
