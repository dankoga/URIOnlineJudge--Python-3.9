tests_qty = int(input())
for t in range(tests_qty):
    text = [letter for letter in input() if letter.islower()]
    print(''.join(text[::-1]))
