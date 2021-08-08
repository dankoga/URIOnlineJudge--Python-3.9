POWER_26 = [1, 26, 676]

while True:
    try:
        col_number_26 = input()
    except EOFError:
        break

    if len(col_number_26) > 3:
        print('Essa coluna nao existe Tobias!')
    else:
        col_number_10 = sum([(ord(letter) - ord('A') + 1) * POWER_26[digit]
                             for digit, letter in enumerate(col_number_26[::-1])])
        if col_number_10 > 16384:
            print('Essa coluna nao existe Tobias!')
        else:
            print(col_number_10)
