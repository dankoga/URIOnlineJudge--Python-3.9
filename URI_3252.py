import sys

pool_size, years = map(int, sys.stdin.readline().split())
if pool_size == 1:
    print(sys.stdin.readline().split()[0])
    exit(0)

moose_data = [tuple(map(int, line.split())) for line in sys.stdin]
karl_data = moose_data[0]
moose_data.sort()
weaker_moose = 0
for m in range(len(moose_data)):
    weaker_moose += int(moose_data[m][1] < karl_data[1])
    if weaker_moose >= pool_size - 1 and moose_data[m][0] >= karl_data[0]:
        print(moose_data[m][0])
        break
else:
    print('unknown')
