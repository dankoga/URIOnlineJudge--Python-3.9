for t in range(int(input())):
    number_a, number_b = input().split()
    if number_a[-len(number_b):] == number_b:
        print('encaixa')
    else:
        print('nao encaixa')
