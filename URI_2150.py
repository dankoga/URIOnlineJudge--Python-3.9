while True:
    try:
        vowels = input()
        text = input()
    except EOFError:
        break
    print(sum([text.count(v) for v in vowels]))
