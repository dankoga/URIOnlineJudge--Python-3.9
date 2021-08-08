from math import log2


while True:
    try:
        number = float(input())
    except EOFError:
        break
    print('{:.0f}'.format(log2(number)))
