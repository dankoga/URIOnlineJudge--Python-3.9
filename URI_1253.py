tests_qty = int(input())
for t in range(tests_qty):
    text = input()
    displacement = int(input())
    print(''.join([chr((ord(letter) - 65 - displacement) % 26 + 65) for letter in text]))
