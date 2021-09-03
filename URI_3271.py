from itertools import accumulate


def dice_results(dices, n):
    a1, b1, a2, b2 = dices
    results = [0] * (n + 1)
    for d1 in range(a1, b1 + 1):
        for d2 in range(a2, b2 + 1):
            results[d1 + d2] += 1
    return results


if __name__ == '__main__':
    dices_g = list(map(int, input().split()))
    dices_e = list(map(int, input().split()))
    number_max = max([dices_g[1] + dices_g[3], dices_e[1] + dices_e[3]])
    results_g = dice_results(dices_g, number_max)
    results_e = dice_results(dices_e, number_max)

    wins_g = 0
    cumulative_e = list(accumulate(results_e))
    for result, frequency in enumerate(results_g):
        wins_g += frequency * cumulative_e[result - 1]

    wins_e = 0
    cumulative_g = list(accumulate(results_g))
    for result, frequency in enumerate(results_e):
        wins_e += frequency * cumulative_g[result - 1]

    if wins_g > wins_e:
        print('Gunnar')
    elif wins_g < wins_e:
        print('Emma')
    else:
        print('Tie')
