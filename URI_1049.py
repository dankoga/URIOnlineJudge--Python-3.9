class_1 = input()
class_2 = input()
class_3 = input()
if class_1 == 'vertebrado':
    if class_2 == 'ave':
        if class_3 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if class_3 == 'onivoro':
            print('homem')
        else:
            print('vaca')
else:
    if class_2 == 'inseto':
        if class_3 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if class_3 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')