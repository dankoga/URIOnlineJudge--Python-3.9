competitors_qty = int(input())
votes_carlos = int(input())
votes_other = [int(input()) for c in range(1,competitors_qty)]
if votes_carlos >= max(votes_other):
    print('S')
else:
    print('N')
