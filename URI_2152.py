DOOR_STATUS = ['fechou!', 'abriu!']

cases_qty = int(input())
for case in range(cases_qty):
    time_H, time_M, door = map(int, input().split())
    print('{:02d}:{:02d} - A porta {}'.format(time_H, time_M, DOOR_STATUS[door]))
