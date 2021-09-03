from math import log10

WINNER_NAME = ['Lucas', 'Pedro']

if __name__ == '__main__':
    cases_qty = int(input())
    game_results = [0] * cases_qty
    for c in range(cases_qty):
        base, exponent = map(float, input().split('^'))
        factor = int(input().split('!')[0])

        lucas_score = exponent * log10(base)
        pedro_score = 0
        for f in range(factor, 0, -1):
            pedro_score += log10(f)
            if pedro_score > lucas_score:
                game_results[c] = 1
                break

    if 2 * sum(game_results) == cases_qty:
        print('A competicao terminou empatada!')
    else:
        w = (2 * sum(game_results) > cases_qty)
        print('Campeao: {}!'.format(WINNER_NAME[w]))

    for c in range(cases_qty):
        print('Rodada #{}: {} foi o vencedor'.format(c + 1, WINNER_NAME[game_results[c]]))


