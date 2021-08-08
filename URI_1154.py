total_age = 0.0
total_people = 0.0
while True:
    age = float(input())
    if age < 0:
        break
    total_age += age
    total_people += 1

print('{:.2f}'.format(total_age / total_people))