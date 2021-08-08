tests_qty = int(input())
for t in range(tests_qty):
    elements_qty = int(input())
    hash_value = 0
    for e in range(elements_qty):
        element = input()
        for c, letter in enumerate(element):
            hash_value += e + c + ord(letter) - 65
    print(hash_value)
