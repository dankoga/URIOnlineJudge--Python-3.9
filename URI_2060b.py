numbers_qty = int(input())
numbers_list = list(map(int, input().split()))

mod_2 = map(lambda x: int(x % 2 == 0), numbers_list)
mod_3 = map(lambda x: int(x % 3 == 0), numbers_list)
mod_4 = map(lambda x: int(x % 4) == 0, numbers_list)
mod_5 = map(lambda x: int(x % 5) == 0, numbers_list)

print('{} Multiplo(s) de 2'.format(sum(mod_2)))
print('{} Multiplo(s) de 3'.format(sum(mod_3)))
print('{} Multiplo(s) de 4'.format(sum(mod_4)))
print('{} Multiplo(s) de 5'.format(sum(mod_5)))
