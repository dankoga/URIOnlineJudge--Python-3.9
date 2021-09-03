import sys

if __name__ == '__main__':
    ones_count = 0
    for binary_number in sys.stdin:
        ones_count += sum([int(d == '1') for d in binary_number])
        if binary_number.rstrip()[-1] == '#':
            if ones_count % 17 == 0:
                print('YES')
            else:
                print('NO')
            ones_count = 0

# Por algum motivo, todos multiplos de 131071 (2^17 - 1) possuem quantidades de dígitos 1 divisível por 17...
