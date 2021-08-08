import sys

LETTER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz'
NUMBER = '22233344455566677778889999' + '22233344455566677778889999'

for telephone in sys.stdin:
    digits = ''.join([d for d in telephone if d.isalnum() or d in '#*'])
    print(digits.translate(digits.maketrans(LETTER, NUMBER)))
