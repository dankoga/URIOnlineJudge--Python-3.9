beam_status = list(map(int, input().split()))
beam_position = sum([(i + 1) * beam_status[i] for i in range(4)])
print(beam_position)
