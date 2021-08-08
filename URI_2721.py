REINDEERS = ['Dasher', 'Dancer', 'Prancer', 'Vixen', 'Comet', 'Cupid', 'Donner', 'Blitzen', 'Rudolph']

snowballs = sum(map(int, input().split()))
print(REINDEERS[(snowballs - 1) % 9])
