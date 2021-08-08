import sys


for word in sys.stdin:
    word = word.rstrip()
    stutters = [s for s in reversed(range(len(word) - 1))
                if word[s + 1:] == word[2 * s - len(word) + 2:s + 1]]
    if len(stutters) == 0:
        print(word)
    else:
        print('\n'.join([word[:s + 1] for s in stutters[::-1]]))
