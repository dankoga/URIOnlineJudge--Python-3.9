def is_prime(n):
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    for p in range(5, int(n ** 0.5) + 1, 6):
        if n % p == 0 or n % (p + 2) == 0:
            return False
    return True


if __name__ == '__main__':
    mass = int(input())
    mass += 1 - (mass % 2)

    velocity = 0
    factors_qty = 0
    while factors_qty < 10:
        if is_prime(mass):
            velocity += mass
            factors_qty += 1
        mass += 2

    print('{} km/h'.format(velocity))
    print('{} h / {} d'.format(60000000 // velocity, 2500000 // velocity))
