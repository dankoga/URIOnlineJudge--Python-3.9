if __name__ == '__main__':
    A, B, C, D = map(int, input().split())

    # Trivial case, as A is a divisor of N and C is a multiple of N, A must be a divisor of C
    if C % A != 0:
        print(-1)
        exit(0)

    candidates = [C]
    for n in range(1, int(C ** 0.5) + 1):
        if C % n == 0:
            if n % A == 0:
                candidates.append(n)
            if (C // n) % A == 0:
                candidates.append(C // n)
    N = -1
    for n in sorted(candidates):
        if n % B != 0 and D % n != 0:
            N = n
            break
    print(N)
