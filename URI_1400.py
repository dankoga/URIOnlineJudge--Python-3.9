def should_clap(n):
    return int(n % 7 == 0 or any([d == '7' for d in str(n)]))


if __name__ == '__main__':
    while True:
        players_qty, player, clap = map(int, input().split())
        if players_qty == player == clap == 0:
            break

        if player == 1 or player == players_qty:
            period = [2 * (players_qty - 1)]
            periods = 1
        else:
            period = [2 * (players_qty - player), 2 * (player - 1)]
            periods = 2

        count = player
        clap_count = 0
        p = 0
        while True:
            clap_count += should_clap(count)
            if clap_count == clap:
                break
            count += period[p]
            p = (p + 1) % periods
        print(count)
