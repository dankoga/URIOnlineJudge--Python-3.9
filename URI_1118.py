choice = '1'
while choice == '1':
    grade_1 = float(input())
    while not (0.0 <= grade_1 <= 10.0):
        print('nota invalida')
        grade_1 = float(input())

    grade_2 = float(input())
    while not (0.0 <= grade_2 <= 10.0):
        print('nota invalida')
        grade_2 = float(input())

    print('media = {:.2f}'.format((grade_1 + grade_2) / 2.0))
    choice = input('novo calculo (1-sim 2-nao)\n')
    while not (choice == '1' or choice == '2'):
        choice = input('novo calculo (1-sim 2-nao)\n')
