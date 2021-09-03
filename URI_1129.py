if __name__ == '__main__':
    while True:
        questions_qty = int(input())
        if questions_qty == 0:
            break
        for _ in range(questions_qty):
            answer = [chr(i + 65) for i, a in enumerate(map(int, input().split())) if a <= 127]
            if len(answer) == 1:
                print(*answer)
            else:
                print('*')
