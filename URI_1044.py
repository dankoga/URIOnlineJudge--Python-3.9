number_A, number_B = map(int, input().split())

if number_A > number_B:
    if number_A % number_B == 0:
        print( "Sao Multiplos")
    else:
        print("Nao sao Multiplos")
else:
    if number_B % number_A == 0:
        print( "Sao Multiplos")
    else:
        print("Nao sao Multiplos")