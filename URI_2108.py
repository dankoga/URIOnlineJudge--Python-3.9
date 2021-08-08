biggest_word = ''
all_words_list = []
while True:
    text = input().split()
    if text == ['0']:
        break
    word_sizes = [len(word) for word in text]
    all_words_list += list(zip(word_sizes, text))
    print('-'.join([str(s) for s in word_sizes]))
print('\nThe biggest word: {}'.format(sorted(all_words_list, key=lambda x: (-x[0], x[1]))[0][1]))
