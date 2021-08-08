QUADRANTS = ['terceiro',
             'null',
             'segundo',
             'null',
             'null',
             'null',
             'quarto',
             'null',
             'primeiro']

while True:
    coord_X, coord_Y = map(int, input().split())
    if coord_X * coord_Y == 0:
        break

    index_X = 3 * (coord_X // abs(coord_X) + 1)
    index_Y = coord_Y // abs(coord_Y) + 1
    print(QUADRANTS[index_X + index_Y])
