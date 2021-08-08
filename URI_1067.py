number_max = int(input())
number_max += number_max % 2
for number in range(1, number_max, 2):
    print(number)