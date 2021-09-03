if __name__ == '__main__':
    while True:
        try:
            boots_qty = int(input())
        except EOFError:
            break
        boots = dict()
        for _ in range(boots_qty):
            number, side = input().split()
            if number in boots:
                boots[number][ord(side) - 68] += 1
            else:
                boots[number] = [0, 0]
                boots[number][ord(side) - 68] += 1
        pairs = [min(items[1]) for items in boots.items()]
        print(sum(pairs))
