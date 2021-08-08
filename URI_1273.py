first_test = True
words_qty = int(input())
while words_qty > 0:
    if first_test:
        first_test = False
    else:
        print()

    words_list = [input() for w in range(words_qty)]
    field_width = max(map(len, words_list))
    format_string = '{:>' + str(field_width) + 's}'
    for word in words_list:
        print(format_string.format(word))

    words_qty = int(input())
