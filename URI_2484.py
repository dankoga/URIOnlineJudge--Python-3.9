while True:
    try:
        word = input()
    except EOFError:
        break
    print(' '.join(word))
    for i in range(1, len(word)):
        print(' ' * i + ' '.join(word[:(-i)]))
    print()