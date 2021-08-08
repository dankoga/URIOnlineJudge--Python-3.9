from math import sqrt

par_A, par_B, par_C = map(float, input().split())

if par_A == 0:
    print("Impossivel calcular")
else:
    delta2 = par_B ** 2 - 4.0 * par_A * par_C
    if delta2 < 0 :
        print("Impossivel calcular")
    else:
        delta = sqrt(delta2)
        print("R1 = {:.5f}".format((-par_B + delta) / (2.0 * par_A)))
        print("R2 = {:.5f}".format((-par_B - delta) / (2.0 * par_A)))
