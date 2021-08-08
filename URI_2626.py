GAME_TABLE = {'pedra':   {'pedra':   {'pedra': 3, 'papel': 2, 'tesoura': 3},
                          'papel':   {'pedra': 1, 'papel': 3, 'tesoura': 3},
                          'tesoura': {'pedra': 3, 'papel': 3, 'tesoura': 0}},
              'papel':   {'pedra':   {'pedra': 0, 'papel': 3, 'tesoura': 3},
                          'papel':   {'pedra': 3, 'papel': 3, 'tesoura': 2},
                          'tesoura': {'pedra': 3, 'papel': 1, 'tesoura': 3}},
              'tesoura': {'pedra':   {'pedra': 3, 'papel': 3, 'tesoura': 1},
                          'papel':   {'pedra': 3, 'papel': 0, 'tesoura': 3},
                          'tesoura': {'pedra': 2, 'papel': 3, 'tesoura': 3}}}
WIN_QUOTE = ["Os atributos dos monstros vao ser inteligencia, sabedoria...",
             "Iron Maiden's gonna get you, no matter how far!",
             "Urano perdeu algo muito precioso...",
             "Putz vei, o Leo ta demorando muito pra jogar..."]

while True:
    try:
        hand1, hand2, hand3 = input().split()
        print(WIN_QUOTE[GAME_TABLE[hand1][hand2][hand3]])
    except EOFError:
        break
