sides = list(map(int, input().split()))
sides.sort()
if sides[0] + sides[1] <= sides[2]:
    print('Invalido')
else:
    equal_sides = int(sides[0] == sides[1]) + int(sides[0] == sides[2]) + int(sides[1] == sides[2])
    if equal_sides == 0:
        print('Valido-Escaleno')
    elif equal_sides == 1:
        print('Valido-Isoceles')
    else:
        print('Valido-Equilatero')
    if sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2:
        print('Retangulo: S')
    else:
        print('Retangulo: N')
