entourage = {'A': 0,
             'E': 0,
             'H': 0,
             'M': 0,
             'X': 0}

people_qty = int(input())
for people in range(people_qty):
    name_race = input()
    entourage[name_race[-1]] += 1
print('{} Hobbit(s)'.format(entourage['X']))
print('{} Humano(s)'.format(entourage['H']))
print('{} Elfo(s)'.format(entourage['E']))
print('{} Anao(s)'.format(entourage['A']))
print('{} Mago(s)'.format(entourage['M']))
