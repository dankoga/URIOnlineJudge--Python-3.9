numbers_positive = 0
while True:
    try:
        number = float(input())
        numbers_positive += (number >= 0.0)
    except:
        break
print('{} valores positivos'.format(numbers_positive))