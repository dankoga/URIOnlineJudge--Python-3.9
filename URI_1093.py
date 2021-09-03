import math

while True:
    hp1, hp2, attack, damage = map(float, input().split())
    if hp1 == 0:
        break
    hp1 = math.ceil(hp1 / damage)
    hp2 = math.ceil(hp2 / damage)

    if attack == 3:
        win_rate = 100.0 * hp1 / (hp1 + hp2)
    else:
        prob = 6.0 / attack - 1.0
        win_rate = 100.0 * (1.0 - pow(prob, hp1)) / (1.0 - pow(prob, hp1 + hp2))
    print('{:.1f}'.format(win_rate))
