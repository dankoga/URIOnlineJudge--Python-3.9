time_begin, time_end = list(map(int, input().split()))
if time_end <= time_begin:
    time_end += 24
print("O JOGO DUROU {} HORA(S)".format(time_end - time_begin))
