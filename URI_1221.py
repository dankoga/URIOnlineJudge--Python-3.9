def square_range(begin, end):
    i = begin
    while i*i <= end:
        yield i
        i += 6


def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    for divisor in square_range(5, n):
        if n % divisor == 0 or n % (divisor + 2) == 0:
            return False
    return True


tests_qty = int(input())
for t in range(tests_qty):
    number = int(input())
    if is_prime(number):
        print('Prime')
    else:
        print('Not Prime')
