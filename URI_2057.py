time_departure, travel_time, TZ_offset = map(int, input().split())
print((time_departure + travel_time + TZ_offset) % 24)
