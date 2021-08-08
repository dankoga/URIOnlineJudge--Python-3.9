age_H, age_Z, age_L = map(int, input().split())
nephews = [[age_H, 'huguinho'],
           [age_Z, 'zezinho'],
           [age_L, 'luisinho']]
nephews.sort()
print(nephews[1][1])
