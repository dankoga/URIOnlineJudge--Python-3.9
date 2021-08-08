while True:
    number_A , number_B = map(int, input().split())
    if number_A == number_B:
        break
    elif number_A < number_B:
        print('Crescente')
    else:
        print('Decrescente')