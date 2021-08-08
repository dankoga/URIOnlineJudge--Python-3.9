GAME_TABLE = {'pedra'  : {'pedra': 0, 'papel': 1, 'tesoura': 2, 'lagarto': 2, 'Spock': 1},
              'papel'  : {'pedra': 2, 'papel': 0, 'tesoura': 1, 'lagarto': 1, 'Spock': 2},
              'tesoura': {'pedra': 1, 'papel': 2, 'tesoura': 0, 'lagarto': 2, 'Spock': 1},
              'lagarto': {'pedra': 1, 'papel': 2, 'tesoura': 1, 'lagarto': 0, 'Spock': 2},
              'Spock'  : {'pedra': 2, 'papel': 1, 'tesoura': 2, 'lagarto': 1, 'Spock': 0}}
GAME_RESULT_STR = ['De novo!', 'Raj trapaceou!', 'Bazinga!']


games_max = int(input())
for game in range(1, games_max + 1):
    hand_sheldon, hand_raj = input().split()
    print('Caso #{}: {}'.format(game, GAME_RESULT_STR[GAME_TABLE[hand_sheldon][hand_raj]]))