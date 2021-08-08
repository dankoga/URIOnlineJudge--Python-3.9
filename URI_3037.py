games_qty = int(input())
for games in range(games_qty):
    score, distance = map(int, input().split())
    score_player1 = score * distance
    score, distance = map(int, input().split())
    score_player1 += score * distance
    score, distance = map(int, input().split())
    score_player1 += score * distance

    score, distance = map(int, input().split())
    score_player2 = score * distance
    score, distance = map(int, input().split())
    score_player2 += score * distance
    score, distance = map(int, input().split())
    score_player2 += score * distance

    if score_player1 > score_player2:
        print('JOAO')
    else:
        print('MARIA')
