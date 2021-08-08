while True:
    try:
        text = input()
    except EOFError:
        break

    words_list = [word[:-1] if word[-1] == '.' else word for word in text.split()]
    words_list = [word for word in words_list if word.isalpha()]

    if len(words_list) == 0:
        print(250)
        continue

    word_total_length = sum(map(len, words_list))
    score = word_total_length // len(words_list)
    if score <= 3:
        print(250)
    elif score <= 5:
        print(500)
    else:
        print(1000)
