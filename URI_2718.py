from math import log2

groups_qty = int(input())
for group in range(groups_qty):
    lights_string = int(input())
    if lights_string == 0:
        print(0)
    else:
        string_length = int(log2(lights_string)) + 1
        mask_all = 2 ** string_length - 1
        for mask_length in range(string_length, 0, -1):
            mask = 2 ** mask_length - 1
            while lights_string & mask != mask and mask < mask_all:
                mask <<= 1
            if lights_string & mask == mask:
                print(mask_length)
                break
