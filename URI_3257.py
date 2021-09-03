if __name__ == '__main__':
    seedlings_qty = input()
    seedlings_maturing_time = sorted(list(map(int, input().split())), reverse=True)
    print(max([t + i for i, t in enumerate(seedlings_maturing_time, start=1)]) + 1)
