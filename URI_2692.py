exchanged_keys_qty, sentences_qty = map(int, input().split())
key_map =['', '']
for k in range(exchanged_keys_qty):
    keys = input().split()
    key_map[0] += keys[0] + keys[1]
    key_map[1] += keys[1] + keys[0]
for s in range(sentences_qty):
    sentence = input()
    print(sentence.translate(sentence.maketrans(key_map[0], key_map[1])))
