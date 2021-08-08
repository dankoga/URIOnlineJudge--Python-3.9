import sys


tests_qty = input()
for text in sys.stdin:
    print(''.join([word[0] for word in text.split()]))
