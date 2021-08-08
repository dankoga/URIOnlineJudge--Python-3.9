GAME_TABLE = {'ataque': {'ataque': 0, 'pedra': 1, 'papel': 1},
              'pedra':  {'ataque': 2, 'pedra': 4, 'papel': 1},
              'papel':  {'ataque': 2, 'pedra': 2, 'papel': 3},}
RESULTS = ['Aniquilacao mutua',
           'Jogador 1 venceu',
           'Jogador 2 venceu',
           'Ambos venceram',
           'Sem ganhador']

games_qty = int(input())
for game in range(games_qty):
    hand_1 = input()
    hand_2 = input()
    print(RESULTS[GAME_TABLE[hand_1][hand_2]])
