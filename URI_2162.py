from operator import sub, mul

datapoints_qty = int(input())
datapoints = list(map(int, input().split()))
is_Nlogony_like = True
if datapoints_qty < 2:
    print(0)
elif datapoints_qty == 2:
    is_Nlogony_like = (datapoints[0] != datapoints[1])
else:
    height_difference = list(map(sub, datapoints[:-1], datapoints[1:]))
    consecutive_signals = list(map(mul, height_difference[:-1], height_difference[1:]))
    alternating_signals = list(map(lambda x: x < 0, consecutive_signals))
    is_Nlogony_like = all(alternating_signals)

print(int(is_Nlogony_like))
