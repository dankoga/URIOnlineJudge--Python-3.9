while True:
    try:
        words_list = input().split('-')
    except EOFError:
        break
    cobol = ['Cc', 'Oo', 'Bb', 'Oo', 'Ll']
    if len(words_list) == 5 and all([word[0] in cobol[i] or word[-1] in cobol[i]
                                     for i, word in enumerate(words_list)]):
        print('GRACE HOPPER')
    else:
        print('BUG')
