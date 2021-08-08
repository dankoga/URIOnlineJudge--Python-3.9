input_n = int(input())
factorial_n = 1
for factor in range(2, input_n + 1):
    factorial_n *= factor
print(factorial_n)