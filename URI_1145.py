columns, number_max = map(int, input().split())

for number in range(1,number_max + 1):
    if number % columns == 0:
        print(number)
    else:
        print(number, end=' ')
