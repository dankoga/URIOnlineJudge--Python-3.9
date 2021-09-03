from itertools import accumulate

def twin_prime_sieve(n_max):
    is_p = [True] * (n_max + 1)
    is_p[0:1] = [False] * 2
    is_p[2::2] = [False] * len(is_p[2::2])
    is_p[9::3] = [False] * len(is_p[9::3])
    f1 = 5
    f2 = 7
    while f1 * f1 <= n_max:
        if is_p[f1]:
            is_p[f1 * f1::f1] = [False] * len(is_p[f1 * f1::f1])
        if is_p[f2]:
            is_p[f2 * f2::f2] = [False] * len(is_p[f2 * f2::f2])
        are_twins = is_p[f1] and is_p[f2]
        is_p[f1] = are_twins
        is_p[f2] = are_twins
        f1 += 6
        f2 += 6
    while f2 <= len(is_p):
        are_twins = is_p[f1] and is_p[f2]
        is_p[f1] = are_twins
        is_p[f2] = are_twins
        f1 += 6
        f2 += 6
    #print([n for n, f in enumerate(is_p) if f])
    return is_p


if __name__ == '__main__':
    cases_qty = int(input())
    n_min_list = []
    n_max_list = []
    for c in range(cases_qty):
        n = list(map(int, input().split()))
        n.sort()
        n_min_list.append(n[0])
        n_max_list.append(n[1])
    global_max = max(n_max_list)
    is_twin_prime = twin_prime_sieve(global_max + 2)
    twin_prime_cumulative = list(accumulate(is_twin_prime))
    #print(twin_prime_cumulative)

    for c in range(cases_qty):
        twins = twin_prime_cumulative[n_max_list[c]] - twin_prime_cumulative[n_min_list[c] - 1]
        print(twins)
