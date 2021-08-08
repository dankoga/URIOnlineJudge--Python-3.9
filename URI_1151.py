fibonacci_n = int(input())

if fibonacci_n == 1:
    print(0)
else:
    fibonacci_seq = [0] * fibonacci_n
    fibonacci_seq[1] = 1
    for n in range(2, fibonacci_n):
        fibonacci_seq[n] = fibonacci_seq[n - 1] + fibonacci_seq[n - 2]
    print(' '.join(str(n) for n in fibonacci_seq))