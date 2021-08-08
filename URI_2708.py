tourists_away = 0
jeeps_away = 0
while True:
    operation = list(input().split())
    if operation[0] == 'SALIDA':
        jeeps_away += 1
        tourists_away += int(operation[1])
    elif operation[0] == 'VUELTA':
        jeeps_away -= 1
        tourists_away -= int(operation[1])
    else:
        break
print(tourists_away)
print(jeeps_away)
