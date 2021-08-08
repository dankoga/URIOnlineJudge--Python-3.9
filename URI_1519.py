import re

while True:
    text = input()
    if text == '.':
        break

    initials_dict = dict()
    for word in text.split():
        if len(word) > 2:
            if word[0] in initials_dict:
                if word in initials_dict[word[0]]:
                    initials_dict[word[0]][word] += len(word) - 2
                else:
                    initials_dict[word[0]][word] = len(word) - 2
            else:
                initials_dict[word[0]] = {word: len(word) - 2}

    abbreviations_dict = dict()
    for letter_entry in initials_dict.items():
        abbreviation = letter_entry[0] + '.'
        longest_word = sorted(letter_entry[1].items(), key=lambda x: (-x[1], -len(x[0])))[0]
        abbreviations_dict[abbreviation] = longest_word[0]
        pattern_word = r"\b" + longest_word[0] + r"\b"
        pattern_abrv = abbreviation
        text = re.sub(pattern_word, pattern_abrv,  text)

    print(text)
    print(len(abbreviations_dict))
    for a in sorted(abbreviations_dict.items()):
        print('{} = {}'.format(a[0], a[1]))
