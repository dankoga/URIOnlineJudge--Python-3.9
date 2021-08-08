while True:
    try:
        year = int(input())
    except EOFError:
        break
    print((year - 1)//100 + 1)
