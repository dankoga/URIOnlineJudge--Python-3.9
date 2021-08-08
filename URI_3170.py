balls_qty = int(input())
branches_qty = int(input())

if balls_qty < branches_qty // 2:
    print('Faltam {} bolinha(s)'.format(branches_qty // 2 - balls_qty))
else:
    print('Amelia tem todas bolinhas!')
