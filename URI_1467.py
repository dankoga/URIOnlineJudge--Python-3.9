import sys

GAME_TABLE = [[['*', 'C'], ['B', 'A']],
              [['A', 'B'], ['C', '*']]]

if __name__ == '__main__':
    for input_line in sys.stdin:
        a, b, c = map(int, input_line.split())
        print(GAME_TABLE[a][b][c])
