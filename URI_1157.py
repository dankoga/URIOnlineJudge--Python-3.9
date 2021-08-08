number = int(input())
for candidate in range(1, number//2 + 1):
    if number % candidate == 0:
        print(candidate)
print(number)