# Result was calculated by product of sum reduction using the truth table below in an
# online calculator.
# w: player1 won
# c: player1 cheated
# d: player2 doubted
# w c d  R
# 0 0 0  0
# 0 0 1  1
# 0 1 0  1
# 0 1 1  0
# 1 0 0  1
# 1 0 1  1
# 1 1 0  1
# 1 1 1  0


player1_parity, player1_hand, player2_hand, player1_cheat, player2_doubt = map(int, input().split())
player1_won = not((player1_hand + player2_hand) % 2 == player1_parity)
result = ((not player1_cheat) or (not player2_doubt)) and (player1_won or player1_cheat or player2_doubt)
if result:
    print('Jogador 1 ganha!')
else:
    print('Jogador 2 ganha!')
