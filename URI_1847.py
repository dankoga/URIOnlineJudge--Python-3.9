temperatures = list(map(int, input().split()))
temperatures_delta = [temperatures[1] - temperatures[0], temperatures[2] - temperatures[1]]
if temperatures_delta[0] > 0:
    if temperatures_delta[0] > temperatures_delta[1]:
        print(':(')
    else:
        print(':)')
else:
    if temperatures_delta[0] < temperatures_delta[1]:
        print(':)')
    else:
        print(':(')
