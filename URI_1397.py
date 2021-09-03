if __name__ == '__main__':
    while True:
        games_qty = int(input())
        if games_qty == 0:
            break
        player_1_wins = 0
        player_2_wins = 0
        for _ in range(games_qty):
            number_1, number_2 = map(int, input().split())
            player_1_wins += int(number_1 > number_2)
            player_2_wins += int(number_1 < number_2)
        print('{} {}'.format(player_1_wins, player_2_wins))
