import sys


tests_qty = input()
for word in sys.stdin:
    word = word.rstrip()
    if len(word) > 3:
        print(3)
    else:
        hits = int(word[0] == 'o') + int(word[1] == 'n') + int(word[2] == 'e')
        if hits >= 2:
            print(1)
        else:
            print(2)
