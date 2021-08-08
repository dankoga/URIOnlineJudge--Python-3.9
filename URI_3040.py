christmas_trees_qty = int(input())
for tree in range(christmas_trees_qty):
    height, diameter, branches = map(int, input().split())
    if (200 <= height <= 300) and (diameter >= 50) and (branches >= 150):
        print('Sim')
    else:
        print('Nao')
