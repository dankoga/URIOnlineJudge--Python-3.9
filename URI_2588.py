while True:
    try:
        word = input()
    except EOFError:
        break

    letter_freq = {}
    for letter in word:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1
    odd_freq_qty = sum([letter_freq[k] % 2 for k in iter(letter_freq)])
    print(max(odd_freq_qty - 1, 0))
