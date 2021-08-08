players_qty = int(input())

service_total = [0, 0]
block_total = [0, 0]
attack_total = [0, 0]
for player in range(players_qty):
    player_name = input()

    player_actions = list(map(int, input().split()))
    service_total[0] += player_actions[0]
    block_total[0] += player_actions[1]
    attack_total[0] += player_actions[2]

    player_actions = list(map(int, input().split()))
    service_total[1] += player_actions[0]
    block_total[1] += player_actions[1]
    attack_total[1] += player_actions[2]

print('Pontos de Saque: {:.2f} %.'.format(service_total[1] / service_total[0] * 100.0))
print('Pontos de Bloqueio: {:.2f} %.'.format(block_total[1] / block_total[0] * 100.0))
print('Pontos de Ataque: {:.2f} %.'.format(attack_total[1] / attack_total[0] * 100.0))
