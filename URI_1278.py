first_test = True
sentences_qty = int(input())
while sentences_qty > 0:
    if first_test:
        first_test = False
    else:
        print()

    sentences_list = [' '.join(input().split()) for s in range(sentences_qty)]
    field_width = max(map(len, sentences_list))
    format_string = '{:>' + str(field_width) + 's}'
    for sentence in sentences_list:
        print(format_string.format(sentence))

    sentences_qty = int(input())
