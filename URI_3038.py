import sys

KEY_1 = '@&!*#'
KEY_2 = 'aeiou'

for line in sys.stdin:
    print(line.rstrip().translate(line.maketrans(KEY_1, KEY_2)))
