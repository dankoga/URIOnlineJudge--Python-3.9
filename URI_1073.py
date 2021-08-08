number_max = int(input())
number_max += 1 - number_max % 2
for number in range(2, number_max, 2):
    print('{}^2 = {}'.format(number, number ** 2))