bottle_empty, bottle_found, trade_rate = map(int, input().split())
bottle_empty += bottle_found

bottle_total = 0
bottle_full, bottle_empty = divmod(bottle_empty, trade_rate)
while bottle_full != 0:
    bottle_empty += bottle_full
    bottle_total += bottle_full
    bottle_full, bottle_empty = divmod(bottle_empty, trade_rate)
print(bottle_total)
