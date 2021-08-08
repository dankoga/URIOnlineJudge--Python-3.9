LANGUAGE = {'esquerda': 'ingles',
            'direita':  'frances',
            'nenhuma':  'portugues',
            'as duas':  'caiu'}

while True:
    try:
        leg = input()
    except EOFError:
        break
    print(LANGUAGE[leg])
