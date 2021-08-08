children_qty = int(input())
toy_car = 0
for child in range(children_qty):
    name_sex = input()
    if name_sex[-1] == 'M':
        toy_car += 1
print('{} carrinhos\n{} bonecas'.format(toy_car, children_qty - toy_car))
