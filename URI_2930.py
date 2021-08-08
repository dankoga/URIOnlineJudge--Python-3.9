date_delivery, date_deadline = map(int, input().split())
if date_delivery > date_deadline or date_deadline >= 24:
    print('Eu odeio a professora!')
elif date_delivery <= date_deadline - 3:
    print('Muito bem! Apresenta antes do Natal!')
else:
    print('Parece o trabalho do meu filho!')
    if date_delivery + 2 < 24:
        print('TCC Apresentado!')
    else:
        print('Fail! Entao eh nataaaaal!')
