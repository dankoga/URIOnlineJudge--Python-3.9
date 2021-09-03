if __name__ == '__main__':
    while True:
        seasons_qty, ep_duration = map(int, input().split())
        if seasons_qty == ep_duration == -1:
            break
        seasons_ep = list(map(int, input().split()))
        print(ep_duration * sum([n * s for n, s in enumerate(seasons_ep[::-1], start=1)]))
