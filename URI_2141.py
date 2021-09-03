from math import sqrt

SKILLS_TABLE = {'MightySwing':  [0, 270.00, 0.14,  0.00],
                'GiganticFist': [0, 560.00, 0.16,  0.00],
                'RainyDeath':   [0, 350.00, 0.20,  0.00],
                'Agilao':       [1, 200.00, 0.00,  8.00],
                'Agidyne':      [1, 320.00, 0.00, 12.00],
                'Bufula':       [1, 200.00, 0.00,  8.00],
                'Bufudyne':     [1, 320.00, 0.00, 12.00],
                'Megidola':     [1, 360.00, 0.00, 32.00],
                'Megidolaon':   [1, 420.00, 0.00, 60.00],
                'BlackViper':   [1, 440.00, 0.00, 64.00],
                'Tarukaja':     [2,   0.00, 0.00, 12.00, 0],
                'Rakukaja':     [2,   0.00, 0.00, 12.00, 1],
                'Tarunda':      [2,   0.00, 0.00, 12.00, 2],
                'Rakunda':      [2,   0.00, 0.00, 12.00, 3]}
# TYPE:     CODE:
# Physical  0
# Magical   1
# Support   2


EFFECTS_TABLE = [[0, [0.00, 0.00, 0.00, 0.25, 0.00, 0.00]],
                 [0, [0.00, 0.00, 0.00, 0.00, 0.00, 0.25]],
                 [1, [0.00, 0.00, 0.00, -0.25, 0.00, 0.00]],
                 [1, [0.00, 0.00, 0.00, 0.00, 0.00, -0.25]]]
# Effect   : [Target, Modifiers]
# Modifiers: [LV, HP, MP, ATK, MAG, DEF]


def create_player():
    p = dict()
    p['name'] = input()
    p['stats'] = list(map(float, input().split()))
    p['effects'] = [0.00] * 6
    return p


def damage(t, p, ps, a, d):
    attack = ps[a]['stats'][t + 3] + ps[a]['effects'][t + 3]
    defence = ps[d]['stats'][5] + ps[d]['effects'][5]
    level_dif = ps[a]['stats'][0] - ps[d]['stats'][0]
    return 5.00 * sqrt(attack / defence * p) * (1.00 + 0.1 * level_dif)


def match_end(ps, a, d):
    print('{} is dead.'.format(ps[d]['name']))
    stats = [s + e for s, e in zip(ps[a]['stats'], ps[a]['effects'])]
    print('{} HP: {:.2f}, MP: {:.2f}, ATK: {:.1f}, MAG: {:.1f}, DEF: {:.1f}'.format(ps[a]['name'], stats[1], stats[2],
                                                                                         stats[3], stats[4], stats[5]))


if __name__ == '__main__':
    players = [create_player(), create_player()]

    turn = 0
    while True:
        try:
            action = input()
        except EOFError:
            break

        attacker = turn % 2
        defender = (turn + 1) % 2

        if SKILLS_TABLE[action][0] == 2:
            if players[attacker]['stats'][2] >= SKILLS_TABLE[action][3]:
                players[attacker]['stats'][2] -= SKILLS_TABLE[action][3]
                e = SKILLS_TABLE[action][-1]
                target = (attacker + EFFECTS_TABLE[e][0]) % 2
                players[target]['effects'] = [p * e for p, e in zip(players[target]['stats'], EFFECTS_TABLE[e][1])]
        else:
            if players[attacker]['stats'][2] >= SKILLS_TABLE[action][3]:
                players[attacker]['stats'][2] -= SKILLS_TABLE[action][3]
                players[attacker]['stats'][1] -= players[attacker]['stats'][1] * SKILLS_TABLE[action][2]
                t = SKILLS_TABLE[action][0]
                power = SKILLS_TABLE[action][1]
                if t == 0:
                    players[attacker]['effects'] = [0.00] * 6
                players[defender]['stats'][1] -= damage(t, power, players, attacker, defender)
                players[defender]['effects'] = [0.00] * 6

        if players[defender]['stats'][1] <= 0.00:
            match_end(players, attacker, defender)
            break
        turn += 1
