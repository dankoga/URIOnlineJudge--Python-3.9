forecast_days = int(input())
umbrellas_owned = [0, 0]
umbrellas_bought = [0, 0]
for day in range(forecast_days):
    forecast = input().split()
    if forecast[0] == 'chuva':
        if umbrellas_owned[0] > 0:
            umbrellas_owned[0] -= 1
        else:
            umbrellas_bought[0] += 1
        umbrellas_owned[1] += 1
    if forecast[1] == 'chuva':
        if umbrellas_owned[1] > 0:
            umbrellas_owned[1] -= 1
        else:
            umbrellas_bought[1] += 1
        umbrellas_owned[0] += 1
print('{} {}'.format(umbrellas_bought[0], umbrellas_bought[1]))
