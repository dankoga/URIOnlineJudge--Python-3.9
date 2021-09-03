import sys

if __name__ == '__main__':
    for data in sys.stdin:
        b_int = [int(d) for d in '{:032b}'.format(int(data, 16))[::-1]]
        b_parity = b_int[:5]
        b_message = b_int[5:]
        b_int = b_parity[0:2] + [b_message[0]] + \
                [b_parity[2]] + b_message[1:4] + \
                [b_parity[3]] + b_message[4:11] + \
                [b_parity[4]] + b_message[11:]
        parity = [0] * 5
        for i in range(1, 22):
            if i & 1:
                parity[0] ^= b_int[i - 1]
            if i & 2:
                parity[1] ^= b_int[i - 1]
            if i & 4:
                parity[2] ^= b_int[i - 1]
            if i & 8:
                parity[3] ^= b_int[i - 1]
            if i & 16:
                parity[4] ^= b_int[i - 1]
        error_position = sum([int(parity[i]) * 2 ** i for i in range(5)])
        if error_position > 0 :
            b_int[error_position - 1] ^= 1
        b_message = [b for d, b in enumerate(b_int) if d not in [0,1, 3, 7, 15]]
        number = sum([b * 2 ** i for i, b in enumerate(b_message)])
        print('{:x}'.format(number))
