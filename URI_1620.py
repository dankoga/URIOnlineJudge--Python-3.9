if __name__ == '__main__':
    while True:
        vertex_qty = float(input())
        if vertex_qty == 0:
            break
        print('{:.6f}'.format((vertex_qty - 3.0) / vertex_qty))
