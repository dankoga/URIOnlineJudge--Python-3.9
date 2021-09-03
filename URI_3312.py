if __name__ == '__main__':
    numbers_qty = int(input())
    numbers_list = list(map(int, input().split()))
    biggest_number = max(numbers_list)

    is_prime = [True] * (numbers_qty + 1)
    is_prime[0:2] = [False] * 2
    is_prime[4::2] = [False] * len(is_prime[4::2])
    is_prime[9::3] = [False] * len(is_prime[9::3])
    for p in range(5, int(biggest_number ** 0.5 + 1), 2):
        if is_prime[p]:
            is_prime[p * p::p] = [False] * len(is_prime[p * p::p])
    biggest_prime = max([p for p, is_p in enumerate(is_prime) if is_p])

    factorial = [1]
    for f in range(1, biggest_prime + 1):
        factorial.append(factorial[-1] * f)

    for n in numbers_list:
        if is_prime[n]:
            print('{}! = {}'.format(n, factorial[n]))
