SWAP_MATRIX = [[1, 0, 2],
               [0, 2, 1],
               [2, 1, 0]]

swaps_qty = int(input())
coin_position = ord(input()) - ord('A')
for s in range(swaps_qty):
    swap_type = int(input())
    coin_position = SWAP_MATRIX[swap_type - 1][coin_position]
print(chr(coin_position + ord('A')))
