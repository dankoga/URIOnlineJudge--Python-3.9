def is_vowel(letter):
    return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'


def encrypt(word, key, key_index):
    return ''.join([chr((ord(letter) + ord(key[(key_index + k) % len(key)]) - 2 * ord('a')) % 26 + ord('a'))
                    for k, letter in list(enumerate(word))])


key = input()
sentences_qty = int(input())
for s in range(sentences_qty):
    sentence = input()
    key_index = 0
    sentence_words_encrypted = []
    for word in sentence.split():
        if not is_vowel(word[0]):
            sentence_words_encrypted.append(encrypt(word, key, key_index))
            key_index += len(word)
        else:
            sentence_words_encrypted.append(word)
    print(' '.join(sentence_words_encrypted))
