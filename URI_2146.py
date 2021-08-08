while True:
    try:
        password = int(input())
    except EOFError:
        break
    print(password - 1)
