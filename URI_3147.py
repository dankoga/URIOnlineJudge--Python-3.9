humans, elves, dwarves, orcs, wargs, eagles = map(int, input().split())
if(humans + elves + dwarves + eagles >= orcs + wargs):
    print('Middle-earth is safe.')
else:
    print('Sauron has returned.')
