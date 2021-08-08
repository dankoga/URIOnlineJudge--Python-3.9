GAME_TABLE = {'pedra'  : {'pedra': 0, 'papel': 1, 'tesoura': 2, 'lagarto': 2, 'spock': 1},
              'papel'  : {'pedra': 2, 'papel': 0, 'tesoura': 1, 'lagarto': 1, 'spock': 2},
              'tesoura': {'pedra': 1, 'papel': 2, 'tesoura': 0, 'lagarto': 2, 'spock': 1},
              'lagarto': {'pedra': 1, 'papel': 2, 'tesoura': 1, 'lagarto': 0, 'spock': 2},
              'spock'  : {'pedra': 2, 'papel': 1, 'tesoura': 2, 'lagarto': 1, 'spock': 0}}
GAME_RESULT_STR = ['empate', 'sheldon', 'rajesh']

games_qty = int(input())
for g in range(games_qty):
    hand_1, hand_2 = input().split()
    print(GAME_RESULT_STR[GAME_TABLE[hand_1][hand_2]])
