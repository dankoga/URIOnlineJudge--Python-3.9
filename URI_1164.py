from math import sqrt

input_size = int(input())
for input_line in range(input_size):
    number = int(input())
    number_sqrt = int(sqrt(number))
    if number_sqrt * number_sqrt == number:
        divisor_sum = 1 - number_sqrt
    else:
        divisor_sum = 1
    for candidate in range(2, number_sqrt + 1):
        if number % candidate == 0:
            divisor_sum += candidate + number / candidate

    if divisor_sum == number:
        print('{} eh perfeito'.format(number))
    else:
        print('{} nao eh perfeito'.format(number))
