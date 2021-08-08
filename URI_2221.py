cases_qty = int(input())
for case in range(cases_qty):
    bonus = int(input())
    dabriel_attack, dabriel_defense, dabriel_level = map(int, input().split())
    guarte_attack, guarte_defense, guarte_level = map(int, input().split())

    dabriel_value = (dabriel_attack + dabriel_defense) / 2 + bonus * (1 - dabriel_level % 2)
    guarte_value = (guarte_attack + guarte_defense) / 2 + bonus * (1 - guarte_level % 2)
    if dabriel_value > guarte_value:
        print('Dabriel')
    elif dabriel_value < guarte_value:
        print('Guarte')
    else:
        print('Empate')
