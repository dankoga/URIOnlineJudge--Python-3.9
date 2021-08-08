tests_qty = int(input())
for t in range(tests_qty):
    text = input().lower()
    letter_frequency = [[i , 0] for i in range(26)]
    for letter in text:
        if letter.isalpha():
            letter_frequency[ord(letter) - 97][1] += 1
    letter_frequency.sort(key=lambda x: (-x[1], x[0]))
    frequency_max = letter_frequency[0][1]
    print(''.join([chr(x[0] + 97) for x in letter_frequency if x[1] == frequency_max]))
