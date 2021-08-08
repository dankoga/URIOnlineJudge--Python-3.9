number_A = int(input())
number_B = int(input())
if number_A > number_B:
    buffer = number_A
    number_A = number_B
    number_B = buffer

for number in range(number_A + 1, number_B):
    if (number % 5 == 2) or (number % 5 == 3):
        print(number)