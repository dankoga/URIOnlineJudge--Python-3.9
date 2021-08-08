vitorias_inter = 0
vitorias_gremio = 0
jogos = 0

opcao = '1'
while opcao == '1':
    gols_inter, gols_gremio = map(int, input().split())
    if gols_inter > gols_gremio:
        vitorias_inter += 1
    elif gols_inter < gols_gremio:
        vitorias_gremio += 1
    jogos += 1
    opcao = input('Novo grenal (1-sim 2-nao)\n')

print('{} grenais'.format(jogos))
print('Inter:{}'.format(vitorias_inter))
print('Gremio:{}'.format(vitorias_gremio))
print('Empates:{}'.format(jogos - vitorias_inter - vitorias_gremio))
if vitorias_inter > vitorias_gremio:
    print('Inter venceu mais')
elif vitorias_inter < vitorias_gremio:
    print('Gremio venceu mais')
else:
    print('Nao houve vencedor')
