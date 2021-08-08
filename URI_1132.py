number_A = int(input())
number_B = int(input())
if number_A > number_B:
    buffer = number_A
    number_A = number_B
    number_B = buffer

total = (number_B - number_A + 1) * (number_A + number_B) // 2

if number_A % 13 != 0:
    number_A -= number_A % 13 - 13
number_B -= number_B % 13

total -= ((number_B - number_A)//13 + 1) * (number_A + number_B) // 2
print(total)
