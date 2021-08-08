input_size = int(input())
for input_line in range(input_size):
    number = int(input())
    if (number != 2) and (number % 2 == 0):
        number_is_prime = False
    else:
        number_is_prime = True

    candidate = 3
    while number_is_prime and (candidate * candidate <= number):
        if number % candidate == 0:
            number_is_prime = False
        candidate += 2

    if number_is_prime:
        print('{} eh primo'.format(number))
    else:
        print('{} nao eh primo'.format(number))
