import sys

words_list = [word for line in sys.stdin.readlines() for word in line.rstrip().split()]
char_count = 0
for word in words_list:
    if word == '<br>':
        print('\n', end='')
        char_count = 0
        continue

    if word == '<hr>':
        if char_count > 0:
            print('\n', end='')
        print('-' * 80 + '\n', end='')
        char_count = 0
        continue

    if len(word) + char_count + int(char_count > 0) > 80:
        print('\n' + word, end='')
        char_count = len(word)
    elif char_count > 0:
        print(' ' + word, end='')
        char_count += len(word) + 1
    else:
        print(word, end='')
        char_count += len(word)
print()
