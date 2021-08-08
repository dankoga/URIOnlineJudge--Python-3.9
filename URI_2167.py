from operator import sub

datapoints_qty = int(input())
speeds = list(map(int, input().split()))
if datapoints_qty < 2:
    print(0)
else:
    accelerations = list(map(sub, speeds[1:], speeds[:-1]))
    accelerations_negative = list(map(lambda x: x < 0, accelerations))
    try:
        engine_failure = accelerations_negative.index(True)
        print(engine_failure + 2)
    except ValueError:
        print(0)
