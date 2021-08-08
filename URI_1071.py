import sys

input_A = int(input())
input_B = int(input())
if input_A > input_B:
    number_min = input_B
    number_max = input_A
elif input_A < input_B:
    number_min = input_A
    number_max = input_B
else:
    print(0)
    sys.exit(0)

number_min += 1 + number_min % 2
number_max -= 1 + number_max % 2
odd_qty = (number_max - number_min)//2 + 1

print('{}'.format(odd_qty * (number_max + number_min)//2 ))
