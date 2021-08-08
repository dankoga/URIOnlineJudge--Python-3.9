while True:
    try:
        voters_qty = int(input())
    except EOFError:
        break

    votes = list(map(int, input().split()))
    if 3 * sum(votes) >= 2 * voters_qty:
        print('impeachment')
    else:
        print('acusacao arquivada')
