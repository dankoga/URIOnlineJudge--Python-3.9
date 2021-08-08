time_remaining = int(input())
time_A, time_B = map(int, input().split())
if time_A + time_B > time_remaining:
    print('Deixa para amanha!')
else:
    print('Farei hoje!')
