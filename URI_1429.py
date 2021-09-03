ACM_TO_DEC = [1, 2, 6 , 24, 120]

if __name__ == '__main__':
    while True:
        acm_number = input()
        if acm_number == '0':
            break

        print(sum(int(digit) * ACM_TO_DEC[i] for i, digit in enumerate(acm_number[::-1])))
