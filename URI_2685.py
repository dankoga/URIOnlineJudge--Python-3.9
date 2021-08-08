MESSAGES = ['Bom Dia!!',
            'Boa Tarde!!',
            'Boa Noite!!',
            'De Madrugada!!',
            'Bom Dia!!']

while True:
    try:
        angular_position = int(input())
    except EOFError:
        break
    print(MESSAGES[angular_position // 90])

