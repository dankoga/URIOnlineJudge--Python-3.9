from math import sqrt

height_leak, rate_leak, rain_duration, observation_time, height_observed = map(float, input().split())

if height_observed < height_leak:
    print('{0:.9f} {0:.9f}'.format(height_observed))
else:
    a = rain_duration
    b = height_observed + rate_leak * (observation_time + rain_duration)
    c = rate_leak * height_leak
    delta = sqrt(b ** 2 - 4 * a * c)
    rate_rainfall = (b + delta)/(2*a)
    if height_observed > height_leak:
        print('{0:.9f} {0:.9f}'.format(rate_rainfall * rain_duration))
    else:
        print('{0:.9f} {1:.9f}'.format(height_observed, rate_rainfall * rain_duration))
