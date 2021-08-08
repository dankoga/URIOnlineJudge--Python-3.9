input_line = list(map(int, input().split()))

number_1 = input_line[0]
for number in input_line[1:]:
    if number > 0:
        number_2 = number
        break

print('{}'.format(number_2 * (2 * number_1 + number_2 - 1)//2))