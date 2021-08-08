words_search_qty, rows_qty, cols_qty = map(int, input().split())

words_search_list = [input().lower() for w in range(words_search_qty)]

diagonals_list = [[] for w in range(rows_qty + cols_qty - 1)]
for r in range(rows_qty):
    row = input()
    for c in range(cols_qty):
        diagonals_list[rows_qty - 1 - r + c].append(row[cols_qty - 1 - c])
diagonals_string = [''.join(diagonal).lower() for diagonal in diagonals_list]

for word in words_search_list:
    word_found = False
    if (word in diagonals_string[rows_qty - 1]) or (word[::-1] in diagonals_string[rows_qty - 1]):
        word_found = True
        print('1 Palavra "{}" na diagonal secundaria'.format(word))
        continue

    for diagonal in diagonals_string[:rows_qty - 1]:
        if (word in diagonal) or (word[::-1] in diagonal):
            word_found = True
            print('3 Palavra "{}" abaixo da diagonal secundaria'.format(word))
            break

    for diagonal in diagonals_string[rows_qty:]:
        if (word in diagonal) or (word[::-1] in diagonal):
            word_found = True
            print('2 Palavra "{}" acima da diagonal secundaria'.format(word))
            break

    if not word_found:
        print('4 Palavra "{}" inexistente'.format(word))
