while True:
    try:
        words_list = list(input().lower().split())
    except EOFError:
        break
    alliteration_counter = 0
    new_alliteration = 1
    for w in range(1, len(words_list)):
        if words_list[w][0] == words_list[w - 1][0]:
            alliteration_counter += new_alliteration
            new_alliteration = 0
        else:
            new_alliteration = 1
    print(alliteration_counter)
