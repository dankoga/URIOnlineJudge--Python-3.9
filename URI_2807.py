from math import sqrt, pow


def fibonacci(n):
    sqrt5 = sqrt(5)
    phi = (1 + sqrt5)/2
    return int(pow(phi, n)/sqrt5 + 0.5)


sequence_length = int(input())
sequence = [fibonacci(i) for i in range(sequence_length, 0, -1)]
print(' '.join(str(element) for element in sequence))
