if __name__ == '__main__':
    cases_qty = int(input())
    for c in range(1, cases_qty + 1):
        players = list(map(int, input().split()))
        print('Case {}: {}'.format(c, players[players[0] // 2 + 1]))
