import sys

if __name__ == '__main__':
    for input_line in sys.stdin:
        a, b = map(int, input_line.split())
        print(a ^ b)
