if __name__ == '__main__':
    while True:
        loop_length = int(input())
        if loop_length == 0:
            break
        loop = list(map(int, input().split()))
        loop += loop[:2]
        delta1 = [a - b for a, b in zip(loop[1:loop_length+1], loop[0:loop_length])]
        delta2 = [a - b for a, b in zip(loop[2:loop_length+2], loop[1:loop_length+1])]
        peaks = sum([d1*d2 < 0 for d1, d2 in zip(delta1, delta2)])
        print(peaks)
