def is_prime(number):
    if number <= 3:
        return number > 1
    if number % 2 == 0 or number % 3 == 0:
        return False
    divisor = 5
    while divisor * divisor <= number:
        if number % divisor == 0 or number % (divisor + 2) == 0:
            return False
        divisor += 6
    return True


while True:
    try:
        coins_qty = int(input())
    except EOFError:
        break
    coin_holder = []
    for coin in range(coins_qty):
        coin_holder.append(int(input()))
    skip = int(input())
    if is_prime(sum(coin_holder[::-skip])):
        print('You’re a coastal aircraft, Robbie, a large silver aircraft.')
    else:
        print('Bad boy! I’ll hit you.')
