measurements_qty = int(input())
for m in range(measurements_qty):
    energy = int(input())
    if energy > 8000:
        print('Mais de 8000!')
    else:
        print('Inseto!')
