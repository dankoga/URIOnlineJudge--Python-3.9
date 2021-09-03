if __name__ == '__main__':
    while True:
        queries_qty = int(input())
        if queries_qty == 0:
            break
        center = list(map(int, input().split()))
        for _ in range(queries_qty):
            position = list(map(int, input().split()))
            if position[0] == center[0] or position[1] == center[1]:
                print('divisa')
                continue

            if position[1] > center[1]:
                print('N', end='')
            else:
                print('S', end='')
            if position[0] > center[0]:
                print('E')
            else:
                print('O')
