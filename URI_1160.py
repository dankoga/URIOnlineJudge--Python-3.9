from math import floor

input_size = int(input())
for input_line in range(input_size):
    population_A, population_B, rate_A, rate_B = map(float, input().split())
    rate_A = 1.0 + rate_A / 100.0
    rate_B = 1.0 + rate_B / 100.0
    years = 0
    while (population_A <= population_B) and (years <= 101):
        population_A = floor(population_A * rate_A)
        population_B = floor(population_B * rate_B)
        years += 1
    if years > 100:
        print('Mais de 1 seculo.')
    else:
        print('{} anos.'.format(years))
