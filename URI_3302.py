import sys

questions_qty = input()
for i, answer in enumerate(sys.stdin, 1):
    print('resposta {}: {}'.format(i, answer.strip()))
