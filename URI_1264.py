import sys

DIGITS = {'0':  0, '1':  1, '2':  2, '3':  3, '4':  4, '5':  5, '6':  6, '7':  7, '8':  8,  '9': 9,
          'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
          'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
          'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35, 'a': 36, 'b': 37, 'c': 38, 'd': 39,
          'e': 40, 'f': 41, 'g': 42, 'h': 43, 'i': 44, 'j': 45, 'k': 46, 'l': 47, 'm': 48, 'n': 49,
          'o': 50, 'p': 51, 'q': 52, 'r': 53, 's': 54, 't': 55, 'u': 56, 'v': 57, 'w': 58, 'x': 59,
          'y': 60, 'z': 61}

for input_line in sys.stdin:
    number = input_line.rstrip().lstrip('-')
    digit_sum = sum([DIGITS[d] for d in number])
    base_min = max(2, DIGITS[max(number)] + 1)
    for base in range(base_min, 63):
        if digit_sum % (base - 1) == 0:
            print(base)
            break
    else:
        print('such number is impossible!')


 # R is a number is base N, so:
 #  R = f0*N^0 + f1*N^1 + f2*N^2 + f3*N^3 + ...
 #  R%(N-1) = (f0*N^0 + f1*N^1 + f2*N^2 + f3*N^3 + ...)%(N-1)
 #
 # Using (a+b)%n = (a%n + b%n)%n:
 #  R%(N-1) = ((f0*N^0)%(N-1) + (f1*N^1)%(N-1) + (f2*N^2)%(N-1) + ...)%(N-1)
 #
 # Using (a*b)%n = ((a%n)*(b%n))%n and (N^i)%(N-1) = 1
 #  R%(N-1) = ((f0*N^0)%(N-1) + (f1*N^1)%(N-1) + (f2*N^2)%(N-1) + ...)%(N-1)
 #  R%(N-1) = (f0%(N-1) + f1%(N-1) + f2%(N-1) + ...)%(N-1)
 #
 #  R%(N-1) = (f0 + f1 + f2 + ...)%(N-1)
