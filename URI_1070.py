number_min = int(input())
number_min += 1 - number_min % 2
number_max = number_min + 10 + number_min % 2
for number in range(number_min, number_max, 2):
    print(number)