input_size = int(input())
for input_line in range(input_size):
    input_A, input_B = map(int, input().split())
    if input_A == input_B:
        print(0)
        continue
    elif input_A < input_B:
        number_min = input_A + 1 + input_A % 2
        number_max = input_B - 1 - input_B % 2
    else:
        number_max = input_A - 1 - input_A % 2
        number_min = input_B + 1 + input_B % 2
    print('{}'.format((number_max - number_min + 2) * (number_min + number_max) // 4))