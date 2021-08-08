VITAMIN_TABLE = {'suco de laranja': 120,
                 'morango fresco':   85,
                 'mamao':            85,
                 'goiaba vermelha':  70,
                 'manga':            56,
                 'laranja':          50,
                 'brocolis':         34}

food_qty = int(input())
while food_qty > 0:
    vitamin_total = 0
    for food in range(food_qty):
        food_line = input().split()
        portions = int(food_line[0])
        product = ' '.join(word for word in food_line[1:])
        vitamin_total += portions * VITAMIN_TABLE[product]
    if vitamin_total < 110:
        print('Mais {} mg'.format(110 - vitamin_total))
    elif vitamin_total > 130:
        print('Menos {} mg'.format(vitamin_total - 130))
    else:
        print('{} mg'.format(vitamin_total))

    food_qty = int(input())
