while True:
    try:
        expressions_qty = int(input())
    except EOFError:
        break

    expressions = []
    for expression in range(expressions_qty):
        expressions.append(input().replace('=', ' ').split())

    players_wrong = []
    for player in range(expressions_qty):
        name, index, operator = input().split()
        index = int(index) - 1
        if operator == 'I':
            a, b, c = map(int, expressions[index])
            if (a + b == c) or (a - b == c) or (a * b == c):
                players_wrong.append(name)
        else:
            expression_str = expressions[index][0] + operator + expressions[index][1] + '==' + expressions[index][2]
            if not eval(expression_str):
                players_wrong.append(name)

    if len(players_wrong) == expressions_qty:
        print('None Shall Pass!')
    elif len(players_wrong) == 0:
        print('You Shall All Pass!')
    else:
        players_wrong.sort()
        print(*players_wrong)
