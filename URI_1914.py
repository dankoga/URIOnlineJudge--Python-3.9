input_size = int(input())
for game in range(input_size):
    name_A, choice_A, name_B, choice_B = input().split()
    number_A, number_B = map(int, input().split())
    if (number_A + number_B) % 2 == 0:
        if choice_A == 'PAR':
            print(name_A)
        else:
            print(name_B)
    else:
        if choice_A == 'PAR':
            print(name_B)
        else:
            print(name_A)
