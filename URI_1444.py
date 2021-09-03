if __name__ == '__main__':
    while True:
        drakes_qty = int(input())
        if drakes_qty == 0:
            break
        races_qty = 0
        while drakes_qty > 1:
            drakes_qty = (drakes_qty + 2) // 3
            races_qty += drakes_qty

        print(races_qty)
