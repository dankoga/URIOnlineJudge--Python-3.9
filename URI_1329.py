if __name__ == '__main__':
    while True:
        games_qty = int(input())
        if games_qty == 0:
            break
        john_wins = sum(map(int, input().split()))
        print('Mary won {} times and John won {} times'.format(games_qty - john_wins, john_wins))
