pomekons_captured = int(input())
pomekons_set = set()
for p in range(pomekons_captured):
    pomekons_set.add(input())
print('Falta(m) {} pomekon(s).'.format(151 - len(pomekons_set)))
