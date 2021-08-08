numbers_qty = int(input())
numbers_list = map(int, input().split())
multiples_2 = 0
multiples_3 = 0
multiples_4 = 0
multiples_5 = 0
for number in numbers_list:
    if number % 2 == 0:
        multiples_2 += 1
    if number % 3 == 0:
        multiples_3 += 1
    if number % 4 == 0:
        multiples_4 += 1
    if number % 5 == 0:
        multiples_5 += 1
print('{} Multiplo(s) de 2'.format(multiples_2))
print('{} Multiplo(s) de 3'.format(multiples_3))
print('{} Multiplo(s) de 4'.format(multiples_4))
print('{} Multiplo(s) de 5'.format(multiples_5))
