import sys


def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    factor = 5
    while factor * factor <= n:
        if n % factor == 0 or n % (factor + 2) == 0:
            return False
        factor += 6

    return True


def is_digital_prime(n):
    while n > 0:
        n, digit = divmod(n, 10)
        if digit in [0, 1, 4, 6, 8, 9]:
            return False
    return True


if __name__ == '__main__':
    for input_line in sys.stdin:
        number = int(input_line)
        if is_prime(number):
            if is_digital_prime(number):
                print('Super')
            else:
                print('Primo')
        else:
            print('Nada')
