sides = list(map(int, input().split()))
sides.sort()
if (sides[0] + sides[1] > sides[2]) or (sides[1] + sides[2] > sides[3]):
    print('S')
else:
    print('N')
