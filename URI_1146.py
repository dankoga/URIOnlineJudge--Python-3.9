number_max = int(input())
while number_max > 0:
    numbers_str = ' '.join(str(n) for n in range(1, number_max + 1))
    print(numbers_str)
    number_max = int(input())
