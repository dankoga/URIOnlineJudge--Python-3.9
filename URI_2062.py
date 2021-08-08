words_qty = input()
words_list = [[word] for word in input().split()]
for word in words_list:
    if len(word[0]) == 3:
        if word[0][:2] == 'OB':
            word[0] = 'OBI'
        if word[0][:2] == 'UR':
            word[0] = 'URI'
print(' '.join([word[0] for word in words_list]))
