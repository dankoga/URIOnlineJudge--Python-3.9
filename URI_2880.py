encrypted_text = input()
crib = input()

valid_crib_count = 0
for begin in range(len(encrypted_text) - len(crib) + 1):
    crib_valid = 1
    for i in range(len(crib)):
        if crib[i] == encrypted_text[begin + i]:
            crib_valid = 0
            break
    valid_crib_count += crib_valid
print(valid_crib_count)
