while True:
    try:
        alphabet = input()
    except EOFError:
        break

    message_length = input()
    message = list(map(int, input().split()))
    print(''.join(alphabet[i - 1] for i in message))
