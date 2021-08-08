while True:
    try:
        letters_qty = int(input())
    except EOFError:
        break
    for letter in range(letters_qty):
        code = input().split()
        print(chr(3 * (len(code) - 1) + len(code[-1]) - 1 + ord('a')))
