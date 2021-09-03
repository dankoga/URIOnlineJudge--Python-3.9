from math import gcd

if __name__ == '__main__':
    angle_int, angle_dec = map(int, input().split('.'))
    picture_angle_100 = 100 * angle_int + angle_dec
    print(36000 // gcd(36000, picture_angle_100))


#  A pizza pode ser considerada um polígono regular de n lados. Como cabe ao entregador provar a simetria, assumimos que
# n será o menor valor possível dado o ângulo de rotação entre as fotos.
# Se o entragador mostra a pizza em duas orientações, diferentes em um ângulo "a", ele prova que o ângulo máximo entre
# dois vértices é "a"? Não necessariamente. Mas ele prova que o MDC(360, a) é o ângulo máximo.
