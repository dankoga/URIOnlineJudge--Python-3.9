alcohol_qty = 0
gasoline_qty = 0
diesel_qty = 0
while True:
    option = int(input())
    if option == 4:
        break
    elif option == 1:
        alcohol_qty += 1
    elif option == 2:
        gasoline_qty += 1
    elif option == 3:
        diesel_qty += 1

print('MUITO OBRIGADO')
print('Alcool: {}'.format(alcohol_qty))
print('Gasolina: {}'. format(gasoline_qty))
print('Diesel: {}'.format(diesel_qty))
