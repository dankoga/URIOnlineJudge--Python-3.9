if __name__ == '__main__':
    while True:
        if input() == '0':
            break
        suspects = list(map(int, input().split()))
        suspects_sorted = sorted(enumerate(suspects, start=1), key=lambda x: -x[1])
        print(suspects_sorted[1][0])
