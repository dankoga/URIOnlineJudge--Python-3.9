runes_total, friendship_min = map(int, input().split())
runes_list = [input().split() for r in range(runes_total)]
runes_dict = {rune[0]: int(rune[1]) for rune in runes_list}

runes_writen_qty = int(input())
runes_writen = list(input().split())

friendship_total = sum([runes_dict[r] for r in runes_writen])
print(friendship_total)
if friendship_total >= friendship_min:
    print('You shall pass!')
else:
    print('My precioooous')
