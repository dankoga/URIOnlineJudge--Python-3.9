laps, signs = map(int, input().split())
signs_total = laps * signs
print(' '.join([str((n * signs_total + 9) // 10) for n in range(1, 10)]))
