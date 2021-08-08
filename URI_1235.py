tests_qty = int(input())
for t in range(tests_qty):
    sentence_scrambled = input()
    half = len(sentence_scrambled) // 2
    print(sentence_scrambled[half-1::-1] + sentence_scrambled[-1:half-1:-1])
