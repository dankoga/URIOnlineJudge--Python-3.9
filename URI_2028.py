case_number = 1
while True:
    try:
        element_max = int(input())
    except EOFError:
        break

    if element_max > 0:
        print('Caso {}: {} numeros'.format(case_number, (element_max * (element_max + 1)) // 2 + 1))
        print('0' + ''.join(element * (' ' + str(element)) for element in range(1, element_max + 1)))
        print()
    else:
        print('Caso {}: 1 numero'.format(case_number))
        print('0')
        print()
    case_number += 1
