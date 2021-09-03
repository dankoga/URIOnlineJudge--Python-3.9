def square_range(begin, end, step):
    i = begin
    while i*i <= end:
        yield i*i
        i += step


while True:
    descendants_qty = int(input())
    if descendants_qty == 0:
        break
    print(' '.join([str(d) for d in square_range(1, descendants_qty, 1)]))
