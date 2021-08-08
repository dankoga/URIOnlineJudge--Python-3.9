processes_qty = int(input())
cpu_use = 0.0
for process in range(processes_qty):
    cost, period = map(int, input().split())
    cpu_use += cost/period
if cpu_use > 1:
    print('FAIL')
else:
    print('OK')
