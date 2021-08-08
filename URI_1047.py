time_begin_H, time_begin_M, time_end_H, time_end_M = list(map(int, input().split()))
time_begin = 60 * time_begin_H + time_begin_M
time_end = 60 * time_end_H + time_end_M
if time_end <= time_begin:
    time_end += 60 * 24
time_delta_H, time_delta_M = divmod(time_end - time_begin, 60)
print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(time_delta_H, time_delta_M))