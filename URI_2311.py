divers_qty = int(input())
for diver in range(divers_qty):
    name = input()
    difficulty = float(input())
    scores = list(map(float, input().split()))
    scores.sort()
    print('{} {:.2f}'.format(name, difficulty * sum(scores[1:-1])))
