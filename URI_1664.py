import sys
import re
import math

not_alpha = re.compile(r"[^a-zA-Z ]+")

text = re.sub(not_alpha, ' ', ''.join(sys.stdin.readlines()))
games = 0
total_used_words = 0
used_words_set = set()
for word in text.split():
    if word == 'BULLSHIT':
        total_used_words += len(used_words_set)
        used_words_set = set()
        games += 1
    else:
        used_words_set.add(word.lower())

common_divisor = math.gcd(total_used_words, games)
print('{} / {}'.format(total_used_words // common_divisor, games // common_divisor))
