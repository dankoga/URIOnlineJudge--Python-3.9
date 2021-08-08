QUADRANT = ["Q3",
            "Eixo X",
            "Q2",
            "Eixo Y",
            "Origem",
            "Eixo Y",
            "Q4",
            "Eixo X",
            "Q1"]

coord_X, coord_Y = map(float, input().split())
if coord_X != 0:
    index_X = 3*(coord_X/abs(coord_X) + 1)
else:
    index_X = 3
if coord_Y != 0:
    index_Y = coord_Y/abs(coord_Y) + 1
else:
    index_Y = 1

print(QUADRANT[int(index_X + index_Y)])