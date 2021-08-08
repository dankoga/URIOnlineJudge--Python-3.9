while True:
    try:
        key_size, lines_qty = map(int, input().split())
    except EOFError:
        break

    key1_upper = input().upper()
    key1_lower = key1_upper.lower()
    key2_upper = input().upper()
    key2_lower = key2_upper.lower()
    cypher1 = key1_upper + key1_lower + key2_upper + key2_lower
    cypher2 = key2_upper + key2_lower + key1_upper + key1_lower

    for line in range(lines_qty):
        text = input()
        cypher_table = text.maketrans(cypher1, cypher2)
        print(text.translate(cypher_table))
    print()
