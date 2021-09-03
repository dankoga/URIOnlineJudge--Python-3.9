import sys

if __name__ == '__main__':
    C = 0.69282032302
    for l in sys.stdin:
        print('{:.2f}'.format(C * float(l) ** 2))
