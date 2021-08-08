while True:
    try:
        sentence = input()
    except EOFError:
        break
    letter_counter = 0
    dancing_sentence = []
    for letter in sentence:
        if letter.isalpha():
            if letter_counter % 2 == 0:
                dancing_sentence += [letter.upper()]
            else:
                dancing_sentence += [letter.lower()]
            letter_counter += 1
        else:
            dancing_sentence += [letter]
    print(''.join(dancing_sentence))
