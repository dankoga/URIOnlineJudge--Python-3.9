instance = 1
while True:
    signature = input()
    if signature == '0':
        break
    panel = input()
    if instance > 1:
        print()
    print('Instancia {}'.format(instance))
    if signature in panel:
        print('verdadeira')
    else:
        print('falsa')
    instance += 1
