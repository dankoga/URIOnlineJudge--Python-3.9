text = input().lower()

tokens_freq = dict()
for i in range(1, len(text)):
    if text[i-1:i+1] in tokens_freq:
        tokens_freq[text[i-1:i+1]] += 1
    else:
        tokens_freq[text[i - 1:i + 1]] = 1
most_common = sorted(tokens_freq.items(), key=lambda x: (-x[1], x[0]))[0]
print('{}:{}'.format(most_common[0],most_common[1]))
