sides = list(map(float, input().split()))
sides.sort()

if sides[0] + sides[1] > sides[2]:
    sides2 = [side ** 2 for side in sides]
    if sides2[0] + sides2[1] < sides2[2]:
        print("TRIANGULO OBTUSANGULO")
    elif sides2[0] + sides2[1] > sides2[2]:
        print("TRIANGULO ACUTANGULO")
    else:
        print("TRIANGULO RETANGULO")

    equality = 0
    for s1 in range(0,3):
        for s2 in range(s1+1,3):
            if sides[s1] == sides[s2]:
                equality += 1
    if equality == 3:
        print("TRIANGULO EQUILATERO")
    elif equality == 1:
        print("TRIANGULO ISOSCELES")
else:
    print("NAO FORMA TRIANGULO")
